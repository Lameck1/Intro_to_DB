import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update with your username/password)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure the connection is closed
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")  # Optional

if __name__ == "__main__":
    create_database()
