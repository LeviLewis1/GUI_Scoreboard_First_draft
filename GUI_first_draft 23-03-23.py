import tkinter as tk 
from tkinter import *
from tkinter import messagebox
import os 
import time

def check_validity():
    username = "Admin"
    password = "Admin1"
    if username_entry == username_entry == username and password_entry == password:
        def main_menu():
            main_menu_window = Tk()
            main_menu_window.geometry("300x300")
            main_menu_window.title("Main Menu")
            main_menu_window.mainloop()
        main_menu()
    else:
       def error_msg_login():
           messagebox.showerror("Invalid Login", "You have entered invalid credentials")
       error_msg_login()

login_page = Tk()

login_page.geometry("200x100")
login_page.title("Please log in")
login_page.configure(bg = "#fff")

username_label = Label(login_page, text= "Username").grid(row = 0, column = 0)
username_entry = Entry(login_page).grid(row = 0, column = 1)

password_label = Label(login_page, text= "Password").grid(row = 1, column = 0)
password_entry = Entry(login_page).grid(row = 1, column = 1)

login_button = Button(login_page, text = "Log in", command=check_validity).grid(row = 4, column = 0)
                                                                                
login_page.mainloop()
