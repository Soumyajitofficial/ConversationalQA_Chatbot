import sqlite3
import pandas as pd

# Function to establish a connection to SQLite DB
def get_db_connection():
    connection = sqlite3.connect('conversation_history.db')  # Change the file name as needed
    return connection

# Function to fetch the table structure dynamically from SQLite using PRAGMA table_info()
def fetch_table_structure(table_name):
    connection = get_db_connection()  # Get the connection to the SQLite database
    cursor = connection.cursor()  # Create a cursor object to execute SQL commands
    
    # Query to retrieve the table structure using PRAGMA table_info
    query = f"PRAGMA table_info({table_name});"
    cursor.execute(query)
    
    # Fetch the table structure
    structure = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Convert the structure into a pandas DataFrame
    df_structure = pd.DataFrame(structure, columns=['Column Index', 'Column Name', 'Data Type', 'Not Null', 'Default Value', 'Primary Key'])
    return df_structure

# Fetch and display the table structure dynamically
df_structure_dynamic = fetch_table_structure('conversation_history')

import ace_tools as tools; tools.display_dataframe_to_user(name="Dynamic Table Structure DataFrame", dataframe=df_structure_dynamic)

df_structure_dynamic
