# print(("Hello world"))
# print("this is \\\ double backslash")
# print("this is /\\/\\/\\/\\ mountain")
# # print("this \t awesome")
# number = [1,2,3,4,5,6]
# # name = ["abv", "preet", "singh","mehra",100,2.3,5, None]
# # print(name[2])
# # print(number[-2])
# friuts = ['mango', 'apple',"abv", "preet", "singh","mehra"]
# # friuts.insert(0,'litchi')
# friuts.pop(2)
# friuts.remove('singh')
# del friuts[0]
# # # print(friuts)
# # # i,n,f,o = "a,c,b,d".split(',')
# # # print(i+n+f,o)
# # list = ['love','24']
# # print(','.join(list))
# numbers = list(range(1,100))
# print(numbers.index(3))
# 
# def square(l):
#     num = []
#     for i in l:
#         num.append(i**2)
#     return num

# number = list(range(1,10))
# print(square(number))

# def even_odd(l):
#     odd = []
#     even = []
#     for i in l:
#         if i%2 ==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return odd,even 

# num = [1,2,3,4,5,6,7,8,9]
# print(even_odd(num))

# def common(l1,l2):
#     num = []
#     for i in l1:
#         if i in l2:
#             num.append(i)
#     return num

# num = [1,2,3,4,5,6,7,8,9]
# print(max(num))

# print(common([1,2,5,8], [1,2,7,6,8]))

# mix = 1,
# # print(type(mix)) 

# word = 'one', 'two'
# word1, word2 = (word)
# # print(word2)       

# num = tuple(range(1,10))

# # print(num)
# user = {'name': 'lovepreet', 'age' : 27}
# print(user)
# print(type(user))

# user1 = dict(name = 'love', age = 27)
# print(user1['name'])
# # print(user1['age'])

# user= {}
# user['name']= 'love'
# user['age']= 27
# user['height']= '172cm'

# print(user.items())
# print(user)
# print(user.keys())
# # print(user.values())
# for i,j in user.items():
# #     print(f"{i} + {j}")
# print(user)
# popped_item = user.popitem()
# print(user.popitem())
# print(type(popped_item))
# user= {}
# user['name']= 'love'
# user['age']= 27
# user['height']= '172cm'

# more = {'weight': '50KG', 'qualification': 'Bachelors'}
# # user.update(more)
# # # print(user)
# # print(dict.fromkeys(['name','age',],'unknown'))
# print(more.get('50KG'))
# def cube(n):
#     Value = {}
#     for i in range(1,n+1):
#         Value[i]= i**3
#     return Value

# print(cube(5))

# def counter(n):
#     num = {}
#     for i in n:
#         num[i] = n.count(i)
#     return num

# print(counter('lovEpreet'))
# nm = input('enter your name :')
# ag = input('enter your age :')
# fm = input('enter your fav movie :')
# dictionary = {'name':nm,'age':ag,'fav_movie':fm}
# for key,value in dictionary.items():
#     print(f'{key} : {value}')

# s={'a','b','c'}
# # s.add(56)
# # s.remove(2)
# # print(s)
# # a = (1,24,5,87,6,3,5)
# # s2 = set(a)
# # print(s2)
# # print(type(s2))
# for item in s:
#     print(item)

# s1={1,2,3,4}
# s2={3,4,5,6}
# Union=s1|s2
# print(Union)
# print(s1&s2)

# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# square2=[-i for i in range(1,6)]
# print(square2)

# name=['love','preet','amritsar']
# # first_char=[]
# # for i in name:
# #     first_char.append(i[0])
# # print(first_char)

# name2= [i[0] for i in name]
# print(name2)

# def rev(l):
#     return[i[::-1] for i in l]
# print(rev(['abc','zxc']))
# number = list(range(1,11))
# even=[]
# for i in number:
#     if i%2==0:
#         even.append(i)
# print(even)

# even1 = [i for i in number if i%2==0]
# print(even1)

# import math
# print(math)
# import random
# # for i in range(1,10):
# #     x=random.random()
# #     print(x)
# x=[1,2,3,4,5,6] 
# random.choice(x)
# # print(x)
# x=0
# while x<5:
#     print(x)
#     x=x+1

# def num_str(l):
#     num =[]
#     for i in l:
#         if type(i) == int:
#             num.append(str(i))      
#     return(num)

# print(num_str(['true', 'false', [1,2,3],1,1.0,3]))

# def num_str(l):
#     return [ str(i) for i in l if (type(i) == int or type(i)== float)]

# print(num_str(['true', 'false', [1,2,3],1,1.0,3]))

# num = [1,2,3,4,5,6,7,8,9]
# new_list=[]
# for i in num:
#     if i%2==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

# new_list = [i*2 if (i%2==0) else -i for i in num]
# print(new_list)

# nested_list = [[i for i in range(1,4)] for i in range(3)]
# print(nested_list)

# square={i:i**2 for i in range(1,6)}
# print(square)

# string ="lovepreet"
# count ={i:string.count(i) for i in string}
# print(count)

# even_odd = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(even_odd)

# def fun(num,**kwargs):
#     return(num,kwargs)
# num1 = fun("Hello", first_name = 'Lovepreet', second_name = 'Singh')
# print(num1)
# name = "love"
# print(name.title())
# def cap_rev(a,**kwargs):
#     if kwargs.get("reverse_str")==True:
#         return [name[::-1].title() for name in l]
#     else:
#         return[name.title() for name in l]
# num =lambda a,b: a+b
# print(num(2,3))

# def num(s):
#     if len(s) > 5:
#         return True
# print(num('love'))

# string = lambda s: len(s) > 5 
# print(string('Love'))
# names = ['abc', 'bca','hjk']
# # for pos, name in enumerate(names):
# #     print(f'{pos} ----> {name}')

# length = list(map(len , names))
# # for i in length:
# #     print(i)
# print(length)

# nums = [1,5,2,4,7,8,3,69,10,22]
# even1 = list(filter(lambda a: a%2 ==0, nums))
# print(even1)
# dict()
# l = [(1,2),(3,4),(5,6),(7,8)]
# l1,l2 = zip(*l)
# print(l1)
# print(l2)
# l1=(1, 3, 5, 7)
# l2=(2, 4, 6, 8)
# list =[]
# for i in zip(l1,l2):
#     list.append(max(i))
# print(list)

