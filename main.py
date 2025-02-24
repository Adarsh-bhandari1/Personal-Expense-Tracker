import tkinter as tk
import psycopg2 as pg
from database import connect_to_database
from database import close_database_connection
import bcrypt 
from tkinter import *
from tkinter import messagebox
import threading

# Dashboard CODE
def dashboard(conn):
    dash_bd=tk.Toplevel()
# REGISTER WINDOW CODE 
def register_window():
    reg_win=tk.Toplevel()
    reg_win.title('Register')
    reg_win.geometry('350x250')
    Label(reg_win , text='username').grid(row=0,column=0,padx=10,pady=5)
    global username,password
    username=tk.Entry(reg_win)
    username.grid(row=0,column=1,padx=10,pady=5)
    Label(reg_win,text='password').grid(row=2,column=0,padx=10,pady=5)
    password=tk.Entry(reg_win,show='*')
    password.grid(row=2,column=1,padx=10)

   # Registeration function
    def reg_function():
        username_get=username.get().strip()
        password_get=password.get().strip()
        if not username_get or not  password_get:
            messagebox.showerror(" Error ","All fields required")
            return
        try:
            conn=connect_to_database()
            cur=conn.cursor()
            cur.execute("SELECT * FROM user_credentials WHERE user_name = %s",(username_get,))
            if cur.fetchone():
                messagebox.showerror("Error","User name already exists")
                close_database_connection(conn)
            else:
                hash_pass=bcrypt.hashpw(password_get.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
                cur.execute("INSERT INTO user_credentials (user_name , password_hash) VALUES (%s , %s )",(username_get,hash_pass))
                conn.commit()
                cur.close()
                messagebox.showinfo("Success","Registration successful")
                close_database_connection(conn)
                reg_win.destroy()
                
            
        except Exception as e:
            messagebox.showerror("Error","Cannot connect to database")
    Button(reg_win,text='register',command=reg_function).grid(row=3,column=1,pady=3)

# LOFIN WINDOW CODE
def login_window():
    login=tk.Toplevel()
    login.title("Login")
    login.geometry('350x250')
    global log_username,log_password
    Label(login,text="Username").grid(row=0,column=0,padx=10,pady=5)
    log_username=tk.Entry(login)
    log_username.grid(row=0,column=1,padx=10,pady=5)
    Label(login,text="password").grid(row=1,column=0,padx=10,pady=5)
    log_password=tk.Entry(login)
    log_password.grid(row=1,column=1,padx=10,pady=5)
    def login_function():
        get_username=log_username.get().strip()
        get_password=log_password.get().strip()
        if not get_username or not get_password :
            messagebox.showerror("Error","All fields required")
            return
        try:
            conn=connect_to_database()
            cur=conn.cursor()
            #Fetch password hash from database 
            cur.execute("SELECT password_hash FROM user_credentials WHERE user_name = %s  " , (get_username,))
            result=cur.fetchone()
            if result:
                store_hash=result[0] #result[0] will give the value whereas result will give the tuple not the value 
            
                if bcrypt.checkpw(get_password.encode('utf-8'),store_hash.encode('utf-8')):
                    messagebox.showinfo("Success","Login successful")
                    dashboard(conn)
                else:
                    messagebox.showerror("Error","Invalid password , Please Re-try")
            else:
                messagebox.showerror("Error","User not found ")

        except Exception as e:
            print("Database Error : " , e)
            messagebox.showerror("error" ,"Databse error ")
            close_database_connection(conn)

    Button(login,text="Login",command=login_function).grid(row=3,column=1,pady=3)
# MAIN WINDOW CODE 
def main_window():
    root=tk.Tk()
    root.title("Personal Expense tracker")
    root.geometry('400x300')
    root.resizable(width=500 ,height= 400)

    login_btn=Button(root,text='Login',command=login_window)
    login_btn.pack()
    
    Register_btn=Button(root, text='Resgister',command=register_window)
    Register_btn.pack()

    root.mainloop()
main_window()

