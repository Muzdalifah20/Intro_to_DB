import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "alx_book_store"
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
     
    print(f"Database  {mydb.database} created successfully!")
except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()