# avg_finder = lambda *args : [sum(pair)/ len(pair) for pair in zip(*args)]
# print(avg_finder([1,2,3],[4,5,6],[7,8,9]))

# num = [2,5,6,8,10]
# print(all([i%2==0 for i in num]))

# fruit = ('grape', 'mango', 'apple')

# # print(sorted(fruit))
# print(min.__doc__)
# help(sum)

# def out_fun(x):
#     def Inn_fun(n):
#         return n**x
#     return Inn_fun

# var = out_fun(3)  
# print(var(3502))
# from functools import wraps
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         '''this is wrapper'''
#         print('You are calling add function')
#         return func(*args,**kwargs)
#     return wrapper

# @decorator
# def fun(a,b):
#     '''this is add func'''
#     return a+b

# print(fun(2,5))

# print(fun.__doc__)
        
# def gen_func(n):
#     for i in range(1,n+1):
#         if i%2==0:   
#             yield i

# for i in gen_func(10):
#     print(i)

# def gen_func2(a):
#     yield[i for i in range(1,a+1) if i%2==0]

# for i in gen_func2(10):
#     print(i)  

# A simple example class 
# class Test: 
	
# 	# A sample method 
# 	def fun(self): 
# 		print("Hello") 

# # Driver code 
# obj = Test() 
# obj.fun()                    

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = brand + ' '+ model

#     def disc(self, n):
#         v = ((n/100)*self.price)
#         ap= self.price - v
#         return ap
# l = Laptop('Asus', 'Aspire 5755 G' , 40000)
# # print(f'The brand is {l.brand} and model is {l.model} with price tag of {l.price}')
# print(l.disc(40))

# class Circle:
# #     pi = 3.14
# #     def __init__(self, r):
# #         self.r = r
# #     def circum(self):
# #         return 2*self.pi*self.r

# # # c= Circle(4)
# # # c1 = Circle(5)
# # # print(c.circum(), c1.circum()) 

# # from datetime import date 
  
# # class Person: 
# #     def __init__(self, name, age): 
# #         self.name = name 
# #         self.age = age 
      
# #     # a class method to create a Person object by birth year. 
# #     @classmethod
# #     def fromBirthYear(cls, name, year): 
# #         return cls(name, date.today().year - year) 
      
#     # a static method to check if a Person is adult or not. 
# #     @staticmethod
# #     def isAdult(age): 
# #         return age > 18
  
# # person1 = Person('lovepreet', 27) 
# # person2 = Person.fromBirthYear('lovepreet', 1992) 
  
# # print(person1.age) 
# # print(person2.age)
  
# # # print the result 
# # print(Person.isAdult(22)) 

# # class Alphabet: 
# #     def __init__(self, value): 
# #         self._value = value 
          
# #     # getting the values 
# #     def getValue(self): 
# #         print('having value') 
# #         return self._value 
          
# #     # setting the values 
# #     def setValue(self, value): 
# #         print('Setting value to ' + value) 
# #         self._value = value 
          
# #     # deleting the values 
# #     def delValue(self): 
# #         print('Deleting value') 
# #         del self._value 
      
# #     value = property(getValue, setValue, delValue, ) 
  
# # # passing the value 
# # x = Alphabet('how are you') 
# # print(x.value) 
  
# # x.value = 'GfG'
  
# # del x.value 

# class Phone:
#     def __init__(self,brand, model, price):
#         self.brand = brand
#         self.model =  model
#         self._price = max(price,0)
#         self.complete = f"{self.brand} {self.model} and price is {self.price}"
#     @property
#     def full_spec(self):
#         return f"{self.brand} {self.model} and price is {self._price}"
#     @property
#     def price(self):
#         return self._price
#     @price.setter
#     def price(self, new_price):
#         self._price =  max(new_price,0)       

# phone1 = Phone('nokia', 'N8', 24000)
# phone1.price = -50000
# print(phone1._price)  
# print(phone1.full_spec)  
# print(phone1.complete)

# def divison(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as errr:
#         print(errr) 
#     except:
#         print('unexpected error')       
      

# print(divison(4,2))    

# def validate(name):
#     if len(name) < 8:
#         raise ValueError

# user = input('enter your  name : ')
# validate(user)
# # print(f'hello {user}')      
# from csv import DictReader, DictWriter

# with open('csv.csv', 'w', newline='') as wf:
#     csv_write = DictWriter(wf, fieldnames = ['fname','lname','age','city'])
#     csv_write.writeheader()
#     csv_write.writerows([{'fname':'lovepreet','lname':'singh','age': 27, 'city': 'amritsar'},
#         {'fname':'preet','lname':'singh','age': 25, 'city': 'rajpura'}
    # ])
# import os    
# print(os.getcwd())    
# os.mkdir('OS')
# print(os.path.exists('OS'))
# open('text.txt', 'a').close()
# os.chdir(r'D:\Ash')
# os.mkdir(r'D:\Ash\new')
# print(os.getcwd())
# print(os.listdir(r'D:\Ash'))
# for i in os.listdir():
#     print(os.path.join(os.getcwd(),i))
# f_iter = os.walk(r'D:\python')
# for current_path, folder, file in f_iter:
#     print(f'current path: {current_path}')
#     print(f'folder: {folder}')
#     print(f'file: {file}')
# os.makedirs('new/new1')

# import shutil
# shutil.rmtree('new')
# os.mkdir('new`')
# shutil.copytree('new', 'os/new')
# shutil.copy('csv.csv', 'OS/csv.csv')
# shutil.move('text.txt','OS/text.txt')
# from PIL import Image
# img1 = Image.open('Love 1.jpg')
# img1.save('Love 1.pdf')
# from textblob import TextBlob
# text = TextBlob('welcoe, how ar you!!!!!')
# # print(text.detect_language())
# # print(text.translate(to='fr'))
# print(text.correct())
# image = ('.jpg')
# from PIL import Image
# img = Image.open(r'C:\Users\20035128\Downloads\156.jpg')
# img.save('156.png')
# dict_ext = {
#     'image' : ('.JPG','.png'),
#     'docs' : ('.pdf','.txt')
# }
    
