import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "news_db"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE news (trading_code VARCHAR(50), news_title VARCHAR(255), news Varchar(10000), news_date date)")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
