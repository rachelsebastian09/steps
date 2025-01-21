import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import timedelta

st.set_page_config(layout="wide")

st.title("Step Analysis")

df = pd.read_csv('E:\Projects\Rachel\Steps\daily_steps.csv')
df["date"] = pd.to_datetime(df["date"])

with st.sidebar:

    st.header('Select Plot Inputs')

    min_date = df['date'].min()
    max_date = df['date'].max()

    time_period_choice = st.selectbox("Plotting Aggregation:", ["Month", "Week", "Day"])

    start_date = min_date

    if time_period_choice in ("Week", "Day"):
        start_date = max_date - timedelta(days=60)

    date_choice = st.date_input("Date Range: ",
                                (start_date, max_date),
                                min_value=min_date,
                                max_value=max_date
                                )
    

if len(date_choice) == 1:
    end_date = df['date'].max()
else:
    end_date = date_choice[1]

start = date_choice[0].strftime('%Y-%m-%d')
end = end_date.strftime('%Y-%m-%d')

filtered_df = df[(df['date'] >= start) & (df['date'] <= end)]

if time_period_choice == "Month":
    filtered_df['plotting_period'] = filtered_df['date'].dt.to_period('M')
elif time_period_choice == "Week":
    filtered_df['plotting_period'] = filtered_df['date'].dt.to_period('W')
else:
    filtered_df['plotting_period'] = filtered_df['date']

avg_steps = filtered_df.groupby('plotting_period')['steps'].mean().reset_index()
avg_steps['plotting_period'] = avg_steps['plotting_period'].astype(str)

fig = px.line(avg_steps, x='plotting_period', y='steps', title='Average Steps per Day', labels={'plotting_period': time_period_choice, 'steps': 'Steps'})

fig.update_yaxes(range=[0, avg_steps["steps"].max() + 1000])

# Show the plot
st.plotly_chart(fig)

st.header("Interpretation")
st.write("""Overall, my average steps monthly are decreasing. However,
         I have more variation in my steps in the past year than before, which can be explained due to lifestyle changes.
         In the summer of 2023, I graduated from college and moved to Colorado. This seems to have lead to more sedentary day to day life,
         but making the most of my PTO and weekends in the mountains.""")

df["year"] = df["date"].dt.year.astype(str)
stats_by_year = df.groupby("year")["steps"].agg(["min","mean", "median", "max", "std"]).round(2)

st.write(stats_by_year)