# folder = input('enter folder path: ')

# def filefinder(folderpath, fileext):
#     files = []
#     for i in os.listdir(folderpath):
#         for ext in fileext:
#             if i.endswith(ext):
#                 files.append(i)
#     return(files)

# # print(filefinder(folder,docs))

# for exten_type, extn_tuple in dict_ext.items():
#     foldername = exten_type + 'Files'
#     folder_path = os.path.join(folder, foldername)
#     os.mkdir(folder_path)
#     for item in filefinder(folder,extn_tuple):
#         item_path= os.path.join(folder,item)
#         item_path2= os.path.join(folder_path,item)
#         shutil.move(item_path,item_path2)
#     # print(filefinder(folder,extn_tuple))

#                           GUI APPLICATION
# import tkinter as tk
# from tkinter import ttk
# from csv import DictWriter
# import os
# win = tk.Tk()
# # title change
# win.title('Hello, world')
# # create labels
# name_label = ttk.Label(win, text='enter your name :  ')
# name_label.grid(row=0 , column =0,sticky=tk.W)

# age_label = ttk.Label(win, text='enter your age : ').grid(row=1 , column =0,sticky=tk.W)

# mail_label = ttk.Label(win, text='enter your email : ').grid(row=2 , column =0,sticky=tk.W)

# select_gender = ttk.Label(win, text='select your gender : ').grid(row=3 , column =0,sticky=tk.W)

# # input for labels/ entry box
# name_var = tk.StringVar()
# name_entry = ttk.Entry(win, width=15, textvariable= name_var)
# name_entry.grid(row=0,column=1)
# name_entry.focus()

# mail_var = tk.StringVar()
# mail_entry = ttk.Entry(win, width=15, textvariable= mail_var)
# mail_entry.grid(row=2,column=1)

# age_var = tk.StringVar()
# age_entry = ttk.Entry(win, width=15, textvariable= age_var)
# age_entry.grid(row=1,column=1)

# # create combobox
# gendervar = tk.StringVar()
# gender_cbox = ttk.Combobox(win, width = 15,textvariable= gendervar, state='readonly')
# gender_cbox['values'] = ('Male','Female','other')
# gender_cbox.current(0)
# gender_cbox.grid(row=3,column=1)

# # radio button
# usertype = tk.StringVar()
# rbtn = ttk.Radiobutton(win, text='student', value='student', variable = usertype)
# rbtn.grid(row=4,column=0)

# rbtn = ttk.Radiobutton(win, text='teacher', value='teacher', variable = usertype)
# rbtn.grid(row=4,column=1)
# # chechbutton
# checkbtn = tk.IntVar()
# ckhbtn = ttk.Checkbutton(win, text="abc", variable = checkbtn)
# ckhbtn.grid(row = 5, columnspan=1)

# # create button
# def action():
#     username = name_var.get()
#     userage= age_var.get()
#     usermail = mail_var.get()
#     gender = gendervar.get()
#     typeuser = usertype.get()
#     cbtn = checkbtn.get()
#     # print(f'{username} {userage} {usermail} and {gender}, {typeuser}, {cbtn}\n')

#     # with open('text.txt','a') as f:
#     #     f.write(f'{username},{userage},{usermail},{gender},{typeuser},{cbtn}\n')

#     with open('csv.csv', 'a', newline= '') as f:
#         csv = DictWriter(f,fieldnames=['Username','User email','User Age', 'user gender','user type','subscribed'])
#         if os.stat('csv.csv').st_size ==0:
#             csv.writeheader()

#         csv.writerows([
#             {'Username':username,'User email': usermail,'User Age': userage,'user gender': gender,'user type': typeuser,'subscribed': cbtn}
#         ])
#     name_entry.delete(0,tk.END)
#     mail_entry.delete(0,tk.END)
#     age_entry.delete(0, tk.END) 
#     name_label.configure(foreground="blue")


# button = ttk.Button(win, text='Submit',command =action).grid(row=6,column=0)

# win.mainloop()
# ?                                       END
# Loops in Tkinter
# import tkinter as tk
# from tkinter import ttk
# import os
# from csv import DictWriter

# win = tk.Tk()
# win.title("GUI")

# label_main = ['Name','Age','Country','City','Gender']
# for i in range(len(label_main)):
#     labels = 'label' + str(i)
#     labels = ttk.Label(win, text = label_main[i])
#     labels.grid(row = i, column=0, sticky =tk.W, padx=4,pady=4) 

# # name_var = tk.StringVar()
# user_info = {
#     'name':tk.StringVar(),
#     'age':tk.StringVar(),
#     'country':tk.StringVar(),
#     'city':tk.StringVar(),
#     'gender':tk.StringVar()
# }
# count = 0
# for i in user_info:
#     entry_box = 'entry' + i
#     entry_box = ttk.Entry(win, width =15, textvariable=user_info[i])
#     entry_box.grid(row=count,column=1)
#     count +=1
# def action():
#     print(user_info['name'].get())
#     print(user_info['age'].get())
#     print(user_info['country'].get())
#     print(user_info['city'].get())
#     print(user_info['gender'].get())

# submit_button = tk.Button(win, text='Submit', command=action)
# submit_button.grid(row= 5,column=1)    
# win.mainloop()

#  label frame

# win = tk.Tk()
# win.title('Label Frame')
# label_frame = tk.LabelFrame(win, text='Enter your details :')
# label_frame.grid(row=0,column=0,padx=100,pady=50)

# label_main = ['Name','Age','Country','City','Gender']
# for i in range(len(label_main)):
#     labels = 'label' + str(i)
#     labels = ttk.Label(label_frame, text = label_main[i])
#     labels.grid(row = i, column=0, sticky =tk.W, padx=4,pady=4) 
# user_info = {
#     'name':tk.StringVar(),
#     'age':tk.StringVar(),
#     'country':tk.StringVar(),
#     'city':tk.StringVar(),
#     'gender':tk.StringVar()
# }
# count = 0
# for i in user_info:
#     entry_box = 'entry' + i
#     entry_box = ttk.Entry(label_frame, width =15, textvariable=user_info[i])
#     entry_box.grid(row=count,column=1)
#     count +=1

