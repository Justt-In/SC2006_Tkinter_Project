import os
import tkinter as tk
import customtkinter
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
from datetime import datetime
from random import randint
import re
from hashlib import blake2b


class Register_page(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        if customtkinter.get_appearance_mode() == "light" or customtkinter.get_appearance_mode() == "Light":
            main_bg = "#ffe5d9"
            accentColour = "#48CAE4"
            accentColour2 = "#E46248"
            textColour = "black"
            backdrop = "images/backdropv3_2.png"
        else:
            main_bg = "#464646"
            accentColour = "#0077b6"
            accentColour2 = "#B63F00"
            textColour = "black"
            backdrop = "images/backdropv3_4.png"
        customtkinter.CTkFrame.__init__(self, parent, fg_color=main_bg)
        self.controller = controller
        connection = sqlite3.connect('Databases/User_database.db')
        cursor = connection.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS User(profile_pic TEXT, creation_date TEXT, data_protect BOOLEAN, fullname TEXT, age INT, nationality TEXT, username TEXT, email TEXT, github TEXT, linkedIn TEXT, code_lang TEXT, events TEXT, meeting_mode TEXT, meeting_region TEXT, field_study TEXT, years_in_field INT, short_Desc TEXT, user_preference TEXT)'''
        cursor.execute(sql)
        connection.commit()

        #Create elements & widgets
        self.space_label1 = customtkinter.CTkLabel(self, height=100, width=1280, bg_color=accentColour, text='Registration',
                                                   text_color=textColour, text_font=['trebuchet MS bold', 42])
        self.load_register_icon = tk.PhotoImage(file="images/register_hello.png")
        self.register_icon_label = tk.Label(self, image=self.load_register_icon, bg=accentColour)

        self.load_return_img = Image.open("images/back_icon.png")
        return_img = ImageTk.PhotoImage(self.load_return_img.resize((128, 128), Image.ANTIALIAS))
        self.return_login = customtkinter.CTkButton(self, image=return_img, bg_color=accentColour, fg_color=accentColour2,
                                                    hover_color="light blue", text="Return", text_color=textColour,
                                                    text_font=['trebuchet MS bold', 20],
                                                    command=lambda: controller.show_frame("Login"))
        #Backdrop Left
        self.load_backdrop1_img = Image.open(backdrop)
        self.backdrop1 = ImageTk.PhotoImage(self.load_backdrop1_img.resize((500, 800), Image.ANTIALIAS))
        self.backdrop1_label = customtkinter.CTkLabel(self, image=self.backdrop1, bg=main_bg)
        self.username_label = customtkinter.CTkLabel(self, text='Username', text_font='Bahnschrift 20 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.username_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)
        def handleFocusIn(_):
            self.password_entry.configure(fg='black', show='*')
            self.retype_password_entry.configure(fg='black', show='*')
        self.password_label = customtkinter.CTkLabel(self, text='Password', text_font='Bahnschrift 20 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.password_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)
        self.password_entry.bind('<FocusIn>', handleFocusIn)
        self.retype_password_label = customtkinter.CTkLabel(self, text='Retype Password', text_font='Bahnschrift 20 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.retype_password_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)
        self.retype_password_entry.bind('<FocusIn>', handleFocusIn)
        self.email_label = customtkinter.CTkLabel(self, text='Email', text_font='Bahnschrift 20 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.email_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)
        self.fullname_label = customtkinter.CTkLabel(self, text='Full Name', text_font='Bahnschrift 20 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.fullname_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)
        self.nationality_label = customtkinter.CTkLabel(self, text='Nationality', text_font='Bahnschrift 20 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.nationality_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)
        self.github_label = customtkinter.CTkLabel(self, text='Github Username (Optional)', text_font='Bahnschrift 16 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.github_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)

        #Backdrop Middle
        self.backdrop3 = self.backdrop1
        self.backdrop3_label = customtkinter.CTkLabel(self, image=self.backdrop1, bg=main_bg)
        self.LinkedIn_label = customtkinter.CTkLabel(self, text='LinkedIn URL (Optional)', text_font='Bahnschrift 15 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.LinkedIn_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)
        self.age_label = customtkinter.CTkLabel(self, text='Age', text_font='Bahnschrift 20 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.age_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)

        self.meet_pref_dd = customtkinter.CTkOptionMenu(self, values=["Virtual", "Physical", "None"])
        self.meet_pref_dd.set("Meeting Preference")
        self.meet_pref_dd.configure(text_font='Bahnschrift 20 bold', bg_color=accentColour, fg_color=accentColour2,
                                        text_color=textColour, button_color=accentColour2, dropdown_color=accentColour2,
                                        dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 18 bold',
                                        width=190)

        self.locale_pref_dd = customtkinter.CTkOptionMenu(self, values=["Central SG", "North SG", "East SG", "South SG", "West SG"])
        self.locale_pref_dd.set("Preferred Area")
        self.locale_pref_dd.configure(text_font='Bahnschrift 20 bold', bg_color=accentColour, fg_color=accentColour2,
                                    text_color=textColour, button_color=accentColour2, dropdown_color=accentColour2,
                                    dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 18 bold',
                                    width=190)


        self.field_label = customtkinter.CTkLabel(self, text='Specialization/Field of Study', text_font='Bahnschrift 16 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.field_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)
        self.year_of_exp_label = customtkinter.CTkLabel(self, text='Years of Experience in Field', text_font='Bahnschrift 16 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.year_of_exp_entry = customtkinter.CTkEntry(self, text_font=['arial', 16], width=250, bg_color=accentColour,
                                                     fg_color='white', border_color='black', text_color=textColour)

        #Backdrop Right
        self.backdrop2 = self.backdrop1
        self.backdrop2_label = customtkinter.CTkLabel(self, image=self.backdrop2, bg='#2176FF')
        var1 = tk.IntVar(self)
        var2 = tk.IntVar(self)
        var3 = tk.IntVar(self)
        var4 = tk.IntVar(self)
        var5 = tk.IntVar(self)
        var6 = tk.IntVar(self)
        var7 = tk.IntVar(self)
        var8 = tk.IntVar(self)
        var9 = tk.IntVar(self)
        var10 = tk.IntVar(self)

        self.experience1 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience1.set("Experience")
        self.experience1.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                    text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                    dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                    width=100)
        self.switch1 = customtkinter.CTkSwitch(self, bg_color=accentColour,text='', variable=var1, fg_color='red', progress_color='#2BD447')
        self.switchLabel1 = customtkinter.CTkLabel(self, text='Python', text_font='Bahnschrift 14 bold',
                                                     bg_color=accentColour, text_color=textColour)
        self.experience2 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience2.set("Experience")
        self.experience2.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch2 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var2, fg_color='red', progress_color='#2BD447')
        self.switchLabel2 = customtkinter.CTkLabel(self, text='C++', text_font='Bahnschrift 14 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.experience3 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience3.set("Experience")
        self.experience3.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch3 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var3, fg_color='red', progress_color='#2BD447')
        self.switchLabel3 = customtkinter.CTkLabel(self, text='C#', text_font='Bahnschrift 14 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.experience4 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience4.set("Experience")
        self.experience4.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch4 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var4, fg_color='red', progress_color='#2BD447')
        self.switchLabel4 = customtkinter.CTkLabel(self, text='C', text_font='Bahnschrift 14 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.experience5 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience5.set("Experience")
        self.experience5.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch5 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var5, fg_color='red', progress_color='#2BD447')
        self.switchLabel5 = customtkinter.CTkLabel(self, text='Java', text_font='Bahnschrift 14 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.experience6 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience6.set("Experience")
        self.experience6.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch6 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var6, fg_color='red', progress_color='#2BD447')
        self.switchLabel6 = customtkinter.CTkLabel(self, text='Javascript', text_font='Bahnschrift 12 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.experience7 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience7.set("Experience")
        self.experience7.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch7 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var7, fg_color='red', progress_color='#2BD447')
        self.switchLabel7 = customtkinter.CTkLabel(self, text='PHP', text_font='Bahnschrift 14 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.experience8 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience8.set("Experience")
        self.experience8.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch8 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var8, fg_color='red', progress_color='#2BD447')
        self.switchLabel8 = customtkinter.CTkLabel(self, text='SQL', text_font='Bahnschrift 14 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.experience9 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience9.set("Experience")
        self.experience9.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch9 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var9, fg_color='red', progress_color='#2BD447')
        self.switchLabel9 = customtkinter.CTkLabel(self, text='HTML', text_font='Bahnschrift 14 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.experience10 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience10.set("Experience")
        self.experience10.configure(text_font='Bahnschrift 12 bold', bg_color=accentColour, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch10 = customtkinter.CTkSwitch(self, bg_color=accentColour, text='', variable=var10, fg_color='red', progress_color='#2BD447')
        self.switchLabel10 = customtkinter.CTkLabel(self, text='CSS', text_font='Bahnschrift 14 bold',
                                                   bg_color=accentColour, text_color=textColour)
        self.error_label = tk.Label(self, text="", font='Bahnschrift 14 underline bold', bg=main_bg, fg='red')
        def goto_cfm_page():
            count = 0
            counter = 0
            data_trust = 'Yes'
            user_conn = sqlite3.connect("Databases/User_database.db")
            user_cursor = user_conn.cursor()
            user_cursor.execute("SELECT username FROM User")
            username_list = user_cursor.fetchall()

            def isAllPresent(str):

                # ReGex to check if a string
                # contains uppercase, lowercase
                # special character & numeric value
                regex = ("^(?=.*[a-z])(?=." +
                         "*[A-Z])(?=.*\\d)" +
                         "(?=.*[-+_!@#$%^&*., ?]).+$")

                # Compile the ReGex
                p = re.compile(regex)

                # If the string is empty
                # return false
                if (str == None):
                    return "no"

                # Print Yes if string
                # matches ReGex
                if (re.search(p, str)):
                    return "yes"
                else:
                    return "no"
            #personal details
            username = self.username_entry.get()
            if len(username) <= 5:
                self.error_label['text'] = 'Username has to be longer than 5 characters'
                self.error_label.place(x=50, y=1020)
                return
            for name in username_list:
                if username == name[0]:
                    self.error_label['text'] = 'Username already exists, please choose another'
                    self.error_label.place(x=50, y=1020)
                    return
            if username == '': count+=1
            else:
                f = open('Databases/event.txt', 'r+')
                f.truncate(0)
                f = open("Databases/event.txt", "a")
                f.write(username)
                f.close()
            password = self.password_entry.get()
            if len(password) < 8:
                self.error_label['text'] = 'Password has to be more than 8 characters'
                self.error_label.place(x=50, y=1020)
                return
            regex = isAllPresent(password)
            if regex == "no":
                self.error_label['text'] = 'Password must contain Upper & Lowercase, \nNumbers & Special Character'
                self.error_label.place(x=50, y=1000)
                return
            if password == '': count += 1
            else:
                h = blake2b()
                h.update(password.encode())
                password = h.hexdigest()
            re_password = self.retype_password_entry.get()
            if re_password == '': count += 1
            else:
                h = blake2b()
                h.update(re_password.encode())
                re_password = h.hexdigest()
            if password != re_password: counter += 1
            email = self.email_entry.get()
            if email == '': count += 1
            fullname = self.fullname_entry.get()
            if fullname == '': count += 1
            nationality = self.nationality_entry.get()
            if nationality == '': count += 1
            github = self.github_entry.get()
            if github == '':
                github = ''
            linkedin = self.LinkedIn_entry.get()
            if linkedin == '':
                linkedin = ''
            age = self.age_entry.get()
            if age == '': count += 1
            meet_pref = self.meet_pref_dd.get()
            if meet_pref == 'Meeting Preference': count += 1
            locale_pref = self.locale_pref_dd.get()
            if locale_pref == 'Preferred Area': count += 1
            field = self.field_entry.get()
            if field == '': count += 1
            years_exp = self.year_of_exp_entry.get()
            if years_exp == '': count += 1

            #coding knowledge
            coding_prof = ''
            print(self.switch1.get())
            if self.switch1.get() == 1:
                python = self.experience1.get()
                if python == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', Python ' + python
            if self.switch2.get() == 1:
                c_plus = self.experience2.get()
                if c_plus == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', C++ ' + c_plus
            if self.switch3.get() == 1:
                c_sharp = self.experience3.get()
                if c_sharp == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', C# ' + c_sharp
            if self.switch4.get() == 1:
                c_only = self.experience4.get()
                if c_only == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', C ' + c_only
            if self.switch5.get() == 1:
                java = self.experience5.get()
                if java == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', Java ' + java
            if self.switch6.get() == 1:
                javascript = self.experience6.get()
                if javascript == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', Javascript ' + javascript
            if self.switch7.get() == 1:
                php = self.experience7.get()
                if php == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', PHP ' + php
            if self.switch8.get() == 1:
                s_q_l = self.experience8.get()
                if s_q_l == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', SQL ' + s_q_l
            if self.switch9.get() == 1:
                html = self.experience9.get()
                if html == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', HTML ' + html
            if self.switch10.get() == 1:
                css = self.experience10.get()
                if css == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', CSS ' + css

            date_time = str(datetime.now())

            if counter > 0:
                self.error_label['text'] = 'Your Passwords Do Not Match Up'
                self.error_label.place(x=50, y=1020)
            elif count > 0:
                self.error_label['text'] = 'Please Double Check Your Entries'
                self.error_label.place(x=50, y=1020)
            else:
                ans = tk.messagebox.askquestion("Username Warning","Your Username cannot be changed in tuhe future.\nDo you wish to proceed?")
                if ans == "yes":
                    connection.cursor()
                    cursor.execute(
                        'INSERT INTO User(creation_date, data_protect, fullname, age, nationality, username, password, email, github, linkedIn, code_lang, meeting_mode, meeting_region, field_study, years_in_field) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                        (date_time, data_trust, fullname, age, nationality, username, password, email, github, linkedin,
                         coding_prof, meet_pref, locale_pref, field, years_exp))
                    connection.commit()
                    data = cursor.execute('SELECT * FROM User')
                    for row in data:
                        print(row)
                    connection.close()
                    controller.show_frame('Register_confirmation_page')
                else:
                    return

        self.next_button = customtkinter.CTkButton(self, text='Continue To Next Step', text_font='Bahnschrift 20 bold',
                                                   bg_color=main_bg, fg_color='#0d9c8c', text_color=textColour,
                                                   command=goto_cfm_page)
        #Arrange elements & widgets in grid
        self.space_label1.place(x=0, y=0)
        self.register_icon_label.place(x=560, y=5)
        self.return_login.place(x=900, y=5)

        #Backdrop1
        self.backdrop1_label.place(x=25, y=125)
        self.username_label.place(x=125, y=140)
        self.username_label.tkraise()
        self.username_entry.place(x=65, y=175)
        self.username_entry.tkraise()
        self.password_label.place(x=125, y=210)
        self.password_label.tkraise()
        self.password_entry.place(x=65, y=245)
        self.password_entry.tkraise()
        self.retype_password_label.place(x=85, y=280)
        self.retype_password_label.tkraise()
        self.retype_password_entry.place(x=65, y=315)
        self.retype_password_entry.tkraise()
        self.email_label.place(x=125, y=350)
        self.email_label.tkraise()
        self.email_entry.place(x=65, y=385)
        self.email_entry.tkraise()
        self.fullname_label.place(x=125, y=420)
        self.fullname_label.tkraise()
        self.fullname_entry.place(x=65, y=455)
        self.fullname_entry.tkraise()
        self.nationality_label.place(x=125, y=490)
        self.nationality_label.tkraise()
        self.nationality_entry.place(x=65, y=525)
        self.nationality_entry.tkraise()
        self.github_label.place(x=60, y=560)
        self.github_label.tkraise()
        self.github_entry.place(x=65, y=590)
        self.github_entry.tkraise()
        #Backdrop3
        self.backdrop3_label.place(x=475, y=125)
        self.LinkedIn_label.place(x=535, y=145)
        self.LinkedIn_label.tkraise()
        self.LinkedIn_entry.place(x=515, y=175)
        self.LinkedIn_entry.tkraise()
        self.age_label.place(x=570, y=210)
        self.age_entry.place(x=515, y=245)
        self.meet_pref_dd.place(x=505, y=300)
        self.locale_pref_dd.place(x=505, y=370)
        self.field_label.place(x=505, y=435)
        self.field_entry.place(x=515, y=470)
        self.year_of_exp_label.place(x=505, y=505)
        self.year_of_exp_entry.place(x=515, y=540)
        #Backdrop2
        self.backdrop2_label.place(x=925, y=125)
        self.experience1.place(x=1100, y=170)
        self.experience1.tkraise()
        self.switchLabel1.place(x=980, y=170)
        self.switch1.place(x=960, y=175)
        self.switch1.tkraise()
        self.experience2.place(x=1100, y=210)
        self.experience2.tkraise()
        self.switchLabel2.place(x=970, y=210)
        self.switch2.place(x=960, y=215)
        self.switch2.tkraise()
        self.experience3.place(x=1100, y=250)
        self.experience3.tkraise()
        self.switchLabel3.place(x=965, y=250)
        self.switch3.place(x=960, y=255)
        self.switch3.tkraise()
        self.experience4.place(x=1100, y=290)
        self.experience4.tkraise()
        self.switchLabel4.place(x=970, y=290)
        self.switch4.place(x=960, y=295)
        self.switch4.tkraise()
        self.experience5.place(x=1100, y=330)
        self.experience5.tkraise()
        self.switchLabel5.place(x=970, y=330)
        self.switch5.place(x=960, y=335)
        self.switch5.tkraise()
        self.experience6.place(x=1100, y=370)
        self.experience6.tkraise()
        self.switchLabel6.place(x=970, y=370)
        self.switch6.place(x=960, y=375)
        self.switch6.tkraise()
        self.experience7.place(x=1100, y=410)
        self.experience7.tkraise()
        self.switchLabel7.place(x=970, y=410)
        self.switch7.place(x=960, y=415)
        self.switch7.tkraise()
        self.experience8.place(x=1100, y=450)
        self.experience8.tkraise()
        self.switchLabel8.place(x=970, y=450)
        self.switch8.place(x=960, y=455)
        self.switch8.tkraise()
        self.experience9.place(x=1100, y=490)
        self.experience9.tkraise()
        self.switchLabel9.place(x=970, y=490)
        self.switch9.place(x=960, y=495)
        self.switch9.tkraise()
        self.experience10.place(x=1100, y=530)
        self.experience10.tkraise()
        self.switchLabel10.place(x=970, y=530)
        self.switch10.place(x=960, y=535)
        self.switch10.tkraise()
        self.next_button.place(x=500, y=670)

