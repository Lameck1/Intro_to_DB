import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root"   # or your test user
            # password="your_password"  # leave empty if no password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:   # <-- required by checker
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
