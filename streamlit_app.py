import streamlit
import pandas

streamlit.title("My parents new healthy diner")

streamlit.header("🥣    Breakfast Menu")
streamlit.text("🥗 Omega 3 & Blueberry Oatmea")
streamlit.text("🐔 Kale Spinach & Rocket Smoothie")
streamlit.text("🥑🍞 HArd Boiled Free Range Egg")

streamlit.header("🥑🍞🥗 Build your own fruit smoothie 🐔🥣 ")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
