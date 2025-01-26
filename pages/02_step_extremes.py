import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import timedelta
from PIL import Image, ImageOps

st.header("Most Steps")
st.write("Month: September 2022 with 11,681 steps per day. The increase is probably due to college starting back up in the fall.")
st.write("""Week: September 30, 2024 - October 6, 2024. I averaged 22,947 steps per day. I spent this week camping in Utah,
         going to national parks and hiking a lot. Below are some highlights! It was an awesome trip.""")

cols = st.columns(3)

# Put a border around the first image & display
stars = Image.open("images/stars.JPG")
stars_border = ImageOps.expand(stars, border=4, fill="lightgrey")
cols[0].image(stars_border, caption="Milky Way")

# Displayed the two landscape photos in the second column
cols[1].image("images/bryce.jpg", caption="Bryce Canyon")
cols[1].image("images/arches.JPG", caption="Windows Arch")

# Rotate the fourth image to the correct orientation and display
image4 = Image.open("images/waterfall.jpg")
image4_rotated = image4.rotate(270, expand=True) 
cols[2].image(image4_rotated, caption="Lower Calf Creek Falls")

st.write("""Day: October 5, 2024 with 29,431 steps. Outside of the Utah trip, August 26, 2023 with 28,505 steps. 
         That day I went on a hike to a lake in the morning, then a Broncos preseason game in the evening.""")

cols = st.columns(3)

# Display Oct 5 images
cols[0].image("images/lake.jpg", caption="Brainard Lake")
cols[1].image("images/moose.jpg", caption="Moose!")
cols[2].image("images/broncos.jpg", caption="Broncos Game")

st.header("Least Steps")
st.write("""Month: In both June 2023 and Nov-Dec 2024, I averaged less than 7,000 steps/day. June 2023 was the time between when I graduated college and moved,
         so I was out of a routine. Not sure about November and December of last year other than the weather.""")
st.write("""Performing meaningful analysis by week or day is more difficult since most of the times looked at had lots of missing values. 
         Unfortunately there were no pictures to be found on my least stepped days.""")