# def action():
#     print(user_info['name'].get())
#     print(user_info['age'].get())
#     print(user_info['country'].get())
#     print(user_info['city'].get())
#     print(user_info['gender'].get())

# submit_button = tk.Button(win, text='Submit', command=action)
# submit_button.grid(row= 1,column=0)    
# win.mainloop()

# notebook/tabbed controlled widget
# win = tk.Tk()
# win.title('TAB control')
# nb =ttk.Notebook(win)
# page1 =ttk.Frame(nb)
# page2 =ttk.Frame(nb)
# nb.add(page1,text="ONE")
# nb.add(page2,text="TWO")
# nb.pack(expand=True, fill='both')

# label1= ttk.Label(page1, text='this is label :')
# label1.grid(row=0,column=0)
# entry1 = ttk.Entry(page1, width=15)
# entry1.grid(row=0,column=1)

# label2= ttk.Label(page2, text='Enter your name nd age :')
# label2.grid(row=0,column=0)
# entry2 = ttk.Entry(page2, width=15)
# entry2.grid(row=0,column=1)
# win.mainloop()

# menubar
# import pandas as pd
# import openpyxl
# from openpyxl import Workbook
# import xlwt
# import xlrd
# from xlutils.copy import copy
# import xlsxwriter
# customers = [13,14,15,16,17,20,31,100125,28,27]
# df = pd.read_excel(open("SALE DETAIL.xlsx", "rb"), sheet_name="SEPTEMBER",index_col=None, header=  None)
# tarik = input("please enter the date(dd-mm-yyyy) : ")
# sum_list = []
# count_list =[]
# for i in customers:
#     ab = df[df[2] == i]
#     a= (ab[ab[6]== tarik][8]).sum()
#     b= (ab[ab[6]== tarik][8]).count()
#     sum_list.append(round(a,2))
#     count_list.append(b)

# df1 = pd.DataFrame({
#     'count' : count_list,
#     'sum' : sum_list
# })
# with pd.ExcelWriter('output.xlsx', mode = 'a',engine="openpyxl") as writer:
#     df1.to_excel(writer, sheet_name='sheet1', index=False, startcol= 5, startrow=1)
#     writer.save()

# # rb = xlrd.open_workbook('output.xlsx')
# wb = copy(rb)
# w_sheet = wb.get_sheet(0)
# w_sheet.write(4,2,"hello")
# wb.save('output.xlsx')

   

# path='SALE DETAIL.xlsx'
# df = pd.read_excel(path)
# print(df[['Customer Name','QTY', 'AMOUNT']].head())   # particular column selection
# print(df.shape)
# print(df.iloc[1:3])    # particular row selection------- iloc method
# print(df.iloc[5,8])     # particular cell selection------- iloc[row,column]
# print(df.iloc[5:10,8]) 

# df = pd.read_excel('SALE DETAIL.xlsx')
# print(df[2])
# import os
# a =os.getcwd()
# print(a)
# b = r'\\10.9.32.2\adm'
# os.chdir(b
# combi = [[0,0],[1,0],[2,0],[3,0]]
# # print(combi[0,0])
# for i in combi:
#     print(i[0],i[1],i[0],i[1]+1)
    # print(f'self.treeWidget.topLevelItem({i[0]}).setText({i[1]}, _translate')
    # print(i[0])
    # print(i[1])   
# combi = [[0,0,0,1],[1,0,1,1],[2,0,2,1]]
# for i in combi:
#     print(i[0],i[1],i[2],i[3])iport



# import sys
# from PyQt5 import QtWidgets
# import pandas as pd
# sum_list= []
# customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
# customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
# customers2_length = range(0,len(customers2))
# tarik = input('enter data')
# df = pd.read_excel(open(r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\SALE DETAIL SHEET OCTOBER 2019.xlsx',"rb"), index_col=None, header=  None)
# for (i,j) in zip(customers1, customers2_length):
#     ab = df[df[2] == i]
#     a= (ab[ab[6]== tarik][8]).sum()
#     b = round(a,2)
#     i = customers2[j]
#     sum_list.append([i, str(b)])

# app = QtWidgets.QApplication(sys.argv)
# win = QtWidgets.QWidget()
# layout =QtWidgets.QVBoxLayout(win)
# # data1= [['asian', '183.51'], ['asian fine', '671.36'], ['utcl roorkee', '495.81'], ['utcl bagheri', '296.82'], ['utcl panipat', '0'], ['amnuja nalagargh', '0']]
# t = QtWidgets.QTreeWidget()
# t.setHeaderLabels(['Customers','Sales (MT)'])
# t.setAlternatingRowColors(True)
# for i in sum_list:
#     if i[1] != '0' :
#         cg =QtWidgets.QTreeWidgetItem(t,i)
# # cg1 =QtWidgets.QTreeWidgetItem(t,['abcd','xyzq'])

# layout.addWidget(t)
# win.show()
# sys.exit(app.exec_())


# sum_list= []
#         # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
# path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\SALE DETAIL SHEET OCTOBER 2019.xlsx'
#         # abc = os.path.join(path, userpath+'.xlsx')
# customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
# customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
# customers2_length = range(0,len(customers2))
# df = pd.read_excel(open(path,"rb"), index_col=None, header=  None)
# tarik = '19-10-2019'
# for (i,j) in zip(customers1, customers2_length):
#     ab = df[df[2] == i]
#     a= (ab[ab[6]== tarik][8]).sum()
#     b = round(a,2)
#     # print(a)
#     i = customers2[j]
#     sum_list.append([i, b])
# print(sum_list)    

# customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
#     customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
#     customers2_length = range(0,len(customers2))
# df = pd.read_excel(open(path,"rb"), index_col=None, header=  None)
# for (i,j) in zip(customers1, customers2_length):
#     ab = df[df[2] == i]
#     a= (ab[ab[6]== tarik][8]).count()
#     b = round(a,2)
#     # print(b)
# x =(df[df[2] == 20])    
# y = (x[x[6] == '20-10-2019']).sum()
# print(y)

# from datetime import date
# today = date.today()
# d1 = today.strftime("%d-%m-%Y")
# print(d1)


