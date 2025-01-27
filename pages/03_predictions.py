import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("2025 Predictions")

# Read in monthly data
df = pd.read_csv("daily_steps.csv")
df['date'] = pd.to_datetime(df['date'])
df1 = df.set_index('date')
monthly_steps = df1.resample('ME').mean()

# Read in forecast data
forecast_df = pd.read_csv("combined_forecast.csv", index_col=0)

# Plot forecasts
fig = go.Figure()

# Add step observations
fig.add_trace(go.Scatter(
    x=monthly_steps.index, 
    y=monthly_steps['steps'], 
    mode='lines', 
    name='Historical Data', 
    line=dict(color='blue')
))

# Holt Winters forecast
fig.add_trace(go.Scatter(
    x=forecast_df.index, 
    y=forecast_df['holtwinters'], 
    mode='lines', 
    name="Holt-Winters Forecast", 
    line=dict(color='red', dash='dash')
))


# Add averaged data
fig.add_trace(go.Scatter(
    x=forecast_df.index, 
    y=forecast_df['average'], 
    mode='lines', 
    name='Average by Month', 
    line=dict(color='green', dash='dash')
))

# Add 2024 shifted data
fig.add_trace(go.Scatter(
    x=forecast_df.index, 
    y=forecast_df['shifted'], 
    mode='lines', 
    name='2024 Shifted', 
    line=dict(color='orange', dash='dash')
))

fig.update_yaxes(range=[0, monthly_steps["steps"].max() + 1000])

fig.update_layout(
    title=dict(
        text="Forecasting",
        font=dict(size=24)
    ),
    xaxis=dict(
        title="Month",
        title_font=dict(size=18),
        tickfont=dict(size=14)
    ),
    yaxis=dict(
        title="Steps",
        title_font=dict(size=18),
        tickfont=dict(size=14) 
    ),
    legend=dict(
        font=dict(size=16)
    )
)

st.plotly_chart(fig)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Holt-Winters Forecast")
    st.write("""
    - Smooths time series data
    - Accounts for seasonality
    - Follows the trend downward
             """)

with col2:
    st.markdown("#### Monthly Averages")
    st.write("""
    - Simple, calculates average steps per month
    - Does not weight recent data more heavily
    - Fails to connect with last data point
             """)

with col3:
    st.markdown("#### 2024 Shifted")
    st.write("""
    - Baseline model
    - Calculated by moving 2024 data over a year
    - Does not consider earlier data
             """)
    
st.divider()

col1_, padding, col2_ = st.columns([1, 0.1, 1])

with col1_:  
    st.subheader("Hypothesis")
    st.write("""
            The Holt-Winters forecast does the best job of following the downward trend and accounting for seasonality.
            However, my daily patterns changed significantly in the summer of 2023, so earlier data may not be as relevant for modelling. 
            I will be surprised if my step count continues to decrease over this upcoming year.
            My daily activities are likely to remain very similar from 2024 to 2025, so I expect that the 2024 shifted data will perform the best.
            """)
    
with col2_:  
    st.subheader("Conclusions")
    st.write("""
            Estimating my steps for 2025 proved to be more difficult than I expected.
            Three years of daily data seems plenty, but was challenging with life changes and monthly aggregations.
            Moving forward, I plan to explore more advanced models like SARIMA and XGBoost.
            It would also be interesting to try modeling the data at a weekly or daily level.
            """)
    st.write("Check back in a few months to see which model is performing the best!")