import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(fruit_choice):
    streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #streamlit.text(fruityvice_response.json())
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    
    return fruityvice_normalized

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list ")
        my_data_rows = my_cur.fetchall()
        
    return my_data_rows

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values('from streamlit')")
    return 'Thanks for adding: ' + new_fruit

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

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select fruit to get information.")
  else:
    fruityvice_normalized = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

if streamlit.button("Get Fruit Load List"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

if streamlit.button("What fruit would you like to add?"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    fruit_add = insert_row_snowflake(fruit_add)
    streamlit.text(fruit_add)