# x = datetime.datetime.now()
# path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
# a = x.strftime("%B")
# # path1 = input('enter path : ')
# userpath = f'SALE DETAIL SHEET {a.upper()} 2019'
# abc = os.path.join(path, userpath+'.xlsx')
# print(abc)
# if userpath =='' :
#     print(f'SALE DETAIL SHEET {a.upper()} 2019')
# else:  
#     print(userpath)
# today = date.today()
# d1 = today.strftime("%d-%m-%Y")   
# print(d1)

# import os.path  
# a = (r"C:\Users\20035128\OneDrive - Larsen & Toubro\icons&pics\truck.png")
# b = os.path.relpath('C:\\Windows', 'C:\\')
# # print(r'.\')
# a =os.path.join("Ash_solution","truck.png")
# # print(a)
# import datetime
# x = datetime.datetime.now()
# print(x.strftime('%x %X'))
# import pymysql
# import pandas as pd


# con=pymysql.connect(host='localhost',user='root',password='',database='vms')
# cur=con.cursor()
# cur.execute('select * from vehicle' )
# rows=cur.fetchall()
# df= pd.DataFrame(rows)
# group =df.groupby(3)
# # print(df.describe())
# print(group.get_group('Ash'))
# for i,j in group:
#     print(i)
#     # print(j)
# import pyqrcode
# from pyqrcode import QRCode
# from qrtools import QR


# s = "hey how r u"
  
# # Generate QR code 
# url = pyqrcode.create(s) 
  
# # Create and save the png file naming "myqr.png" 
# a=url.svg("qr.svg", scale = 8) 


# my_QR = QR(filename = "qr.svg") 
  
# # decodes the QR code and returns True if successful 
# my_QR.decode() 
  
# prints the data 
# print(my_QR.data)

# from bokeh.plotting import figure,output_file,show
# import pandas as pd
# import pymysql
# # from tkinter import filedialog
# # from tkinter import *

# # var_search_entrybox= '24-11-2019'
# con=pymysql.connect(host='localhost',user='root',password='',database='vms')
# cur=con.cursor()
# cur.execute("select username from user_login where username LIkE 'love'")# + str(username.get()))
# # print("select * from vehicle where entry like '%" + str(var_search_entrybox)+ "%'")
# rows=cur.fetchall()
# for i in rows:
#     print(rows)
# # df= pd.DataFrame(rows)

# # # print(df)
# # # for i,j in rows:
# # #     print(i)
# # #     print(j)
# # root = Tk()
# # root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = ((".xlsx","*xlsx"),("all files","*.*")))
# # # print (root.filename)
# writer = pd.ExcelWriter(str(root.filename)+".xlsx",engine='xlsxwriter')
# x= df.to_excel(writer,sheet_name='Sheet1',index=FALSE)

# writer.save()

# ########################
# from tkinter import *

# root = Tk() # Create Tk before you can create an image

# img = PhotoImage(file='npl.png')
# w, h = img.width(), img.height()   

# canvas = Canvas(root, width=w, height=h, bg='blue', highlightthickness=0)
# canvas.pack(expand = YES, fill = BOTH)
# canvas.create_image(0, 0, image=img, anchor=NW)

# root.mainloop()


###########################################
# import datetime
# import tkinter as tk

# def round_time(dt, round_to):
#     seconds = (dt - dt.min).seconds
#     rounding = (seconds + round_to / 2) // round_to * round_to
#     return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)


# def ct():
#     def count():
#         now = round_time(datetime.datetime.now(), round_to=1)
#         eh = datetime.datetime(2019, 3, 31, 20, 30)
#         tte = eh - now
#         canvas.itemconfig(label_cd, text=str(tte))
#         root.after(50, count)

#     count()

# root = tk.Tk()
# root.title("Earth Hour Countdown!")
# now = round_time(datetime.datetime.now(), round_to=1)
# eh = datetime.datetime(2019, 3, 31, 20, 30)
# tte = eh - now

# canvas = tk.Canvas(root, height=1350, width=1500,highlightthickness=0)
# canvas.pack()
# textentry = tk.Entry(canvas)
# canvas.create_window(600, 500, window=textentry, height=30, width=100)

# bg_img = tk.PhotoImage(file="new.png")
# bg_label = canvas.create_image((0,0), image=bg_img, anchor=tk.N+tk.W)

# label_msg = canvas.create_text((410, 120), text="Earth Hour Countdown:", font="MSGothic 50 bold", fill="#652828")

# label_cd = canvas.create_text((1030,120), text=str(tte), font="MSGothic 50 bold", fill="#652828")

# ehtime_label = canvas.create_text((650,240), text=("Earth Hour:" + eh.strftime("%d-%m-%Y %H:%M:%S")), font="MSGothic 50 bold", fill="#652828")

# ct()

# root.mainloop()

# from PyQt5 import QtWidgets, uic
# from PyQt5.QtWidgets import *

# app = QtWidgets.QApplication([])
# dlg= uic.loadUi(r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\ui files\DPR_final.ui')

# dlg.show()
# app.exec()
# import time
# def project():
#     print("hello")
    

# while True:
#     project()    
# #     time.sleep(5)
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
# # # import dryspace
# from bs4 import BeautifulSoup
# import requests
# # source = urllib.request.urlopen('http://www.punjabsldc.org/realtimepbGen.aspx').read()
# # soup = BeautifulSoup(source,'lxml')
# # table = soup.table
# # table_rows = table.find_all('tr')
# # for tr in table_rows:
# #     td = tr.find_all('td')
# #     row = [i.text for i in td]
# #     print(row)
# # class Client(QWebPage):

# #     def __init__(self, url):
# #         self.app = QApplication(sys.argv)
# #         QWebPage.__init__(self)
# #         self.loadFinished.connect(self.on_page_load)
# #         self.mainFrame().load(QUrl(url))
# #         self.app.exec_()
        
# #     def on_page_load(self):
# #         self.app.quit()    
# # url = 'http://www.punjabsldc.org/realtimepbGen.aspx'
# # client_response = Client(url)
# # source = client_response.mainFrame().toHtml()
# # soup = bs.BeautifulSoup(source, 'lxml')
# # ippRajpura1 = soup.find(id="ippRajpura1")
# # print(ippRajpura1.text)        
# # # content = urllib2.urlopen(url).read()

