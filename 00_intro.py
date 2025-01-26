import streamlit as st
import pandas as pd
from PIL import Image, ImageOps

st.set_page_config(layout="wide")

st.title("Stepping into the New Year")

st.write("""Fitness trackers like Fitbit have transformed how we monitor daily activity, providing valuable data on step counts over time. 
         This project explores my step count data from 2022 to 2024 to identify trends and patterns in my steps.
         Using time-series analysis and modeling techniques, I will analyze past steps and forecast future step counts.""")

st.header("Data Ingestion")

st.markdown(
    'For full details on the ingestion process, view the <a href="https://www.youtube.com/watch?v=BBJa32lCaaY" target="_blank">script</a>.',
    unsafe_allow_html=True
)

df = pd.read_csv('daily_steps.csv')

col1, arrow1, col2, arrow2, col3, col4 = st.columns([0.7, 0.4, 0.9, 0.4, 0.8, 1.5])

# col1, col2, col3 = st.columns([0.5, 1, 1])

with col1:
    fitbit = Image.open("images/fitbit.jpg")

    # Add a white border
    fitbit_border = ImageOps.expand(fitbit, border=100, fill="white")

    st.write("")
    st.write("")
    st.write("")

    st.image(fitbit_border, width=200, caption="My Fitbit")

with arrow1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image("images/arrow.jpg")

with col2:

    st.write("")
    st.write("")

    st.image("images/spreadsheets.png", caption="Data Export")

with arrow2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image("images/arrow.jpg")

with col3:
    st.dataframe(df)

with col4:

    st.write("#### Extract")

    st.write("""Fitbit has basic analytical functionality in their app,
            but in order to receive the raw data I had to request it.""")

    st.write("#### Transform")

    st.write("""Aggregated the data by day, corrected time zones, and filled in missing values.""")

    st.write("#### Load")

    st.write("""Saved a new csv with the processed information in the desired location for building this dashboard.""")
             
st.subheader("Assumptions & Predictions")

