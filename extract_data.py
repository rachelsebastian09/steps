# Extract data file

# Imports
import pandas as pd
import glob
import os
import pytz
import numpy as np
import logging as log

# Configure logging
log.basicConfig(level=log.INFO, format='%(levelname)s: %(message)s')

# Folder with base data exporting from Fitbit
folder = "E:\Projects\Rachel\Steps\Activity Data"

# The relevant files are csvs starting with "steps"
csv_files = glob.glob(os.path.join(folder, "steps*.csv"))

# Read in the files & combine
dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df) 

combined_df = pd.concat(dfs, ignore_index=True)

# Convert timestamp field to proper time zones
# I lived in Eastern time before 7/1/2023 and Mountain after
combined_df['timestamp'] = pd.to_datetime(combined_df['timestamp'], utc=True)

mountain_tz = pytz.timezone("America/Denver")
cutoff_date_mt = pd.Timestamp("2023-07-01", tz=mountain_tz)

combined_df['converted_time'] = combined_df.apply(
    lambda row: row['timestamp'].tz_convert("America/New_York") 
    if row['timestamp'] < cutoff_date_mt 
    else row['timestamp'].tz_convert("America/Denver"), 
    axis=1
)

# Extract the date from each timestamp
combined_df['date'] = combined_df['converted_time'].apply(lambda x: x.date())

# Total the steps by day
steps_df = combined_df.groupby('date', as_index=False)['steps'].sum()

steps_df['date'] = pd.to_datetime(steps_df['date'])

# Define the date range we're studying
start_date = pd.to_datetime("2022-01-01")
end_date = pd.to_datetime("2024-12-31")

# Filter the DataFrame to keep only dates within the range
steps_df = steps_df[(steps_df['date'] >= start_date) & (steps_df['date'] <= end_date)]

# Get 10th percentile
# I tend to not wear my watch on lazy days, 
# so estimating at this value when there is no data
fill_10 = round(steps_df["steps"].quantile(0.10))

log.info(f"Filling missing values with {fill_10} steps")

# Create a complete date range from the min to max date in your dataset
date_range = pd.date_range(start=steps_df['date'].min(), end=steps_df['date'].max(), freq='D')

# Calculate number of days with no data
missing_dates = len(set(date_range) - set(steps_df['date']))

# Fill in missing step data at 10th percentile
steps_df = steps_df.set_index('date').reindex(date_range, fill_value=fill_10).reset_index()
steps_df.rename(columns={'index': 'date'}, inplace=True)

log.info(f"Number of missing dates filled in: {missing_dates}")

# Show and export df
print(steps_df)
steps_df.to_csv('E:\Projects\Rachel\Steps\daily_steps.csv', index=False)