import streamlit
import pandas
import requests
import snowflake.connector


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Menú de desayuno')
streamlit.text('🥣Omega 3 y avena con arándanos')
streamlit.text('🥗Batido de col rizada, espinacas y rúcula')
streamlit.text('🥚Huevo de gallinas camperas hervidas')

streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.
streamlit.dataframe(fruit_to_show)


#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','banana')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json())


# Json to Pandas
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Show Data
streamlit.dataframe(fruityvice_normalized)
