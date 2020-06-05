# # a = 'Hi, HOW r u'
# # print(a.upper())
# from textblob import TextBlob
import pandas as pd
import numpy as np
# # text = TextBlob('heelo , whatt ar yo dong')
# # # print(text.detect_language())
# # print(text.correct())
# customers1 = [20,31,28,27,17,13,15,14,37,100125]
# df = pd.read_excel(open(r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\SALE DETAIL SHEET OCTOBER 2019.xlsx',"rb"), index_col=None, header=  None)
# tarik = 

# sum_list1 = []
# count_list1 =[]
# for i in customers1:
#     ab = df[df[2] == i]
#     a= (ab[ab[6]== tarik][8]).sum()
#     b= (ab[ab[6]== tarik][8]).count()
#     sum_list1.append(round(a,2))
#     count_list1.append(b)a =
# a= df[df[2] ==20]
# b = a[a[6] == '13-10-2019','14-10-2019'][8]
# # a= df[df[2] ==20][8].sum()
# # a= df[df[2] ==20][8].count()
# print(b.count()pip
# print(b.sum())
import mysql.connector

# conn = mysql.connector.connect(host='localhost', username='root',password='Qwerty@@1234', database='dpr')
# my_cursor = conn.cursor()
# # query = 'create database new_database'
# # query= 'show databases'
# # query2 = 'CREATE TABLE student(name VARCHAR(500),age INT(50),EmailAddress VARCHAR(500))'
# # query2 = 'insert into student(name,age,EmailAddress) values (%s,%s,%s)'
# # values = [
# #     ('love',27,'abc@gmail.com'),
# #     ('preet',27,'xyz@gmail.com'),
# #     ('singh',25,'vahgh@gmail.com'),
# #     ('rahul',29,'syuw@gmail.com'),
# #     ('ravi',19,'xyzwxrg@gmail.com')
# # ]
# query2 = 'select * from student'
# # my_cursor.executemany(query2,values)
# my_cursor.execute(query2)
# for database_name in my_cursor:
#     print(database_name)
# # print(my_cursor.fetchall())
# conn.commit()
# conn.close()
# print(conn)
# import bs4 #import BeautifulSoup
# import requests
# import lxml
# req = requests.get('http://www.punjabsldc.org/realtimepbGen.aspx')
# # print(type(req))
# # print(req.text)
# soup = bs4.BeautifulSoup(req.text, "html.parser")
# # a = soup.select('title')
# print(soup.get_text())
# print(a[0].getText())
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """
# soup = bs4.BeautifulSoup(html_doc, 'html.parser')
# # print(soup.prettify())
# print(soup.p)

# import pyrfc
# ASHOST='myhostserver'
# CLIENT='111'
# SYSNR='00'
# USER='user'
# PASSWD='password'

# conn = pyrfc.Connection(ashost=ASHOST, sysnr=SYSNR, client=CLIENT, user=USER, passwd=PASSWD)
      ############################ Balance Amount   ####################################
import xlwings
import datetime
from datetime import date
import os.path


def balance():
# wb = xlwings.Book(r'\\10.9.32.2\adm\Ash\FY 2019-20\DAILY REPORT\DAILY REPORT FORMAT.xlsx')
    wb = xlwings.Book(r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\DAILY REPORT FORMAT.xlsx')
    xlwings.App().visible=False
    ws = wb.sheets['advance tracking sheet']
    dict1= {
        'C191' : 'J191',
        'C192' : 'J192',
        'C193' : 'J193',
        'C195' : 'J195',
        'C196' : 'J196',
        'C199' : 'J199',
        'C204' : 'J204',
        'C208' : 'J208',
        'C209' : 'J209',
        'C210' : 'J210',
        'C212' : 'J212',
        'C213' : 'J213',
        'C215' : 'J215',
        'C216' : 'J216',
        'C217' : 'J217',
        'C218' : 'J218',
        'C219' : 'J219',
        'C220' : 'J220',
        'C221' : 'J221',
        'C222' : 'J222',
        'C223' : 'J223',
        'C224' : 'J224',
        'C225' : 'J225',
    
    }
    list_amount = []
    for i,j in dict1.items():
        b = ws.range(j). value
        c = b
        list_amount.append(c)
# print(list_amount)   
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")
    x = datetime.datetime.now()
    a = x.strftime("%B")
    # print(d1)
    path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
    # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
    userpath = f'SALE DETAIL SHEET OCTOBER 2019'
    abc = os.path.join(path, userpath+'.xlsx')
    df = pd.read_excel(open(abc,"rb"), index_col=None, header=  None)
    tarik = d1
    # customer_list = []
    # for i in dict1.items():
    #     z = ws.range(i).value
    #     customer_list.append(a)
    # print(customer_list)
    customers2 = [100051,100070,100071,100062,100072,100087,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
    store = []
    for i in customers2:
        ab = df[df[2] == i]
        amount = (ab[ab[6]== tarik][19]).sum()
        store.append(amount)

    final_bal = []   
    for (i, j) in zip(list_amount,store):
        final = round(i - j)
        final_bal.append(final)

    cust_name =[]
    for (i,j) in dict1.items():
        b = ws.range(i). value
        cust_name.append(b)

    bal=list(zip(cust_name, final_bal))


    # print(final_list)
    wb.close()
    print(bal)
a = balance()
print(a)    
                          ##########################################################################




