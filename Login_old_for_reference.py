import os
import tkinter as tk
from tkinter import ttk

root = tk.Tk(className='Binary')

# set window size
root.geometry("1024x768")

#create frames
login = tk.Frame(root)
registration = tk.Frame(root)
recommendations = tk.Frame(root)

#set background
bg = tk.PhotoImage(file = "images/angryimg.png")
bg_label = tk.Label(root, image = bg, bd=-2)
bg_label.place(x=0, y=0)

#set logo
logo = tk.PhotoImage(file = "images/binary_home.png")
logo_label = tk.Label(image = logo, bd=-2)
logo_label.place(x=380, y=100)


#set textboxes
def temp_text_user_In(e, username=None):
   username.delete(0,"end")
def temp_text_user_Out(e, username=None):
   username.insert(0,"Username")

username = tk.Entry(root, bg="white", width=45,borderwidth=2)
username.insert(0, "Username")
username.bind("<FocusIn>", temp_text_user_In)
username.bind("<FocusOut>", temp_text_user_Out)
username.place(x=380, y=355, height=40)

def temp_text_pass_In(e, password=None):
   password.delete(0,"end")
def temp_text_pass_Out(e, password=None):
   password.insert(0,"Password")

password = tk.Entry(root, bg="white", width=45, borderwidth=2)
password.insert(0, "Password")
password.bind("<FocusIn>", temp_text_pass_In)
password.bind("<FocusOut>", temp_text_pass_Out)
password.place(x=380, y=400, height=40)

#set sign up and login
def goSignUpView():
    registration.pack(fill="both", expand=1)
    login.pack_forget()

sign_up = tk.Button(root, bg="orange", text="Sign Up", font="Lato 20 bold", width=10,  command = goSignUpView())
sign_up.place(x=390, y=450)

def goRegistrationView():
    registration.pack(fill="both", expand=1)
    login.pack_forget()
    os.system("Registration.py")

lg = tk.PhotoImage(file = "images/img_login.png")
login = tk.Button(root, image=lg,bg="orange", command=goRegistrationView())
login.place(x=590, y=450)


root.mainloop()