# # # soup = BeautifulSoup(content)
# # # soup = BeautifulSoup(url, 'html.parser')
# # # for div in soup.find_all(id='ippRajpura1'):
# # #     print(div.get_text())
# #     # print(str(paragraph.text))
# # # print(soup.p)
# # from selenium import webdriver
# url ='http://www.punjabsldc.org/realtimepbGen.aspx'
# req = requests.get(url)
# # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # driver = webdriver.Chrome(ChromeDriverManager().install())
# # # # driver = webdriver.Chrome()#('/path/to/chromedriver')
# # # # driver.get('http://www.punjabsldc.org/realtimepbGen.aspx')
# # # # print(req.text)
# # # # print(dir(req))
# soup = BeautifulSoup(req.text,'html.parser')
# x=soup.findAll('div',{'id':'ippRajpura1'})
# print(x)
# # # for i in x:
# #     # print(i.text)
# # # print(x)
# # # print(soup.prettify())
# # import dryscrape

# # sess = dryscrape.Session()
# # sess.visit('http://www.punjabsldc.org/realtimepbGen.aspx')
# # source = sess.body()

# # soup = bs.BeautifulSoup(source,'html.parser')
# # js_test = soup.find('div', id="ippRajpura1")
# # print(js_test.text)
# import pandas as pd
# import datetime
# from datetime import date
# import time

# def sms_total(cust_code):
#     x = datetime.datetime.now()
#     month = x.strftime("%B")
#     path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet\SALE DETAIL SHEET JANUARY 2020.xlsx'
#     today = date.today()
#     d1 = today.strftime("%d-%m-%Y")
#     tarik = d1 
#     df = pd.read_excel(open(path,"rb"),sheet_name= month.upper(), index_col=None, header=  None)
#     acc = df[df[2] == cust_code]
#     a = acc[acc[6]== tarik][8].sum()
#     return round(a,2)

    # print(round(a,2))
# print(date.today())
# x =(sms_total(20))                 
# print(x)
# # asian31 = sms_total(31)
# # asian20 = sms_total(20)
# # asian= asian20+asian31
# # acc = sms_total(100125)
# # ambuja =[13,14,15,16,37]
# # all_ambuja =[]
# # total_ambuja = sum(all_ambuja)
# # for i in ambuja:
# #     x = sms_total(i)
# #     total_ambuja.append(x)  
# # ult17 = sms_total(17)
# # ult18 = sms_total(18)
# # ult27 = sms_total(27)
# # ult28 = sms_total(28)
# # ultratech = ult17+ult18+ult27+ult28
# def sum_all(li):
#     all1 = []
#     for i in li:
#         x = sms_total(i)
#         all1.append(x)
#     return sum(all1)
# li = [[20,31],[17,18,27,28],[13,14,15,16,37],[100125]]
# cust= []
# for i in li:
#     cust.append(sum_all(i))        
# print(cust)
# from time import sleep
# def sum1(li):
#     a = sum(li)
#     print(a)
    
# li = [1,2,3,4]
# a = sum1(li)


# while True:
# #     a
# #     sleep(5)
       
# # from bs4 import BeautifulSoup
# # import requests
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # driver = webdriver.Chrome()
# # driver.get("http://www.punjabsldc.org/realtimepbGen.aspx")
# # element = driver.find_elements_by_css_selector("td[class='table'] div") 
# # for i in element: 
# #     print(i.text)
# # driver.close()

# import MySQLdb

# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="root",         # your username
#                      passwd="",  # your password
#                      db="djnago_test")

# cur = db.cursor()

# # Use all the SQL you like
# cur.execute("SELECT * FROM dashboard_sale_detail")

# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print(row[0])
#     print(row[1])
#     print(row[2])
#     print(row[3])

# db.close()   

# import pandas as pd
# import xlwings
# import os.path
# import datetime
# from datetime import date

# app = xlwings.App(visible=False)
# wb = app.books.open(r'\\10.9.32.2\adm\Ash\FY 2019-20\DAILY REPORT\DAILY REPORT FORMAT.xlsx')
# ws = wb.sheets['advance tracking sheet']
# l1 = []
# l2= []
# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="root",         # your username
#                      passwd="",  # your password
#                      db="djnago_test")

# cur = db.cursor()
# cur.execute("SELECT * FROM dashboard_sale_detail")
# for row in cur.fetchall():
#     l1.append(row[2])
#     l2.append(row[3])

# print(l1)
# print(l2)
# # l1 = ['C191', 'C192', 'C193', 'C195', 'C196', 'C199', 'C204', 'C208', 'C209', 'C210','C212', 'C213', 'C215', 'C216', 'C217', 'C218', 'C219', 'C220', 'C221', 'C222', 'C223', 'C224', 'C225']
# # l2 = ['J191', 'J192', 'J193', 'J195', 'J196', 'J199', 'J204', 'J208', 'J209', 'J210','J212', 'J213', 'J215', 'J216', 'J217', 'J218', 'J219', 'J220', 'J221', 'J222', 'J223', 'J224', 'J225']

# # dict1= {
# # 'C191' : 'J191',
# # 'C192' : 'J192',
# # 'C193' : 'J193',
# # 'C195' : 'J195',
# # 'C196' : 'J196',
# # 'C199' : 'J199',
# # 'C204' : 'J204',
# # 'C208' : 'J208',
# # 'C209' : 'J209',
# # 'C210' : 'J210',
# # 'C212' : 'J212',
# # 'C213' : 'J213',
# # 'C215' : 'J215',
# # 'C216' : 'J216',
# # 'C217' : 'J217',
# # 'C218' : 'J218',
# # 'C219' : 'J219',
# # 'C220' : 'J220',
# # 'C221' : 'J221',
# # 'C222' : 'J222',
# # 'C223' : 'J223',
# # 'C224' : 'J224',
# # 'C225' : 'J225',
# # }
# yester_bal = []
# for i in l2:
#     b = ws.range(i). value
#     c = b
#     yester_bal.append(c)  
# today = date.today()
# d1 = today.strftime("%d-%m-%Y")
# x = datetime.datetime.now()
# month = x.strftime("%B")
# path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
# # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
# userpath = f'SALE DETAIL SHEET {month.upper()} 2020' 
# abc = os.path.join(path, userpath+'.xlsx')
# df = pd.read_excel(open(abc,"rb"),sheet_name= month.upper(), index_col=None, header=  None)
# tarik = d1
# customers = [100051,100070,100071,100062,100072,100087,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165,100180]
# today_sale = []
# for i in customers:
#     ab = df[df[2] == i]
#     amount = (ab[ab[6]== tarik][19]).sum()
#     today_sale.append(amount)
# net_bal = []   
# for (i, j) in zip(yester_bal,today_sale):
#     final = round(i - j)
#             # x = babel.numbers.format_currency(( final ), "INR")
#     net_bal.append(final)
        
