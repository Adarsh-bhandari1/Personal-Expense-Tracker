import tkinter as tk
import psycopg2 as pg
from database import connect_to_database
import bcrypt 
from tkinter import *

# REGISTER WINDOW CODE 
def register_window():
    reg_win=tk.Toplevel()
    reg_win.title('Register')
    reg_win.geometry('350x250')
    Label(reg_win , text='username').grid(row=0,column=0,padx=10,pady=5)
    Entry(reg_win).grid(row=0,column=1,padx=10,pady=5)
    Label(reg_win,text='password').grid(row=2,column=0,padx=10,pady=5)
    Entry(reg_win,show='*').grid(row=2,column=1,padx=10)
    Button(reg_win,text='register').grid(row=3,column=1,pady=3)



# MAIN WINDOW CODE 
def main_window():
    root=tk.Tk()
    root.title("Personal Expense tracker")
    root.geometry('400x300')

    """login_btn=Button(root,text='Login',command=login_window)
    login_btn.pack()"""

    Register_btn=Button(root, text='Resgister',command=register_window)
    Register_btn.pack()
    root.mainloop()
main_window()

