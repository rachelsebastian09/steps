import streamlit as st
import pandas as pd
from PIL import Image, ImageOps

st.set_page_config(layout="wide")

st.title("Stepping into the New Year")

st.write("""Fitness trackers like Fitbit have transformed how we monitor daily activity, providing valuable data on step counts over time. 
         This project explores my step count data from 2022 to 2024 to identify trends and patterns in my steps.
         Using time-series analysis and machine learning, I will analyze past steps and forecast future step counts.""")

st.header("Data Ingestion")

st.markdown(
    'For full details on the ingestion process, view the <a href="https://www.youtube.com/watch?v=BBJa32lCaaY" target="_blank">script</a>.',
    unsafe_allow_html=True
)

cols = st.columns(3)

img = Image.open("images/fitbit.jpg")

# Add a white border (size in pixels)
border_size = 100
img_with_border = ImageOps.expand(img, border=border_size, fill="white")

# Display in Streamlit
cols[0].image(img_with_border, width=200)

col1, col2, col3 = st.columns(3)

with col1:

    st.write("#### Extract")

    st.write("""Fitbit has basic analytical functionality in their app,
            but in order to receive the raw data I had to request it.""")

with col2:

    st.write("#### Transform")

    st.write("""In this step I aggregated the data by day, corrected time zones, and filled in missing values.""")

with col3:

    st.write("#### Load")

    st.write("""Output a new csv with the processed information in the desired location.""")
             
st.subheader("Assumptions & Predictions")