# cust_name =[]
# for i in l1:
#     b = ws.range(i). value
#     cust_name.append(b)
# bal= list(zip(cust_name, net_bal))
# print(bal)
import MySQLdb
# customers1 = []
# customers2 = []

# def connect_sql():
#     db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                 user="root",         # your username
#                 passwd="",  # your password
#                 db="djnago_test")
#     cur = db.cursor()

#     # cur.execute("SELECT * FROM dashboard_sale1")
#     # cursor = cur.execute(query)
#     return cur
# cur = connect()
# cur.execute("SELECT * FROM dashboard_dprCumulative_cellLocation")  
# for row in cur.fetchall():
#     customers1.append(row[2])
#     customers2.append(row[3]) 
# print(customers1)   
# print(customers2)  
# print(customers2[1])   

# for i,j in zip(customers1,customers2):
#     print(i)
#     print(j)
# ###******************************************* SLDC SCRAPING ***********************************
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# # import time

# options = Options()
# options.headless = True
# driver = webdriver.Chrome(chrome_options=options)
# driver.get("https://mapp.ntpc.co.in/masha/#/utilisation")
# # power_plant = ["ippRajpura1","ippRajpura2","ippTS1","ippTS2","ippTS3","ippGVK1","ippGVK2","GGSSTP3","GGSSTP4","GGSSTP5","GGSSTP6","GHTP1","GHTP2","GHTP3","GHTP4"]
# # element = driver.find_elements_by_class_name('//*[@id="col-xs-4"]')
# element = driver.find_elements_by_xpath('//*[@id="dtlChart"]/div[4]/div[2]')
# # for x in element:
# print(element)
# driver.close()
# options = Options()           //*[@id="dtlChart"]/div[8]/div[2] /html/body/ion-nav-view/ion-view[2]/ion-content/div[1]/div[1]/div/div/div/div/div/div[2]/div[3]/div[8]/div[2]
# options = Options() //*[@id="dtlChart"]/div[4]/div[2]
# options.headless = True //*[@id="dtlChart"]/div[6]
# driver = webdriver.Chrome(chrome_options=options)  <div class="col-xs-4 text-left ng-binding">24.988 <!-- ngIf: detail.flyAshUtilization != 0 --><span ng-if="detail.flyAshUtilization != 0">(LMT)</span><!-- end ngIf: detail.flyAshUtilization != 0 --></div>
# driver.get("http://www.punjabsldc.org/realtimepbGen.aspx")
# time.sleep(5)
# power_plant = ["ippRajpura1","ippRajpura2","ippTS1","ippTS2","ippTS3","ippGVK1","ippGVK2","GGSSTP3","GGSSTP4","GGSSTP5","GGSSTP6","GHTP1","GHTP2","GHTP3","GHTP4"]
# for i in power_plant:
#     # print(f'\"{i}\"')
#     element = driver.find_element_by_xpath(f'//*[@id=\"{i}\"]')
#     print(element.text)
# driver.close()
# def load():
#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(chrome_options=options)
#     driver.get("http://www.punjabsldc.org/realtimepbGen.aspx")
#     time.sleep(5)
#     mw =[]
#     power_plant = ["ippRajpura1","ippRajpura2","ippTS1","ippTS2","ippTS3","ippGVK1","ippGVK2","GGSSTP3","GGSSTP4","GGSSTP5","GGSSTP6","GHTP1","GHTP2","GHTP3","GHTP4"]
#     for i in power_plant:
#         # print(f'\"{i}\"')
#         element = driver.find_element_by_xpath(f'//*[@id=\"{i}\"]')
#         mw.append(element.text)
#     driver.close()
#     return mw
# x = load()

# #*******************************************************************************************
# def connect_sql():
#     connection = MySQLdb.connect(host="localhost",user="root",passwd="",db="djnago_test")
#     cur = connection.cursor()
#     return cur,connection
# customers1 = [] 
# loc = []  
# cur,conn = connect_sql()
# cur.execute("SELECT * FROM dashboard_dpr_cust_code")
# for row in cur.fetchall():
#     customers1.append(int(row[1]))
# print(customers1) 
# cur.execute("SELECT * FROM dashboard_dprexcel_celllocation")
# for row in cur.fetchall():
#     loc.append(row)
# print(loc)
############                           FOC percentage                    ###############################################
# import pandas as pd 
# path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet\SALE DETAIL SHEET JANUARY 2020.xlsx'
# df = pd.read_excel(open(path,"rb"),sheet_name= 'JANUARY', index_col=None, header=  None,skiprows=1)
# l = 0.00
# total= df[df[9]== l][8].sum()
# total1 = df[8].sum()
# per = total*100/total1
# print(round(total,2))
# print(total1)
# print(per)
######################          ASH ulitilaztion %   ###########################################

# import xlwings
# app = xlwings.App(visible=False)
# wb = app.books.open(r'\\10.9.32.2\adm\Ash\FY 2019-20\Quantity details\MONTHWISE DETAILS 2019-20.xlsx') 
# wb.Interactive = False
# ws = wb.sheets['Summary']
# a = ws.range("N21").value
# b= round(a*100)
# wb.close()
# print(f'{b}%')
# ********************************************************************************
from datetime import date, timedelta
import time

def check():
    today = date.today()
    print(today)
    time.sleep(3)
    check()

