import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
streamlit.title("My parents new healthy diner")

streamlit.header("🥣    Breakfast Menu")
streamlit.text("🥗 Omega 3 & Blueberry Oatmea")
streamlit.text("🐔 Kale Spinach & Rocket Smoothie")
streamlit.text("🥑🍞 HArd Boiled Free Range Egg")

streamlit.header("🍞🥗 Build your own fruit smoothie 🐔🥣 ")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice")

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

#snowflake

my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_rows)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

add_my_fruit = streamlit.text_input('What fruit would you like to add?','')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")


my_cur.execute("insert into fruit_load_list values ('from streamlit')")
