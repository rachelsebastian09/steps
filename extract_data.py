import pandas as pd
import glob
import os
import pytz
import numpy as np
import logging as log

# Configure logging
log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

folder = "E:\Projects\Rachel\Steps\Activity Data"

csv_files = glob.glob(os.path.join(folder, "steps*.csv"))

dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df) 

combined_df = pd.concat(dfs, ignore_index=True)

combined_df['timestamp'] = pd.to_datetime(combined_df['timestamp'], utc=True)

mountain_tz = pytz.timezone("America/Denver")
cutoff_date_mt = pd.Timestamp("2023-07-01", tz=mountain_tz)

combined_df['converted_time'] = combined_df.apply(
    lambda row: row['timestamp'].tz_convert("America/New_York") 
    if row['timestamp'] < cutoff_date_mt 
    else row['timestamp'].tz_convert("America/Denver"), 
    axis=1
)

combined_df['date'] = combined_df['converted_time'].apply(lambda x: x.date())

steps_df = combined_df.groupby('date', as_index=False)['steps'].sum()

steps_df['date'] = pd.to_datetime(steps_df['date'])

# Define the date range
start_date = pd.to_datetime("2022-01-01")
end_date = pd.to_datetime("2024-12-31")

# Filter the DataFrame to keep only dates within the range
steps_df = steps_df[(steps_df['date'] >= start_date) & (steps_df['date'] <= end_date)]

# Fill missing values with 25th percentile
fill_25 = round(steps_df["steps"].quantile(0.10))

log.info(f"Filling missing values with {fill_25} steps")

# Create a complete date range from the min to max date in your dataset
date_range = pd.date_range(start=steps_df['date'].min(), end=steps_df['date'].max(), freq='D')

missing_dates = len(set(date_range) - set(steps_df['date']))

# Reindex the steps_df with this complete date range and fill missing dates with 0 for steps
steps_df = steps_df.set_index('date').reindex(date_range, fill_value=fill_25).reset_index()

# Rename the index column to 'date'
steps_df.rename(columns={'index': 'date'}, inplace=True)

log.info(f"Number of missing dates filled in: {missing_dates}")

print(steps_df)

steps_df.to_csv('E:\Projects\Rachel\Steps\daily_steps.csv', index=False)