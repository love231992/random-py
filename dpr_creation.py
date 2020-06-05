import tkinter as tk
from tkinter import ttk
import pandas as pd
import xlwings
from tkinter import messagebox as m_box
import tkinter.filedialog
import os.path
import time


win = tk.Tk()
win.title("Ash Solutions- NPL")

win.minsize(width=850, height=500)
# win.maxsize(width=850, height=500)
                                         # Frame 1 Starts
frame1 = ttk.Labelframe(win, text= "Daily Report")
frame1.grid(row=1,column=0, padx=20, sticky=tk.W)

# Frame1 Labels
label_date = ttk.Label(frame1, text = 'Enter the date (dd-mm-yyyy) : ')
label_date.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
label_date.configure(foreground='blue')
label_path = ttk.Label(frame1, text = 'Enter the sale detail sheet name : ')
label_path.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
label_path.configure(foreground='blue')
#Frame 1 EntryBox
date_var = tk.StringVar()
date_entrybox = ttk.Entry(frame1, width = 15, textvariable= date_var)
date_entrybox.grid(row=0, column=1,padx=5, pady=5)
date_entrybox.focus()
path_var = tk.StringVar()
path_entrybox = ttk.Entry(frame1, width = 20, textvariable= path_var)
path_entrybox.grid(row=1, column=1,padx=5, pady=5)
# Frame1 Button Command
def action():
    userdate = date_var.get()
    userpath = path_var.get()
    path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
    abc = os.path.join(path, userpath+'.xlsx') 
    if abc =='':
        m_box.showerror('ERROR','Please enter the file name!')  
    customers1 = [20,31,28,27,17,13,15,14,37,100125]
    customers2 = [100051,100062,100087,100071,100070]
    customers3 = [100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
    df = pd.read_excel(open(abc,"rb"), index_col=None, header=  None)
    tarik = userdate
    if tarik=='':
        m_box.showerror('ERROR','Please enter the date!')
#  program for sumifs and countifs for customers1 and appending data to Dpr
    
    sum_list1 = []
    count_list1 =[]
    for i in customers1:
        ab = df[df[2] == i]
        a= (ab[ab[6]== tarik][8]).sum()
        b= (ab[ab[6]== tarik][8]).count()
        sum_list1.append(round(a,2))
        count_list1.append(b)
    wb = xlwings.Book(r'\\10.9.32.2\adm\Ash\FY 2019-20\DAILY REPORT\DAILY REPORT FORMAT.xlsx')
    xlwings.App().visible=False
    ws = wb.sheets['DPR']
    ws.range('E7').options(transpose=True).value = count_list1
    ws.range('F7').options(transpose=True).value = sum_list1
    # print(sum_list1)
    # print(count_list1)
#  program for sumifs and countifs for customers2 and appending data to Dpr
    sum_list2 = []
    count_list2 =[]
    for i in customers2:
        ab = df[df[2] == i]
        a= (ab[ab[6]== tarik][8]).sum()
        b= (ab[ab[6]== tarik][8]).count()
        sum_list2.append(round(a,2))
        count_list2.append(b)

    ws.range('E18').options(transpose=True).value = count_list2
    ws.range('F18').options(transpose=True).value = sum_list2
    # print(sum_list2)
    # print(count_list2)
#  program for sumifs and countifs for customers3 and appending data to Dpr
    sum_list3 = []
    count_list3 =[]
    for i in customers3:
        ab = df[df[2] == i]
        a= (ab[ab[6]== tarik][8]).sum()
        b= (ab[ab[6]== tarik][8]).count()
        sum_list3.append(round(a,2))
        count_list3.append(b)

    ws.range('E24').options(transpose=True).value = count_list3
    ws.range('F24').options(transpose=True).value = sum_list3
    # print(sum_list3)
    # print(count_list3)

    dict1= {
        'F7' : 'E45',
        'F8' : 'E46',
        'F9' : 'E47',
        'F10' : 'E48',
        'F11' : 'E49',
        'F12': 'E50',
        'F13' : 'E51',
        'F14' : 'E52',
        'F15' : 'E53',
        'F16' : 'E54',
    
    }

    for i,j in dict1.items():
        num1 = 0
        num1_new = ws.range(i).value 
        num2 = ws.range(j).value 
        ws.range(j).value =(num2+(num1_new - num1))
    

    dict2= {
        'F18' : 'E56',
        'F19' : 'E57',
        'F20' : 'E59',
        'F21' : 'E60',
        'F22' : 'E61', 
    }

    for i,j in dict2.items():
        num1 = 0
        num1_new = ws.range(i).value 
        num2 = ws.range(j).value 
        ws.range(j).value =(num2+(num1_new - num1))
    

    dict3= {
        'F24' : 'E63',
        'F25' : 'E64',
        'F26' : 'E65',
        'F27' : 'E66',
        'F28' : 'E67',
        'F29':  'E68',
        'F30' : 'E70',
        'F31' : 'E71',
        'F32' : 'E72',
        'F33' : 'E73',
        'F34' : 'E74',
        'F35' : 'E75',
        'F36' : 'E76',
        'F37' : 'E77',
    
    }

    for i,j in dict3.items():
        num1 = 0
        num1_new = ws.range(i).value 
        num2 = ws.range(j).value 
        ws.range(j).value =(num2+(num1_new - num1))
    
        
        date_entrybox.delete(0, tk.END)
        path_entrybox.delete(0, tk.END)
    m_box.showinfo('Message','Report Successfully Created')
    wb.save()
    wb.close()

# Frame 1 Button
submit_button=tk.Button(frame1, text= 'Submit', fg="red", bg= 'pink' , command= action)
submit_button.grid(row=2, column=1,padx=5, pady=5)
                                                            # Frame 1 Ends
                                               # Frame 2 Starts

                                              
frame2 = ttk.Labelframe(win, text="Sale detail")
frame2.grid(row=1,column=1, padx=20,pady=20,sticky = tk.E)

# frame2 function


def clear():
    
    for row in listBox.get_children():
        listBox.delete(row)
def show():
    sum_list = []  
    userdate2 = date2_var.get()
    tarik = userdate2
    userpath = path2_var.get()
    if userdate2 == '' or userpath=='':
        m_box.showerror('ERROR','Please provide the required input first!')
       
    path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
    abc = os.path.join(path, userpath+'.xlsx')
    customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
    customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
    customers2_length = range(0,len(customers2))
    df = pd.read_excel(open(abc,"rb"), index_col=None, header=  None)
    for (i,j) in zip(customers1, customers2_length):
        ab = df[df[2] == i]
        a= (ab[ab[6]== tarik][8]).sum()
        b = round(a,2)
        i = customers2[j]
        sum_list.append([i, b])
    tempList = sum_list
    
    # tarik = 0
    # for customer, qty in tempList:
    #     if qty>0:
    #         listBox.insert("", "end", values=(customer , qty))
    
    for row in listBox.get_children():
        listBox.delete(row)

    # for (i,j) in zip(customers1, customers2_length):
    #     ab = df[df[2] == i]
    #     a= (ab[ab[6]== tarik][8]).sum()
    #     b = round(a,2)
    #     i = customers2[j]
    #     sum_list.append([i, b])
    # tempList = sum_list
    # tempList.sort(key=lambda e: e[1], reverse=True)
    # tarik = 0
    for customer, qty in tempList:
        if qty>0:
            listBox.insert("", "end", values=(customer , qty))
         


label = tk.Label(frame2, text="Sale detail ", font=("Arial",30))
label.grid(row=0, columnspan=3)
label.configure(foreground='blue')
label2_date = ttk.Label(frame2, text = 'Enter the date (dd-mm-yyyy) : ')
label2_date.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
label2_date.configure(foreground='blue')
date2_var = tk.StringVar()
date2_entrybox = ttk.Entry(frame2, width = 15, textvariable= date2_var)
date2_entrybox.grid(row=2, column=1,padx=5, pady=5, columnspan=2)
date2_entrybox.focus()

label2_path = ttk.Label(frame2, text = 'Enter the file path : ')
label2_path.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
label2_path.configure(foreground='blue')
path2_var = tk.StringVar()
path2_entrybox = ttk.Entry(frame2, width = 20, textvariable= path2_var)
path2_entrybox.grid(row=3, column=1,padx=5, pady=5)
# create Treeview with 2columns
cols = ( 'Customer', 'Quantity(MT)')
listBox = ttk.Treeview(frame2, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)


# Scroll bar 
vsb = ttk.Scrollbar(frame2,orient="vertical",command=listBox.yview)
vsb.grid(row=1, column=2, sticky='ns')
listBox.configure(yscrollcommand=vsb.set)

#Frame 2 Buttons
showScores = tk.Button(frame2, text="Show",fg="red", bg= 'pink', width=30, command=show).grid(row=4, column=0)
# closeButton = tk.Button(frame2, text="Close",fg="red", bg= 'pink', width=15, command=exit).grid(row=4, column=1,sticky=tk.W)
clearButton = tk.Button(frame2, text='Clear',fg="red", bg= 'pink', width=30,command=clear).grid(row=4,column=1)

# btn= tk.Button(frame2, text='Customer sale detail', command = abc)
# btn.grid(row=2, column=1,padx=5, pady=5)
win.mainloop()