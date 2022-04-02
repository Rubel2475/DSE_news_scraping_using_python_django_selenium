from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import News
from user.models import userInput

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import mysql.connector

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


def news_duration(request):
    return render(request, 'news_duration.html')


def news_scrape(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="",database = "news_db")

    mycursor = mydb.cursor()
    mycursor.execute("select count(*) from news")
    rows = mycursor.fetchone()[0]

    # sql_del = "DELETE FROM news"
    # mycursor.execute(sql_del)
    # mydb.commit()
    
    News.objects.all().delete()
    
    sql_del = "ALTER TABLE news AUTO_INCREMENT = 1;"
    mycursor.execute(sql_del)
    
    print(rows, "record(s) deleted")
    
    sel = request.GET.get('news_duration')
    print(sel)
    
    url_today = "https://dsebd.org/display_news.php"
    url_seven = "https://dsebd.org/news_archive_7days.php"
    url_search = "https://dsebd.org/news_archive.php"
    
    
    driver = webdriver.Chrome('D:\webdriver\chromedriver')
    
    if(sel=="seven"):
        driver.get(url_seven)
        news_header = "Last seven days news"
    
    elif(sel=="search"):
        driver.get(url_search)
        
        # sDate = "'2021-10-05'"
        # eDate = "'2021-11-11'"
        sDate = "'{}'".format(request.GET.get('sDate'))
        eDate = "'{}'".format(request.GET.get('eDate'))
        print(sDate)
        
        driver.execute_script("document.getElementById('startDate').value = " + sDate)
        time.sleep(3)
        
        driver.execute_script("document.getElementById('endDate').value = " + eDate)
        time.sleep(3)
        
        driver.find_element_by_css_selector('[class="center-block btn btn-primary search-by-date"]').click()
        
        news_header = "News from " + sDate + " to " + eDate
          
    else:
        driver.get(url_today)
        news_header = "Today's News"
    
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
    #mycursor.execute("SELECT * FROM news")

    #myresult = mycursor.fetchall()
    myresult = News.objects.all()
    
    context = {
        "dse": myresult,
        "news_header" : news_header,
    }
    
    if request.user.is_authenticated:
        return HttpResponseRedirect("/userpage")
    else:
        return render(request, "home.html", context)




# def news_view(request):
#     dse_news = News.objects.all()
#     context = {
#         "dse": dse_news,
#     }
    
#     return render(request, "home.html", context)





# Create your views here.

# def userpage_view(request):
#     dse_news = News.objects.all()
#     input = userInput.objects.all()
#     context = {
#         "dse": dse_news,
#         "input": input,
#     }
#     return render(request, "userPage.html", context)





    







