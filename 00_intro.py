import streamlit as st
import pandas as pd
from PIL import Image, ImageOps

st.set_page_config(layout="wide")

st.title("Stepping into the New Year")

st.write("""Fitness trackers like Fitbit have transformed how we monitor daily activity, providing data on step counts over time. 
         This project explores my step count data from 2022 to 2024 to identify trends and patterns in my steps.
         Using time-series analysis and modeling techniques, I will analyze past steps and forecast future step counts.""")

st.subheader("Data Ingestion")

st.markdown(
    'For full details on the ingestion process, go to extract_data.py in the GitHub <a href="https://github.com/rachelsebastian09/steps/tree/main" target="_blank">repo</a>.',
    unsafe_allow_html=True
)

df = pd.read_csv('daily_steps.csv')

col1, arrow1, col2, arrow2, col3, col4 = st.columns([0.5, 0.3, 0.8, 0.3, 0.8, 1.3])

with col1:
    fitbit = Image.open("images/fitbit.jpg")

    # Add a white border
    fitbit_border = ImageOps.expand(fitbit, border=50, fill="white")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image(fitbit_border, caption="Fitbit Inspire 2")

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

    st.image("images/spreadsheets.png", use_container_width=True, caption="Data Export")

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
    st.dataframe(df, hide_index=True)

with col4:

    st.write("#### Extract")

    st.write("""Fitbit has basic analytical functionality in their app,
            but in order to receive the raw data I had to request it.""")

    st.write("#### Transform")

    st.write("""Aggregated the data by day, corrected time zones, and filled in missing values.""")

    st.write("#### Load")

    st.write("""Saved a new csv with the processed information in the desired location for building this dashboard.""")

st.divider()

col1_, padding, col2_ = st.columns([1, 0.1, 1])

with col1_:
    st.subheader("Assumptions")

    st.markdown("""
    **Time:**
    - All steps before 7/1/2023 occured in Eastern Time
    - All steps on or after 7/1/2023 occured in Mountain Time
    - Reasoning: I moved from Eastern to Mountain Time on 7/1/2023. In the raw files, 
                all time was in UTC, and there was no easy way to convert back to local time for every scenerio.
    - Everything needed to be in local time for consistency of daily patterns
    """)

with col2_:

    st.subheader("")

    st.markdown("""
    **Missing Values:**
    - Any days with no values were set to the 10th percentile of the dataset: 4,014 steps
    - Reasoning: I usually don't wear my watch on slower days. Sometimes I forget to wear it, 
                but most of the time it's on days when I don't go anywhere.
    """)