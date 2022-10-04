import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import sqlite3
from datetime import datetime
from random import randint
from hashlib import blake2b

class Register_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5cc9ed')
        self.controller = controller
        connection = sqlite3.connect('Databases/User_database.db')
        cursor = connection.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS User(profile_pic TEXT, creation_date TEXT, data_protect BOOLEAN, fullname TEXT, age INT, nationality TEXT, username TEXT, email TEXT, github TEXT, linkedIn TEXT, code_lang TEXT, events TEXT, meeting_mode TEXT, meeting_region TEXT, field_study TEXT, years_in_field INT, short_Desc TEXT, user_preference TEXT)'''
        cursor.execute(sql)
        connection.commit()
        #Create elements & widgets
        self.space_label1 = tk.Label(self, width=1000, height=9, bg="#ff8c1a", borderwidth=2, relief='solid')
        self.load_register_icon = tk.PhotoImage(file="images/register_hello.png")
        self.register_icon_label = tk.Label(self, image=self.load_register_icon, bg="#ff8c1a")
        self.register_label = tk.Label(self, text='Registration', font='Bahnschrift 70 bold', bg="#ff8c1a")
        #Backdrop Left
        self.load_backdrop1_img = Image.open("images/backdrop1_v.png")
        self.backdrop1 = ImageTk.PhotoImage(self.load_backdrop1_img.resize((450, 600), Image.ANTIALIAS))
        self.backdrop1_label = tk.Label(self, image=self.backdrop1, bg='#5cc9ed')
        self.username_label = tk.Label(self, text='Username', font='Bahnschrift 20 bold', bg='#4C5270')
        self.username_entry = tk.Entry(self,font=('arial', 16), width=24)
        def handleFocusIn(_):
            self.password_entry.configure(fg='black', show='*')
            self.retype_password_entry.configure(fg='black', show='*')
        self.password_label = tk.Label(self, text='Password', font='Bahnschrift 20 bold', bg='#4C5270')
        self.password_entry = tk.Entry(self, font=('arial', 16), width=24)
        self.password_entry.bind('<FocusIn>', handleFocusIn)
        self.retype_password_label = tk.Label(self, text='Retype Password', font='Bahnschrift 20 bold', bg='#4C5270')
        self.retype_password_entry = tk.Entry(self, font=('arial', 16), width=24)
        self.retype_password_entry.bind('<FocusIn>', handleFocusIn)
        self.email_label = tk.Label(self, text='Email', font='Bahnschrift 20 bold', bg='#4C5270')
        self.email_entry = tk.Entry(self, font=('arial', 16), width=24)
        self.fullname_label = tk.Label(self, text='Full Name', font='Bahnschrift 20 bold', bg='#4C5270')
        self.fullname_entry = tk.Entry(self, font=('arial', 16), width=24)
        self.nationality_label = tk.Label(self, text='Nationality', font='Bahnschrift 20 bold', bg='#4C5270')
        self.nationality_entry = tk.Entry(self, font=('arial', 16), width=24)
        self.github_label = tk.Label(self, text='Github Username(Optional)', font='Bahnschrift 20 bold', bg='#4C5270')
        self.github_entry = tk.Entry(self, font=('arial', 16), width=24)
        #Backdrop Middle
        self.backdrop3 = self.backdrop1
        self.backdrop3_label = tk.Label(self, image=self.backdrop1, bg='#5cc9ed')
        self.LinkedIn_label = tk.Label(self, text='LinkedIn URL (Optional)', font='Bahnschrift 20 bold', bg='#4C5270')
        self.LinkedIn_entry = tk.Entry(self, font=('arial', 16), width=24)
        self.age_label = tk.Label(self, text='Age', font='Bahnschrift 20 bold', bg='#4C5270')
        self.age_entry = tk.Entry(self, font=('arial', 16), width=24)
        self.meet_pref = tk.StringVar(self)
        self.meet_pref.set("Meeting Preference")  # default value
        self.meet_pref_dd = tk.OptionMenu(self, self.meet_pref,"Virtual", "Physical", "None")
        self.meet_pref_dd.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        meet_pref_menu = self.nametowidget(self.meet_pref_dd.menuname)
        meet_pref_menu.configure(font='Bahnschrift 12 bold')
        self.locale_pref = tk.StringVar(self)
        self.locale_pref.set("Preferred Area")  # default value
        self.locale_pref_dd = tk.OptionMenu(self, self.locale_pref,"Central SG", "North SG", "East SG", "South SG", "West SG")
        self.locale_pref_dd.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        locale_pref_menu = self.nametowidget(self.locale_pref_dd.menuname)
        locale_pref_menu.configure(font='Bahnschrift 12 bold')
        self.field_label = tk.Label(self, text='Specialization/Field of Study', font='Bahnschrift 20 bold', bg='#4C5270')
        self.field_entry = tk.Entry(self, font=('arial', 16), width=24)
        self.year_of_exp_label = tk.Label(self, text='Years of Experience in Field', font='Bahnschrift 20 bold',
                                    bg='#4C5270')
        self.year_of_exp_entry = tk.Entry(self, font=('arial', 16), width=24)
        #Backdrop Right
        self.backdrop2 = self.backdrop1
        self.backdrop2_label = tk.Label(self, image=self.backdrop2, bg='#5cc9ed')
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
        self.proficient1 = tk.StringVar(self)
        self.proficient1.set("Experience")  # default value
        self.proficient2 = tk.StringVar(self)
        self.proficient2.set("Experience")
        self.proficient3 = tk.StringVar(self)
        self.proficient3.set("Experience")
        self.proficient4 = tk.StringVar(self)
        self.proficient4.set("Experience")
        self.proficient5 = tk.StringVar(self)
        self.proficient5.set("Experience")
        self.proficient6 = tk.StringVar(self)
        self.proficient6.set("Experience")
        self.proficient7 = tk.StringVar(self)
        self.proficient7.set("Experience")
        self.proficient8 = tk.StringVar(self)
        self.proficient8.set("Experience")
        self.proficient9 = tk.StringVar(self)
        self.proficient9.set("Experience")
        self.proficient10 = tk.StringVar(self)
        self.proficient10.set("Experience")

        self.experience1 = tk.OptionMenu(self, self.proficient1, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience1.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience1_menu = self.nametowidget(self.experience1.menuname)
        experience1_menu.configure(font='Bahnschrift 12 bold')
        self.check1 = tk.Checkbutton(self, text='Python', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var1)
        self.experience2 = tk.OptionMenu(self, self.proficient2, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience2.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience2_menu = self.nametowidget(self.experience2.menuname)
        experience2_menu.configure(font='Bahnschrift 12 bold')
        self.check2 = tk.Checkbutton(self, text='C++', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var2)
        self.experience3 = tk.OptionMenu(self, self.proficient3, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience3.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience3_menu = self.nametowidget(self.experience3.menuname)
        experience3_menu.configure(font='Bahnschrift 12 bold')
        self.check3 = tk.Checkbutton(self, text='C#', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var3)
        self.experience4 = tk.OptionMenu(self, self.proficient4, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience4.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience4_menu = self.nametowidget(self.experience4.menuname)
        experience4_menu.configure(font='Bahnschrift 12 bold')
        self.check4 = tk.Checkbutton(self, text='C', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var4)
        self.experience5 = tk.OptionMenu(self, self.proficient5, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience5.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience5_menu = self.nametowidget(self.experience5.menuname)
        experience5_menu.configure(font='Bahnschrift 12 bold')
        self.check5 = tk.Checkbutton(self, text='Java', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var5)
        self.experience6 = tk.OptionMenu(self, self.proficient6, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience6.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience6_menu = self.nametowidget(self.experience6.menuname)
        experience6_menu.configure(font='Bahnschrift 12 bold')
        self.check6 = tk.Checkbutton(self, text='Javascript', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var6)
        self.experience7 = tk.OptionMenu(self, self.proficient7, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience7.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience7_menu = self.nametowidget(self.experience7.menuname)
        experience7_menu.configure(font='Bahnschrift 12 bold')
        self.check7 = tk.Checkbutton(self, text='PHP', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var7)
        self.experience8 = tk.OptionMenu(self, self.proficient8, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience8.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience8_menu = self.nametowidget(self.experience8.menuname)
        experience8_menu.configure(font='Bahnschrift 12 bold')
        self.check8 = tk.Checkbutton(self, text='SQL', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var8)
        self.experience9 = tk.OptionMenu(self, self.proficient9, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience9.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience9_menu = self.nametowidget(self.experience9.menuname)
        experience9_menu.configure(font='Bahnschrift 12 bold')
        self.check9 = tk.Checkbutton(self, text='HTML', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var9)
        self.experience10 = tk.OptionMenu(self, self.proficient10, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience10.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience10_menu = self.nametowidget(self.experience10.menuname)
        experience10_menu.configure(font='Bahnschrift 12 bold')
        self.check10 = tk.Checkbutton(self, text='CSS', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2, variable=var10)
        self.error_label = tk.Label(self, font='Bahnschrift 20 underline', bg='#5cc9ed', bd=3, fg='red')
        def goto_cfm_page():
            count = 0
            counter = 0
            data_trust = 'Yes'
            #personal details
            username = self.username_entry.get()
            if username == '': count+=1
            else:
                f = open('Databases/event.txt', 'r+')
                f.truncate(0)
                #f = open("Databases/event.txt", "a")
                f.write(username)
                f.close()
            password = self.password_entry.get()
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
            print(email)
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
            meet_pref = self.meet_pref.get()
            if meet_pref == 'Meeting Preference': count += 1
            locale_pref = self.locale_pref.get()
            if locale_pref == 'Preferred Area': count += 1
            field = self.field_entry.get()
            if field == '': count += 1
            years_exp = self.year_of_exp_entry.get()
            if years_exp == '': count += 1

            #coding knowledge
            coding_prof = ''
            if var1.get() == 1:
                python = self.proficient1.get()
                if python == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', Python ' + python
            if var2.get() == 1:
                c_plus = self.proficient2.get()
                if c_plus == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', C++ ' + c_plus
            if var3.get() == 1:
                c_sharp = self.proficient3.get()
                if c_sharp == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', C# ' + c_sharp
            if var4.get() == 1:
                c_only = self.proficient4.get()
                if c_only == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', C ' + c_only
            if var5.get() == 1:
                java = self.proficient5.get()
                if java == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', Java ' + java
            if var6.get() == 1:
                javascript = self.proficient6.get()
                if javascript == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', Javascript ' + javascript
            if var7.get() == 1:
                php = self.proficient7.get()
                if php == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', PHP ' + php
            if var8.get() == 1:
                s_q_l = self.proficient8.get()
                if s_q_l == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', SQL ' + s_q_l
            if var9.get() == 1:
                html = self.proficient9.get()
                if html == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', HTML ' + html
            if var10.get() == 1:
                css = self.proficient10.get()
                if css == 'Experience':
                    count+=1
                else:
                    coding_prof = coding_prof + ', CSS ' + css

            date_time = str(datetime.now())

            if counter > 0:
                self.error_label['text'] = 'Your Passwords Do Not Match Up'
            elif count > 0:
                self.error_label['text'] = 'Please Double Check Your Entries'
            else:
                connection.cursor()
                cursor.execute('INSERT INTO User(creation_date, data_protect, fullname, age, nationality, username, password, email, github, linkedIn, code_lang, meeting_mode, meeting_region, field_study, years_in_field) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                               (date_time, data_trust, fullname, age, nationality, username, password, email, github, linkedin, coding_prof, meet_pref, locale_pref, field, years_exp))
                connection.commit()
                data = cursor.execute('SELECT * FROM User')
                for row in data:
                    print(row)
                connection.close()
            controller.show_frame('Register_confirmation_page')

        self.next_button = tk.Button(self, text='Continue To Next Step', font='Bahnschrift 20 bold', bg='#5cc9ed', bd=3, relief='raised', width=20, height=1, command=goto_cfm_page)

        #Arrange elements & widgets in grid
        self.space_label1.place(x=0, y=0)
        self.register_icon_label.place(x=400, y=5)
        self.register_label.place(x=550, y=10)
        #Backdrop1
        self.backdrop1_label.place(x=50, y=175)
        self.username_label.place(x=215, y=190)
        self.username_label.tkraise()
        self.username_entry.place(x=125, y=230)
        self.username_entry.tkraise()
        self.password_label.place(x=215, y=270)
        self.password_label.tkraise()
        self.password_entry.place(x=125, y=310)
        self.password_entry.tkraise()
        self.retype_password_label.place(x=170, y=350)
        self.retype_password_label.tkraise()
        self.retype_password_entry.place(x=125, y=390)
        self.retype_password_entry.tkraise()
        self.email_label.place(x=230, y=430)
        self.email_label.tkraise()
        self.email_entry.place(x=125, y=470)
        self.email_entry.tkraise()
        self.fullname_label.place(x=210, y=510)
        self.fullname_label.tkraise()
        self.fullname_entry.place(x=125, y=550)
        self.fullname_entry.tkraise()
        self.nationality_label.place(x=210, y=590)
        self.nationality_label.tkraise()
        self.nationality_entry.place(x=125, y=630)
        self.nationality_entry.tkraise()
        self.github_label.place(x=110, y=670)
        self.github_label.tkraise()
        self.github_entry.place(x=125, y=710)
        self.github_entry.tkraise()
        #Backdrop3
        self.backdrop3_label.place(x=500, y=175)
        self.LinkedIn_label.place(x=580, y=200)
        self.LinkedIn_label.tkraise()
        self.LinkedIn_entry.place(x=580, y=240)
        self.LinkedIn_entry.tkraise()
        self.age_label.place(x=700, y=280)
        self.age_entry.place(x=580, y=320)
        self.meet_pref_dd.place(x=560, y=380)
        self.locale_pref_dd.place(x=750, y=380)
        self.field_label.place(x=550, y=420)
        self.field_entry.place(x=580, y=460)
        self.year_of_exp_label.place(x=550, y=500)
        self.year_of_exp_entry.place(x=580, y=540)
        #Backdrop2
        self.backdrop2_label.place(x=950, y=175)
        self.experience1.place(x=1200, y=230)
        self.check1.place(x=1040, y=225)
        self.experience2.place(x=1200, y=270)
        self.check2.place(x=1040, y=268)
        self.experience3.place(x=1200, y=310)
        self.check3.place(x=1040, y=310)
        self.experience4.place(x=1200, y=350)
        self.check4.place(x=1040, y=348)
        self.experience5.place(x=1200, y=390)
        self.check5.place(x=1040, y=388)
        self.experience6.place(x=1200, y=430)
        self.check6.place(x=1040, y=428)
        self.experience7.place(x=1200, y=470)
        self.check7.place(x=1040, y=468)
        self.experience8.place(x=1200, y=510)
        self.check8.place(x=1040, y=508)
        self.experience9.place(x=1200, y=550)
        self.check9.place(x=1040, y=548)
        self.experience10.place(x=1200, y=590)
        self.check10.place(x=1040, y=588)

        self.error_label.place(x=520, y=780)
        self.next_button.place(x=570, y=820)


