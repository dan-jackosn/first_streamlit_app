import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Menu")

streamlit.header("Breakfast")
streamlit.text("🥣 Oatmeal")
streamlit.text("🥗 Spinach")
streamlit.text("🐔 Eggs")
streamlit.text("🥑🍞 Avocado Toast")


streamlit.header("🍌🥭 Your Own Fruit Smoothie 🥝🍇")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado","Strawberries"])

streamlit.dataframe(my_fruit_list.loc[fruits_selected])


streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input("What fruit would you like information about ?")
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()
    
streamlit.write("the user entered",fruit_choice)





streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input("What fruit would you like to add?")
streamlit.write("Thanks for adding",add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
