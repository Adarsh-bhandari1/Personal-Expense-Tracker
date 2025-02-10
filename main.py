import tkinter as tk
import psycopg2 as pg
from database import connect_to_database
import bcrypt 
from tkinter import *
def main_window():
    root=tk.Tk()
    root.title("Personal Expense tracker")
    root.geometry('400x300')
    login=Label(root,text='Login',font=('Arial',20))
    login.pack()
    login_btn=Button(root,text='Login')
    login_btn.pack()
    root.mainloop()
main_window()