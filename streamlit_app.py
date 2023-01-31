import streamlit
import pandas

streamlit.title("Menu")

streamlit.header("Breakfast")
streamlit.text("🥣 Oatmeal")
streamlit.text("🥗 Spinach")
streamlit.text("🐔 Eggs")
streamlit.text("🥑🍞 Avocado Toast")


streamlit.header("🍌🥭 Your Own Fruit Smoothie 🥝🍇")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
