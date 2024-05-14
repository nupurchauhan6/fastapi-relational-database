import mysql.connector
from mysql.connector import Error


# Function to get database connection
def get_database_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='sample_db',
            user='root',
            password=''
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None
