import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import mysql.connector

#connection to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "news_db"
)

mycursor = mydb.cursor()

sql_del = "DELETE FROM news"
mycursor.execute(sql_del)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")


url = "https://dsebd.org/news_archive_7days.php"

driver = webdriver.Chrome('D:\webdriver\chromedriver')
driver.get(url)

time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")


table_data = soup.find("table", attrs={"class": "table-news"})
table_rows = table_data.tbody.find_all("tr")  # contains rows

number_of_rows = len(table_rows)
print(number_of_rows)

#Get all the data of Lists
data = []

for i in range(number_of_rows):
    for td in table_rows[i].find_all("td"):
        # remove any newlines and extra spaces from left and right
        data.append(td.text.replace('\n', ' ').strip())
        #print(td.text)

#print(data)

number_of_td = len(data)


trading_code = []
news_title = []
news = []
post_date = []

for j in range(number_of_td):
    if j%4==0:
        trading_code.append(data[j])
    elif j%4==1:
        news_title.append(data[j])
    elif j%4==2:
        news.append(data[j])
    elif j%4==3:
        post_date.append(data[j])

# print(trading_code)
# print(news_title)
# print(news)
# print(post_date)

driver.close() # closing the webdriver


#store news dato database
if(number_of_td%4==0):
    element_per_col_in_dbTable = int(number_of_td / 4)
else:
    element_per_col_in_dbTable = int(number_of_td / 4)+1
        
r=0 #for counting how many records are inserted
for k in range(element_per_col_in_dbTable):
    sql = "INSERT INTO news (trading_code, news_title, news, news_date) VALUES (%s, %s, %s, %s)"
    val = (trading_code[k], news_title[k], news[k], post_date[k])
    mycursor.execute(sql, val)
    r=r+1

mydb.commit()

print(element_per_col_in_dbTable, "record(s) inserted.")



#fetch data from database
mycursor.execute("SELECT * FROM news")

myresult = mycursor.fetchall()

#t_code = input("Enter tranding code of company: ")
t_code ="EXCH"

for row in myresult:
    if row[1]==t_code:
        print(row[0])
