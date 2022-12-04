import streamlit
import pandas


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Menú de desayuno')
streamlit.text('🥣Omega 3 y avena con arándanos')
streamlit.text('🥗Batido de col rizada, espinacas y rúcula')
streamlit.text('🥚Huevo de gallinas camperas hervidas')

streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
