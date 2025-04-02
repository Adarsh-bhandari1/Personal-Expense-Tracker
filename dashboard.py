import tkinter as tk
from tkinter import messagebox
from tkinter import *

# DASHBOARD WINDOW CODE
class Dashboard:
    def __init__(self,conn,dash,get_username):
        self.conn=conn
        self.dash=dash
        self.username=get_username
        self.dash_window()

    def dash_window(self):
        for widget in self.dash.winfo_children():
            widget.destroy()
        self.dash.title('Dashboard')
        self.dash.geometry('400x300')
        self.dash.configure(bg='lightblue')
        self.dash.resizable(False , False)
        Label(self.dash ,text=f"Welcome,{self.username} !",font=("Arial" , 14 , "bold")).grid(row=0,column=0,padx=10,pady=10)
        self.dash.grid_columnconfigure(0,weight=1)
      
        