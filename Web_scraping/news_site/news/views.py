	
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from jmespath import search

from .models import News
from user.models import userInput

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import mysql.connector

from datetime import datetime, date, timedelta
from itertools import chain


def news_duration(request):
    return render(request, 'news_duration.html')


def news_scrape(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="",database = "news_db")

    url_today = "https://dsebd.org/display_news.php"
    url_seven = "https://dsebd.org/news_archive_7days.php"
    url_search = "https://dsebd.org/news_archive.php"
    
    today_date = datetime.now().date()
    #today_date = datetime.today()
    day_name = today_date.strftime('%A')
    
    week = today_date - timedelta(days=7)
    #some_day_last_week = timezone.now().date() - timedelta(days=7)
    
    today_date = today_date.strftime('%Y-%m-%d')
    week = week.strftime('%Y-%m-%d')
    
    print(today_date)
    print(day_name)
    
    #print(some_day_last_week)
    
    news = News.objects.all()
    print(news[0].news_date)
    
    news_date = news[0].news_date
    news_date = news[0].news_date.strftime('%Y-%m-%d')
    
    if (news_date != today_date) and (day_name != 'Friday' and day_name != 'Saturday'):
        
        mycursor = mydb.cursor()
        mycursor.execute("select count(*) from news_news")
        rows = mycursor.fetchone()[0]
    
        News.objects.all().delete()
        
        sql_del = "ALTER TABLE news_news AUTO_INCREMENT = 1;"
        mycursor.execute(sql_del)
        print(rows, "record(s) deleted")
        
        driver = webdriver.Chrome('D:\webdriver\chromedriver')
    
        driver.get(url_search)
            
        sDate = "'2022-01-01'"
        print(sDate)
        #eDate = "'2021-11-11'"
        eDate = "'{}'".format(today_date)
        print(eDate)
        
        driver.execute_script("document.getElementById('startDate').value = " + sDate)
        time.sleep(3)
        
        driver.execute_script("document.getElementById('endDate').value = " + eDate)
        time.sleep(3)
        
        driver.find_element_by_css_selector('[class="center-block btn btn-primary search-by-date"]').click()
        
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
            sql = "INSERT INTO news_news (trading_code_id, news_title, news, news_date) VALUES (%s, %s, %s, %s)"
            val = (trading_code[k], news_title[k], news[k], post_date[k])
            mycursor.execute(sql, val)
            r=r+1

        mydb.commit()

        print(element_per_col_in_dbTable, "record(s) inserted.")
        
    
    myresult = News.objects.all()

    sel = request.GET.get('news_duration')
    print(sel)

    if(sel=="seven"):
        news_header = "Last seven days news"

        days = 7
        seven_days_news = News.objects.filter(news_date=today_date)
        
        for day in range(days-1):
            seven_days_news = list(chain(seven_days_news, News.objects.filter(news_date=datetime.now() - timedelta(days=day))))
                
        news = seven_days_news
        
        context = {
            "dse": seven_days_news,
            "news_header" : news_header,
        }
        

    elif(sel=="search"):
        #pass
        news_header ="search news"
        
        Date1 = request.GET.get('sDate')
        print(Date1)
        Date2 = request.GET.get('eDate')
        
        ymd_date_1 = Date1
        ymd_date_2 = Date2
        # Creates actual date objects from our string values.
        date_1 = date.fromisoformat(ymd_date_1)
        date_2 = date.fromisoformat(ymd_date_2)
        # Subtracting a date object from another gives a timedelta object,
        #   which has a useful .days attribute.
        total_days = abs(date_1 - date_2).days
        print(total_days)
        
        search_news = News.objects.filter(news_date=Date2)
        
        days = total_days
        Date2 = date.fromisoformat(Date2)
        
        for day in range(days-1):
            search_news = list(chain(search_news, News.objects.filter(news_date=Date2 - timedelta(days=day))))
        
        news = search_news
        
        context = {
            "dse": search_news,
            "news_header" : news_header,
        }
        
    else:
        news_header = "Today's News"
        today_news = News.objects.filter(news_date=today_date)
        news = today_news
        
        context = {
            "dse": today_news,
            "news_header" : news_header,
        }
        

    if request.user.is_authenticated:
        
        input = userInput.objects.all()
        user_name = request.user.get_username()
        
        context = {
            "dse": news,
            "input": input,
            "logged_username": user_name,
        }
        return render(request=request, template_name='userPage.html', context=context)
        #return HttpResponseRedirect("/userpage")
        #return redirect('userpage_view', dse_news=news)
        #return render(request, "userPage.html", context)
    else:
        return render(request, "home.html", context)