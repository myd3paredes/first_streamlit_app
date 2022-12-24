import streamlit
import pandas
import snowflake.connector

streamlit.title("My parents new healthy diner")

streamlit.header("🥣    Breakfast Menu")
streamlit.text("🥗 Omega 3 & Blueberry Oatmea")
streamlit.text("🐔 Kale Spinach & Rocket Smoothie")
streamlit.text("🥑🍞 HArd Boiled Free Range Egg")

streamlit.header("🍞🥗 Build your own fruit smoothie 🐔🥣 ")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice")

import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

