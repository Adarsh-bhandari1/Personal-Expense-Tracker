import tkinter as tk
import psycopg2 as pg
from database import connect_to_database
import bcrypt 
from tkinter import *
root=tk.Tk()
root.title("Expense_tracker")
root.geometry('650x500')
root.mainloop()