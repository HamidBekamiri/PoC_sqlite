import streamlit as st
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('example.db')

# Create a table for storing names and ages
conn.execute('''CREATE TABLE IF NOT EXISTS people
                (id INTEGER PRIMARY KEY,
                 name TEXT,
                 age INTEGER)''')

# Define a function for inserting new data into the database
def insert_data(name, age):
    conn.execute("INSERT INTO people (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    st.success("Data inserted successfully!")

# Define a function for searching the database
def search_data(name):
    cursor = conn.execute("SELECT * FROM people WHERE name=?", (name,))
    rows = cursor.fetchall()
    if not rows:
        st.warning("No data found!")
    else:
        st.write("Search results:")
        for row in rows:
            st.write(row)

# Create a Streamlit app
st.title("Simple Database App")

# Add input fields for entering new data
name = st.text_input("Enter a name:")
age = st.number_input("Enter an age:")

# Add a button to insert new data into the database
if st.button("Insert data"):
    insert_data(name, age)

# Add input field for searching the database
search_name = st.text_input("Search by name:")

# Add a button to search the database
if st.button("Search data"):
    search_data(search_name)