check()    
# print(x)
# #******************************************************************************
# import pandas as pd 
# from babel.numbers import format_currency
# # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet\SALE DETAIL SHEET JANUARY 2020.xlsx'
# # df = pd.read_excel(open(path,"rb"),sheet_name= 'JANUARY', index_col=None, header=  None,skiprows=1)
# # amount = df[10].sum()
# # handling = df[15].sum()
# # total = amount+handling
# x = format_currency(90.0, 'INR', format=u'#,##0\xa0¤',currency_digits=False,locale='en_IN')
# print(x)
# import datetime
# print((datetime.datetime.now()))

# from requests_html import HTMLSession
# session = HTMLSession()

# r = session.get('http://www.punjabsldc.org/realtimepbGen.aspx')
# x = r.html.xpath('//*[@id=\"ippRajpura1"]')
# # x = r.html.find('.table',first=True)
# print((x.get('content')))

# from lxml import html
# import requests
# url = 'http://www.punjabsldc.org/realtimepbGen.aspx'
# page = requests.get(url)
# tree = html.fromstring(page.content)
# x = tree.xpath('//*[@id=\"ippRajpura1"]')[0]
# print((x.get('content')))

# import pandas as pd
# import os
# import datetime

# date_time = datetime.datetime.now()
# year = date_time.year
# month = date_time.strftime("%B")
# today = date_time.strftime("%d-%m-%Y")
# # # print(today)
# def detailsheet():
#     path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
#     sheet = f'SALE DETAIL SHEET {month.upper()} {year}'
#     full_path = os.path.join(path, sheet+'.xlsx')
#     df = pd.read_excel(open(full_path,'rb'),sheet_name= month.upper() ,index_col=None, header=  None)
#     # print(df.head())
#     return df

# # df = detailsheet()
# # print(df.head())
   
# def dpr_sale(customer_list):
#     sum_list = []
#     count_list =[]
#     df = detailsheet()
#     # print(df.head())
#     for i in customer_list:
#         ab = df[df[2] == i]
#         a= (ab[ab[6]== x][8]).sum()
#         # print(a)
#         b= (ab[ab[6]== x][8]).count()
#         sum_list.append(round(a,2))
#         count_list.append(b)
#     return count_list,sum_list

# count_list,sum_list = dpr_sale(customers1)  
# # print(count_list) 
# print(sum_list) 

# def connect_sql():
#     connection = MySQLdb.connect(host="localhost",user="root",passwd="",db="djnago_test")
#     cur = connection.cursor()
#     return cur,connection

# customers1 = []              # Getting customer code from db                            
# customers2 = []              # Getting customer name from db 
# cur,conn = connect_sql()
# cur.execute("SELECT * FROM dashboard_sale1")
# for row in cur.fetchall():
#     customers1.append(int(row[1]))
#     customers2.append(row[2])    
# conn.close()
# # print(customers1)
# import matplotlib.pyplot as plt 
# count_list,sum_list = dpr_sale(customers1)
# x = customers1
# y = sum_list
# plt.plot(x,y)
# # naming the x axis 
# plt.xlabel('x - axis') 
# # naming the y axis 
# plt.ylabel('y - axis') 
  
# # giving a title to my graph 
# plt.title('My first graph!') 
# plt.show()
# # print(count_list)
# # print(sum_list)



# # ***********************************    Excel sheets path **************************
# daily_report = []
# sale_detail = []
# ash_utilization = []
# cur,conn = connect_sql()
# cur.execute("SELECT * FROM dashboard_excel_sheet_path")
# for row in cur.fetchall():
#     daily_report.append(row[1])
#     sale_detail.append(row[2])
#     ash_utilization.append(row[3])             

# path = sale_detail[0] 
# sheet = f'SALE DETAIL SHEET {month.upper()} {year}'
# full_path = os.path.join(path, sheet+'.xlsx')

# def detailsheet():
#     path = sale_detail[0]
#     sheet = f'SALE DETAIL SHEET {month.upper()} {year}'
#     full_path = os.path.join(path, sheet+'.xlsx')
#     df = pd.read_excel(open(full_path,'rb'),sheet_name= month.upper() ,index_col=None, header=  None)
#     return df

# df = detailsheet()
# print(df.head())

# for (i,j) in zip(customers1, customers2_length):
#     ab = df[df[2] == i]
#     bifurcated_month_total = round(ab[8].sum(),2) 
#     bifurcated_month_count = ab[8].count() 
#     a= (ab[ab[6]== today][8]).sum()
#     count1= (ab[ab[6]== today][8]).count()
#     b = round(a,2)
#     i = customers2[j]
#     if b != 0:
#         sum_list.append([i, str(b),count1])
#     if bifurcated_month_total !=0:
#         month_sum.append([i,str(bifurcated_month_total),bifurcated_month_count])
# total= df[df[6]== today][8].sum()
# month_total= df[8].sum()
# total_count= df[df[6]== today][8].count()
# month_count= df[8].count()
# if total !=0:
#     sum_list.append(["Total",str(round(total,2)),total_count])
# if month_total !=0:                 
#     month_sum.append(["Total",str(round(month_total,2)),month_count]) 

# def abc(day):
#     for (i,j) in zip(customers1, customers2_length):
#         ab = df[df[2] == i]
#         a= (ab[ab[6]== day][8]).sum()
#         count1= (ab[ab[6]== day][8]).count()
#         b = round(a,2)
#         i = customers2[j]
#         if b != 0:
#             sum_list.append([i, str(b),count1])



# yesterday = today - timedelta(days = 2)
# print(today.strftime('%d-%m-%Y'))
# print(yesterday.strftime('%d-%m-%Y'))
# print(today.strftime("%B"))
# print(today.strftime("%Y"))





# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# def sum1(a,b):
#     ''' this function adds two numbers'''
#     return a+b
# print(len(mytuple))
# print(len.__doc__)


# try:
#     with open(r'C:\Users\20035128\Desktop\New Text Document.txt','a') as f:
#         # print(f.write("hello bro"))
#         print(f.read())
# except IOError:
#     print("file not found")
import os
# import subprocess
# os.startfile("outlook")
# # subprocess.Popen("explorer")
# subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK")
# # os.system("text.txt")

# def outlook_is_running():
#     import win32ui
#     try:
#         win32ui.FindWindow(None, "Microsoft Outlook")
#         return True
#     except win32ui.error:
#         return False

# if not outlook_is_running():
#     import os
#     os.startfile("outlook")
# print(dir(os))