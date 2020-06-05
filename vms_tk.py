from tkinter import *
from tkinter import ttk
import pymysql
import datetime
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd


class bulker_entry:

    def __init__(self,root):
                
        self.root=root
        self.root.title('Vehicle Management System')
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap('yellow_icon.ico')
        self.root.configure(background='#65f075')

        title = Label(self.root, text='Vehicle Management System',bd =10,relief=GROOVE, font=('times new roman',40,'bold'),bg='#65f075',fg='#ed2434')
        title.pack(side=TOP, fill=X)
#==============================Variables========================================
        self.var_bulker=StringVar()
        self.var_mobile=StringVar()
        self.var_transporter=StringVar()
        self.var_driver=StringVar()
        self.var_material=StringVar()
        self.var_save_file=StringVar()

        self.var_search=StringVar()
        self.var_search_entrybox=StringVar()

     #-------------------Manage Frame--------------------------------------   

        manage_frame = Frame(self.root,bd=4,relief=RIDGE,bg='#e67c53')
        manage_frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(manage_frame,text='Vehicle Entry',bg='#e67c53',fg='white', font=('times new roman',25,'bold'))
        m_title.grid(row=0,columnspan=2,pady=20,padx=90)

        bulker_title=Label(manage_frame,text='Vehicle no.',bg='#e67c53',fg='white', font=('times new roman',20,'bold'))
        bulker_title.grid(row=1,column=0,pady=10,padx=15,sticky='w')

        bulker_text=Entry(manage_frame,textvariable=self.var_bulker,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        bulker_text.grid(row=1,column=1,pady=10,padx=15,sticky='w')

        tpt_title=Label(manage_frame,text='Transporter',bg='#e67c53',fg='white', font=('times new roman',20,'bold'))
        tpt_title.grid(row=2,column=0,pady=10,padx=15,sticky='w')

        tpt_text=Entry(manage_frame,textvariable=self.var_transporter,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        tpt_text.grid(row=2,column=1,pady=10,padx=15,sticky='w')

        driver_title=Label(manage_frame,text='Driver',bg='#e67c53',fg='white', font=('times new roman',20,'bold'))
        driver_title.grid(row=3,column=0,pady=10,padx=15,sticky='w')

        driver_text=Entry(manage_frame,textvariable=self.var_driver,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        driver_text.grid(row=3,column=1,pady=10,padx=15,sticky='w')

        mob_title=Label(manage_frame,text='Mobile no.',bg='#e67c53',fg='white', font=('times new roman',20,'bold'))
        mob_title.grid(row=4,column=0,pady=10,padx=15,sticky='w')

        mob_text=Entry(manage_frame,textvariable=self.var_mobile,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        mob_text.grid(row=4,column=1,pady=10,padx=15,sticky='w')

        mob_title=Label(manage_frame,text='Material',bg='#e67c53',fg='white', font=('times new roman',20,'bold'))
        mob_title.grid(row=5,column=0,pady=10,padx=15,sticky='w')

        mob_text=Entry(manage_frame,textvariable=self.var_material,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        mob_text.grid(row=5,column=1,pady=10,padx=15,sticky='w')

        # save_file_title=Label(manage_frame,text='Save File ',bg='#e67c53',fg='white', font=('times new roman',20,'bold'))
        # save_file_title.grid(row=6,column=0,pady=10,padx=15,sticky='w')

        # save_file_text=Entry(manage_frame,textvariable=self.var_save_file,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        # save_file_text.grid(row=6,column=1,pady=10,padx=15,sticky='w')

 #-------------------button Frame--------------------------------------        
        btn_frame = Frame(manage_frame,bd=4,relief=RIDGE,bg='#e67c53')
        btn_frame.place(x=15,y=500,width=415)

        addbtn= Button(btn_frame,text='Add Entry', width=10,command=self.add_veh).grid(row=0,column=0,padx=10,pady=10)
        updatebtn= Button(btn_frame,text='Exit Entry', width=10,command=self.update).grid(row=0,column=1,padx=10,pady=10)
        delbtn= Button(btn_frame,text='Delete', width=10,command=self.del_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn= Button(btn_frame,text='Clear', width=10,command = self.clear).grid(row=0,column=3,padx=10,pady=10)
        # save_file_btn = Button(manage_frame,text='Save File', width=15,command=self.save_file,font=('times new roman',18),bd=5,relief=GROOVE)
        # save_file_btn.grid(row=7,columnspan=2,padx=10,pady=10)


#-------------------Deatil Frame-------------------------------------- 
        detail_frame = Frame(self.root,bd=4,relief=RIDGE,bg='#e67c53')
        detail_frame.place(x=500,y=100,width=840,height=600)

        search_label=Label(detail_frame,text='Search by',bg='#e67c53',fg='white', font=('times new roman',20,'bold'))
        search_label.grid(row=0,column=0,pady=10,padx=15,sticky='w')
        search_combo=ttk.Combobox(detail_frame,textvariable=self.var_search,width=10,font=('times new roman',13,'bold'),state='readonly')
        search_combo['values']=('Token','Entry','Vehicle','Material','Transporter','Driver','Out_Entry')
        search_combo.grid(row=0,column=1,padx=20,pady=20)

        search_text=Entry(detail_frame,textvariable=self.var_search_entrybox,font=('times new roman',13,'bold'),bd=5,relief=GROOVE,width=10)
        search_text.grid(row=0,column=2,pady=10,padx=15,sticky='w')

        searchbtn= Button(detail_frame,text='Search', width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn= Button(detail_frame,text='Show All', width=10,command=self.showall_data).grid(row=0,column=5,padx=10,pady=10)
        save_file_btn= Button(detail_frame,text='Save as file', width=10,command=self.save_file).grid(row=0,column=6,padx=10,pady=10)
        refresh_btn= Button(detail_frame,text='Refresh', width=10,command=self.get_data).grid(row=0,column=4,padx=10,pady=10)

#=========================== Table frame====================
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='#e67c53')
        table_frame.place(x=20,y=70,width=790,height=500)

        scroll_x= Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= Scrollbar(table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(table_frame,columns=('Token','Entry','Vehicle','Material','Transporter','Driver','Out_Entry','Mobile'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        style = ttk.Style()
        style.configure("Treeview.Heading",font=('Comic Sans MS', 13),foreground="red")

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.vehicle_table.xview)
        scroll_y.config(command=self.vehicle_table.yview)
        self.vehicle_table.heading('Token',text='Token')
        self.vehicle_table.heading('Entry',text='Entry')
        self.vehicle_table.heading('Vehicle',text='Vehicle')
        self.vehicle_table.heading('Material',text='Material')
        self.vehicle_table.heading('Transporter',text='Transporter')
        self.vehicle_table.heading('Driver',text='Driver')
        self.vehicle_table.heading('Out_Entry',text='Out_Entry')
        self.vehicle_table.heading('Mobile',text='Mobile')
        self.vehicle_table['show']='headings'
        self.vehicle_table.column('Token',width=60)
        self.vehicle_table.column('Entry',width=110)
        self.vehicle_table.column('Vehicle',width=90)
        self.vehicle_table.column('Material',width=80)
        self.vehicle_table.column('Transporter',width=110)
        self.vehicle_table.column('Driver',width=70)
        self.vehicle_table.column('Mobile',width=70)
        self.vehicle_table.column('Out_Entry',width=110)
        self.vehicle_table.pack(fill=BOTH,expand=1)
        self.vehicle_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.get_data()

    def add_veh(self):
        if self.var_bulker.get()=='' or self.var_driver.get()=='' or self.var_transporter.get()== '':
            messagebox.showerror("Error","All fields are mandatory!!!!")
        else:    
            x = datetime.datetime.now()
            date_time =x.strftime('%d-%m-%Y %X')
            connection=pymysql.connect(host='localhost',user='root',password='',database='vms')    
            cur=connection.cursor()
            query ='insert into vehicle(entry,vehicle,material,transporter,driver,mobile) values(%s,%s,%s,%s,%s,%s)'
            values = (date_time,self.var_bulker.get().upper(),self.var_material.get().title(),self.var_transporter.get().title(),self.var_driver.get().title(),self.var_mobile.get())
            cur.execute(query,values)
            connection.commit()
            self.get_data()
            self.clear()
            connection.close()
            messagebox.showinfo('Success',"Entry has been inserted")

    def get_data(self):
        x = datetime.datetime.now()
        date =x.strftime('%d-%m-%Y ')
        con=pymysql.connect(host='localhost',user='root',password='',database='vms')
        cur=con.cursor()
        cur.execute("select * from vehicle where entry LIKE '%" +str(date)+ "%'" + "OR out_entry LIKE '%" +str(date)+ "%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for row in rows:
                self.vehicle_table.insert('',END,values=row)
            con.commit()
            self.var_search_entrybox.set('') 
            self.var_search.set('')
        con.close()  

    def clear(self):
        self.var_mobile.set('')
        self.var_transporter.set('')
        self.var_bulker.set('')
        self.var_driver.set('')
        self.var_material.set('')

    def get_cursor(self,ev):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']
        self.var_mobile.set(row[7])
        self.var_transporter.set(row[4])
        self.var_bulker.set(row[2])
        self.var_driver.set(row[5])
        self.var_material.set(row[3])

    def update(self):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']
        x = datetime.datetime.now()
        date_time =x.strftime('%d-%m-%Y %X')
        connection=pymysql.connect(host='localhost',user='root',password='',database='vms')    
        cur=connection.cursor()
        cur.execute('update vehicle set out_entry=%s where token=%s ',(date_time,row[0]))
        connection.commit()
        self.get_data()
        self.clear()
        connection.close()        
    
    def del_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='vms')
        cur=con.cursor()
        cur.execute('delete from vehicle where vehicle =%s',self.var_bulker.get())
        con.commit()
        con.close()
        self.get_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='vms')
        cur=con.cursor()
        cur.execute("select * from vehicle where "+str(self.var_search.get())+ " LIKE '%" +str(self.var_search_entrybox.get()+ "%'"))
        rows=cur.fetchall()
        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for row in rows:
                self.vehicle_table.insert('',END,values=row)
            con.commit()
            # self.var_search_entrybox.set('')
        con.close()   

    def showall_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='vms')
        cur=con.cursor()
        cur.execute('select * from vehicle' )
        rows=cur.fetchall()
        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for row in rows:
                self.vehicle_table.insert('',END,values=row)
            con.commit()
        con.close()

    def save_file(self):
        root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = ((".xlsx","*xlsx"),("all files","*.*")))
        con=pymysql.connect(host='localhost',user='root',password='',database='vms')
        cur=con.cursor()
        cur.execute("select * from vehicle where "+str(self.var_search.get())+ " LIKE '%" +str(self.var_search_entrybox.get()+ "%'"))
        rows=cur.fetchall()
        df= pd.DataFrame(rows)
        writer = pd.ExcelWriter(str(root.filename)+".xlsx",engine='xlsxwriter')
        df.to_excel(writer,sheet_name='Sheet1',index=FALSE)
        writer.save()
        self.var_search_entrybox.set('') 
        self.var_search.set('')

root = Tk()
ob = bulker_entry(root)
root.mainloop()