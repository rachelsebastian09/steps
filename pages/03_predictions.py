import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

st.title("2025 Predictions")

st.subheader("Checking Stationary & Seasonality")

df = pd.read_csv("daily_steps.csv")
df['date'] = pd.to_datetime(df['date'])
df1 = df.set_index('date')
monthly_steps = df1.resample('ME').mean()

decomposition = seasonal_decompose(monthly_steps, model='additive', period = 12)

#  Create Matplotlib figure
fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

decomposition.observed.plot(ax=axes[0], title="Observed")
decomposition.trend.plot(ax=axes[1], title="Trend")
decomposition.seasonal.plot(ax=axes[2], title="Seasonality")
decomposition.resid.plot(ax=axes[3], title="Residuals")

plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)
