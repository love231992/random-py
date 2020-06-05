import pymysql

connection=pymysql.connect(host='localhost',user='root',password='',database='vms')
cur = connection.cursor()

def login(tup):
    cur.execute("SELECT * FROM user_login WHERE username = %s AND password = %s", tup)
    return (cur.fetchone())
    print("welcome")
   