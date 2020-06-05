from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import db1
import after_login

##############################################################################
class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        # self.root.geometry('1350x700+0+0')
        self.root.geometry('1900x870+0+0')

        self.bg_icon=PhotoImage(file='new.png')
        self.pass_icon=PhotoImage(file='password.png')
        self.user_icon=PhotoImage(file='user.png')
        self.login_icon=PhotoImage(file='login.png')

        self.username = StringVar()
        self.password = StringVar()

        bg_label=Label(self.root,image=self.bg_icon)
        bg_label.place(x=0,y=30)

        title=Label(self.root,text="Login System",font=('times new roman',40,'bold'),bg="crimson",fg='yellow',bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=100,y=150)

        login_label=Label(login_frame,image=self.login_icon,bd=0)
        login_label.grid(row=0,columnspan=2,pady=20)

        user_label=Label(login_frame,text="Username",image=self.user_icon,compound=LEFT,font=('times new roman',15,'bold'),bg='white')
        user_label.grid(row=1,column=0,padx=20,pady=10)

        user_entry=Entry(login_frame,bd=5,relief=GROOVE,textvariable=self.username,font=("",15)).grid(row=1,column=1,padx=20,pady=10)

        pass_label=Label(login_frame,text="Password",image=self.pass_icon,compound=LEFT,font=('times new roman',15,'bold'),bg='white')
        pass_label.grid(row=2,column=0,padx=20,pady=10)

        pass_entry=Entry(login_frame,bd=5,relief=GROOVE,show='*',textvariable=self.password,font=("",15)).grid(row=2,column=1,padx=20,pady=10)

        btn_login=Button(login_frame,text="Login",width=10,command=self.login,font=('times new roman',15,'bold'),bg='crimson',fg='yellow').grid(row=3,column=1,pady=10)
        btn_new_login=Button(login_frame,text="Register",width=10,command=self.register,font=('times new roman',15,'bold'),bg='crimson',fg='yellow').grid(row=3,column=0,pady=20)

    def login(self):
        data =( self.username.get(),
        self.password.get()
        )
        if self.username.get() == '' or self.password.get() == '' :
            messagebox.showwarning("Error", 'Both fields are mandatory')
        else :
            res= db1.login(data)
            if res:
                messagebox.showinfo("Message", "Login Succesfully")
                root.destroy()
                after_login.after_login()
            else:
                messagebox.showinfo("Alert", "wrong username or Password")

##################### New User Registration #########################################################################

    def register(self):
        self.register_screen = Toplevel(root)
        self.register_screen.title("Register")
        self.register_screen.geometry("500x300")
        username = StringVar()
        password = StringVar()
        title=Label(self.register_screen,text="Enter your details below for registration",font=('times new roman',20,'bold'),bg="crimson",fg='yellow',bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        

        user_label=Label(self.register_screen,text="Username",compound=LEFT,font=('times new roman',15,'bold'))
        user_label.place(x=80,y=130)

        user_entry=Entry(self.register_screen,textvariable=username,bd=5,relief=GROOVE,font=("",15))
        user_entry.place(x=220,y=130)

        pass_label=Label(self.register_screen,text="Password",compound=LEFT,font=('times new roman',15,'bold'))
        pass_label.place(x=80,y=180)

        pass_entry=Entry(self.register_screen,show='*',textvariable=password,bd=5,relief=GROOVE,font=("",15))
        pass_entry.place(x=220,y=180)     

        def create_user():
            if username.get()== '' or password.get()== '':
                messagebox.showwarning('Error','Both the fields are mandatory!!')
            else :
                connection=pymysql.connect(host='localhost',user='root',password='',database='vms')    
                cur=connection.cursor()
                if cur.execute('select username from user_login where username = %s',username.get()):
                    rows=cur.fetchall()
                    messagebox.showwarning('Warning',"Username already taken!!")
                else :    
                    query ='insert into user_login(username,password) values(%s,%s)'
                    values = (username.get(),password.get())
                    cur.execute(query,values)
                    connection.commit()    
                    connection.close()
                    messagebox.showinfo('Success',"User has been registered!!")
                    user_entry.delete(0,END)
                    pass_entry.delete(0,END)
                    self.register_screen.destroy()    
        btn_login=Button(self.register_screen,text="Register",width=10,command=create_user,font=('times new roman',15,'bold'),bg='crimson',fg='yellow')
        btn_login.place(x=170,y=250)        

root=Tk()
obj=login_system(root)
root.mainloop()        