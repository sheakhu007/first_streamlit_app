""""
Project: Streamlit App
Date: 13 July 2023
Snowflake certification
"""
import streamlit
import pandas as pd
streamlit.title("""My Parents Healthy Dinner""")
streamlit.header('🍞Breakfast Menu')
streamlit.text(' 🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

df = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.text("DF")
streamlit.dataframe(df)
streamlit.text("Table")
streamlit.table(df)
