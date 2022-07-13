import streamlit
import pandas as pd

streamlit.title("SnowPro Ninja's Kitchen")
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

lst_fruit = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
lst_fruit = lst_fruit.set_index("Fruit")
fruit_selected = streamlit.multiselect("Select your fruits:", list(lst_fruit.index),['Avocado','Strawberries'])
fruit_to_show = lst_fruit.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
