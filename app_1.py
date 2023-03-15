import streamlit as st
import sqlite3

# create a connection to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS example_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# add some data to the table
c.execute("INSERT INTO example_table (name, age) VALUES ('John', 25)")
c.execute("INSERT INTO example_table (name, age) VALUES ('Mary', 30)")
c.execute("INSERT INTO example_table (name, age) VALUES ('Bob', 40)")

# commit the changes
conn.commit()

# display the data from the table
st.write("Data from the database:")
result = c.execute("SELECT * FROM example_table")
for row in result:
    st.write(row)

# close the connection to the database
conn.close()
