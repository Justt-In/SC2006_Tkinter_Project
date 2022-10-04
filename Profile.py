import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import sqlite3

class Profile_page(tk.Frame):
    #Initialises the Tkinter frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='green')
        self.controller = controller
        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg='#ff8c1a', borderwidth=2, relief='solid')

        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="#ff8c1a", bd="3", height=130, relief="raised",
                                  command=lambda: controller.show_frame("Recs_page"))

        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="#ff8c1a", bd="3", height=130,
                                    relief="raised", command=lambda: controller.show_frame("Search_page"))

        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="#ff8c1a", bd="3", height=130,
                                    relief="raised", command=lambda: controller.show_frame("Events_page"))

        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="#ff8c1a", bd="3", height=130,
                                      relief="raised", command=lambda: controller.show_frame("Contacts_page"))

        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="#ff8c1a", bd="3", height=130,
                                     relief="raised", command=lambda: controller.show_frame("Profile_page"))
        # End of Toolbar

        #Create elements & widgets
        self.email_label = tk.Label(self, text='Email', font='Bahnschrift 16 bold', bg='green')
        self.email_entry = tk.Entry(self, font='Bahnschrift 16')
        self.name_label = tk.Label(self, text='Name', font='Bahnschrift 16 bold', bg='green')
        self.name_entry = tk.Entry(self, font='Bahnschrift 16')
        self.nationality_label = tk.Label(self, text='Nationality', font='Bahnschrift 16 bold', bg='green')
        self.nationality_entry = tk.Entry(self, font='Bahnschrift 16')
        self.meetOpt = tk.StringVar(self)
        self.meetOpt.set("Meeting Preference")
        self.meetPref = tk.OptionMenu(self, self.meetOpt, "Virtual", "Physical", "None")
        self.meetPref.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        meetPref_menu = self.nametowidget(self.meetPref.menuname)
        meetPref_menu.configure(font='Bahnschrift 12 bold')
        self.areaOpt = tk.StringVar(self)
        self.areaOpt.set("Preferred Area")
        self.areaPref = tk.OptionMenu(self, self.areaOpt, "Central SG", "North SG", "East SG", "South SG", "West SG")
        self.areaPref.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        areaPref_menu = self.nametowidget(self.areaPref.menuname)
        areaPref_menu.configure(font='Bahnschrift 12 bold')
        self.github_label = tk.Label(self, text='Github Username (Optional)', font='Bahnschrift 16 bold', bg='green')
        self.github_entry = tk.Entry(self, font='Bahnschrift 16')
        self.linkedIn_label = tk.Label(self, text='LinkedIn Url (Optional)', font='Bahnschrift 16 bold', bg='green')
        self.linkedIn_entry = tk.Entry(self, font='Bahnschrift 16')
        self.age_label = tk.Label(self, text='Age', font='Bahnschrift 16 bold', bg='green')
        self.age_entry = tk.Entry(self, font='Bahnschrift 16')
        self.specialize_label = tk.Label(self, text='Specialization/Field of study', font='Bahnschrift 16 bold', bg='green')
        self.specialize_entry = tk.Entry(self, font='Bahnschrift 16')
        self.fieldYrs_label = tk.Label(self, text='Years in Specialization', font='Bahnschrift 16 bold', bg='green')
        self.fieldYrs_entry = tk.Entry(self, font='Bahnschrift 16')
        self.load_profile_pic = Image.open('images/default_profile_img.png')
        self.default_pic = ImageTk.PhotoImage(self.load_profile_pic.resize((200, 200), Image.ANTIALIAS))
        self.profile_pic_label = tk.Label(self, image=self.default_pic, bg='green')

        #This function allows the user to change their profile picture and updates dynamically upon update, it also
        # saves the image to the database immediately
        def change_pic():
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            file = open("Databases/logs.txt", "r")
            username = file.read()
            file.close()
            username = username[:-1]
            filename = filedialog.askopenfilename(initialdir="C:\\", filetypes=(
            ("PNG file", "*.png"), ("JPEG File", "*.jpeg"), ("JPG File", "*.jpg"), ("All File Types", "*.*")))
            cursor.execute("UPDATE User SET profile_pic = ? WHERE username = ?", [filename, username])
            connection.commit()
            connection.close()
            stgImg = ImageTk.PhotoImage(file=filename)
            self.profile_pic_label.configure(image=stgImg)
            self.profile_pic_label.image = stgImg

        self.pic_btn = tk.Button(self, text='Change Picture', width=20, height=1, relief='solid', font='Bahnschrift 16 underline bold', bg='cyan', command=change_pic)
        self.username_label = tk.Label(self, text='Username', font='Bahnschrift 50 underline bold', bg='green')

        #This function gets the data of the logged in user from the database and displays his/her details on screen
        def start_edits():
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            file = open("Databases/logs.txt", "r")
            username = file.read()
            file.close()
            username = username[:-1]
            self.username_label["text"] = username
            cursor.execute("SELECT profile_pic FROM User WHERE username = ?", [username])
            file_path = str(cursor.fetchall())[3:-4]
            print(file_path)
            img2 = ImageTk.PhotoImage(Image.open(file_path))
            self.profile_pic_label.configure(image=img2)
            self.profile_pic_label.image = img2
            cursor.execute("SELECT short_Desc FROM User WHERE username = ?", [username])
            new_desc = str(cursor.fetchall())[3:-4]
            self.user_desc.insert('insert',new_desc)
            cursor.execute("SELECT fullname FROM User WHERE username = ?", [username])
            fullname = str(cursor.fetchall())[3:-4]
            self.name_entry.insert('insert', fullname)
            cursor.execute("SELECT age FROM User WHERE username = ?", [username])
            age = str(cursor.fetchall()[0][0])
            self.age_entry.insert('insert', age)
            cursor.execute("SELECT nationality FROM User WHERE username = ?", [username])
            nationality = str(cursor.fetchall())[3:-4]
            self.nationality_entry.insert('insert', nationality)
            cursor.execute("SELECT email FROM User WHERE username = ?", [username])
            email = str(cursor.fetchall())[3:-4]
            self.email_entry.insert('insert', email)
            cursor.execute("SELECT github FROM User WHERE username = ?", [username])
            github = str(cursor.fetchall())[3:-4]
            self.github_entry.insert('insert', github)
            cursor.execute("SELECT linkedIn FROM User WHERE username = ?", [username])
            linkedIn = str(cursor.fetchall())[3:-4]
            self.linkedIn_entry.insert('insert', linkedIn)
            cursor.execute("SELECT field_study FROM User WHERE username = ?", [username])
            field_study = str(cursor.fetchall())[3:-4]
            self.specialize_entry.insert('insert', field_study)
            cursor.execute("SELECT years_in_field FROM User WHERE username = ?", [username])
            yrsField = str(cursor.fetchall()[0][0])
            self.fieldYrs_entry.insert('insert', yrsField)
            cursor.execute("SELECT meeting_mode FROM User WHERE username = ?", [username])
            meet_mode = str(cursor.fetchall())[3:-4]
            self.meetOpt.set(meet_mode)
            cursor.execute("SELECT meeting_region FROM User WHERE username = ?", [username])
            meet_region = str(cursor.fetchall())[3:-4]
            self.areaOpt.set(meet_region)
            cursor.execute("SELECT code_lang FROM User WHERE username = ?", [username])
            code_lang = str(cursor.fetchall())[3:-4]
            code_lang = code_lang.split(',')
            for x in code_lang:
                if x == '':
                    continue
                language_year = x[1:].split(" ")
                if language_year[0] == "Python":
                    self.check1.select()
                    self.proficient1.set(language_year[1])
                elif language_year[0] == "C++":
                    self.check2.select()
                    self.proficient2.set(language_year[1])
                elif language_year[0] == "C#":
                    self.check3.select()
                    self.proficient3.set(language_year[1])
                elif language_year[0] == "C":
                    self.check4.select()
                    self.proficient4.set(language_year[1])
                elif language_year[0] == "Java":
                    self.check5.select()
                    self.proficient5.set(language_year[1])
                elif language_year[0] == "Javascript":
                    self.check6.select()
                    self.proficient6.set(language_year[1])
                elif language_year[0] == "PHP":
                    self.check7.select()
                    self.proficient7.set(language_year[1])
                elif language_year[0] == "SQL":
                    self.check8.select()
                    self.proficient8.set(language_year[1])
                elif language_year[0] == "HTML":
                    self.check9.select()
                    self.proficient9.set(language_year[1])
                elif language_year[0] == "CSS":
                    self.check10.select()
                    self.proficient10.set(language_year[1])
            connection.close()
        self.get_details_btn = tk.Button(self, text='Get Current Profile Details', font='Bahnschrift 32 bold', bg='cyan', relief='solid', command=start_edits)

        #Proficiencies
        self.proficient_label = tk.Label(self, text='Proficient Languages', font='Bahnschrift 24 bold underline', bg='green')
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
        self.check1 = tk.Checkbutton(self, text='Python', font='Bahnschrift 16 bold', bg='green', bd=-2,
                                     variable=var1)
        self.experience2 = tk.OptionMenu(self, self.proficient2, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience2.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience2_menu = self.nametowidget(self.experience2.menuname)
        experience2_menu.configure(font='Bahnschrift 12 bold')
        self.check2 = tk.Checkbutton(self, text='C++', font='Bahnschrift 16 bold', bg='green', bd=-2, variable=var2)
        self.experience3 = tk.OptionMenu(self, self.proficient3, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience3.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience3_menu = self.nametowidget(self.experience3.menuname)
        experience3_menu.configure(font='Bahnschrift 12 bold')
        self.check3 = tk.Checkbutton(self, text='C#', font='Bahnschrift 16 bold', bg='green', bd=-2, variable=var3)
        self.experience4 = tk.OptionMenu(self, self.proficient4, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience4.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience4_menu = self.nametowidget(self.experience4.menuname)
        experience4_menu.configure(font='Bahnschrift 12 bold')
        self.check4 = tk.Checkbutton(self, text='C', font='Bahnschrift 16 bold', bg='green', bd=-2, variable=var4)
        self.experience5 = tk.OptionMenu(self, self.proficient5, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience5.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience5_menu = self.nametowidget(self.experience5.menuname)
        experience5_menu.configure(font='Bahnschrift 12 bold')
        self.check5 = tk.Checkbutton(self, text='Java', font='Bahnschrift 16 bold', bg='green', bd=-2, variable=var5)
        self.experience6 = tk.OptionMenu(self, self.proficient6, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience6.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience6_menu = self.nametowidget(self.experience6.menuname)
        experience6_menu.configure(font='Bahnschrift 12 bold')
        self.check6 = tk.Checkbutton(self, text='Javascript', font='Bahnschrift 16 bold', bg='green', bd=-2,
                                     variable=var6)
        self.experience7 = tk.OptionMenu(self, self.proficient7, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience7.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience7_menu = self.nametowidget(self.experience7.menuname)
        experience7_menu.configure(font='Bahnschrift 12 bold')
        self.check7 = tk.Checkbutton(self, text='PHP', font='Bahnschrift 16 bold', bg='green', bd=-2, variable=var7)
        self.experience8 = tk.OptionMenu(self, self.proficient8, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience8.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience8_menu = self.nametowidget(self.experience8.menuname)
        experience8_menu.configure(font='Bahnschrift 12 bold')
        self.check8 = tk.Checkbutton(self, text='SQL', font='Bahnschrift 16 bold', bg='green', bd=-2, variable=var8)
        self.experience9 = tk.OptionMenu(self, self.proficient9, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience9.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience9_menu = self.nametowidget(self.experience9.menuname)
        experience9_menu.configure(font='Bahnschrift 12 bold')
        self.check9 = tk.Checkbutton(self, text='HTML', font='Bahnschrift 16 bold', bg='green', bd=-2, variable=var9)
        self.experience10 = tk.OptionMenu(self, self.proficient10, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience10.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience10_menu = self.nametowidget(self.experience10.menuname)
        experience10_menu.configure(font='Bahnschrift 12 bold')
        self.check10 = tk.Checkbutton(self, text='CSS', font='Bahnschrift 16 bold', bg='green', bd=-2, variable=var10)
        self.error_label = tk.Label(self, text="",font='Bahnschrift 20 underline', bg='green', bd=3, fg='red')

        #This function collects the data in all the entry widgets and saves it to the overall user database
        def save_edits():
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            file = open("Databases/logs.txt", "r")
            username = file.read()
            file.close()
            username = username[:-1]
            shortDesc = self.user_desc.get("1.0", "end-1c")
            cursor.execute("UPDATE User SET short_Desc = ? WHERE username = ?", [shortDesc, username])
            connection.commit()
            email = self.email_entry.get()
            email = email.strip()
            if email == None or email == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            cursor.execute("UPDATE User SET email = ? WHERE username = ?", [email, username])
            connection.commit()
            fullname = self.name_entry.get()
            fullname = fullname.strip()
            if fullname == None or fullname == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            cursor.execute("UPDATE User SET fullname = ? WHERE username = ?", [fullname, username])
            connection.commit()
            age = self.age_entry.get()
            age = age.strip()
            if age == None or age == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            elif not age.isdigit():
                self.error_label['text'] = "Please ensure your age is an integer"
                return
            cursor.execute("UPDATE User SET age = ? WHERE username = ?", [age, username])
            connection.commit()
            nationality = self.nationality_entry.get()
            nationality = nationality.strip()
            if nationality == None or nationality == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            cursor.execute("UPDATE User SET nationality = ? WHERE username = ?", [nationality, username])
            connection.commit()
            github = self.github_entry.get()
            cursor.execute("UPDATE User SET github = ? WHERE username = ?", [github, username])
            connection.commit()
            linkedIn = self.linkedIn_entry.get()
            cursor.execute("UPDATE User SET linkedIn = ? WHERE username = ?", [linkedIn, username])
            connection.commit()
            specialization = self.specialize_entry.get()
            specialization = specialization.strip()
            if specialization == None or specialization == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            cursor.execute("UPDATE User SET field_study = ? WHERE username = ?", [specialization, username])
            connection.commit()
            years_field = self.fieldYrs_entry.get()
            years_field = years_field.strip()
            if years_field == None or years_field == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            elif not years_field.isdigit():
                self.error_label['text'] = "Please ensure your age is an integer"
                return
            cursor.execute("UPDATE User SET years_in_field = ? WHERE username = ?", [years_field, username])
            connection.commit()

            # coding knowledge
            count = 0
            coding_prof = ''
            print('var1:' + str(var1.get()))
            if var1.get() == 1:
                python = self.proficient1.get()
                if python == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Python ' + python
            if var2.get() == 1:
                c_plus = self.proficient2.get()
                if c_plus == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C++ ' + c_plus
            if var3.get() == 1:
                c_sharp = self.proficient3.get()
                if c_sharp == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C# ' + c_sharp
            if var4.get() == 1:
                c_only = self.proficient4.get()
                if c_only == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C ' + c_only
            if var5.get() == 1:
                java = self.proficient5.get()
                if java == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Java ' + java
            if var6.get() == 1:
                javascript = self.proficient6.get()
                if javascript == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Javascript ' + javascript
            if var7.get() == 1:
                php = self.proficient7.get()
                if php == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', PHP ' + php
            if var8.get() == 1:
                s_q_l = self.proficient8.get()
                if s_q_l == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', SQL ' + s_q_l
            if var9.get() == 1:
                html = self.proficient9.get()
                if html == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', HTML ' + html
            if var10.get() == 1:
                css = self.proficient10.get()
                if css == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', CSS ' + css
            if count != 0:
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            cursor.execute("UPDATE User SET code_lang = ? WHERE username = ?", [coding_prof, username])
            connection.commit()

            connection.close()
        self.save_details_btn = tk.Button(self, text='Save Edits', font='Bahnschrift 28 bold', bg='Red', relief='solid', command=save_edits)
        self.user_desc = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=25, height=15, font='Bahnschrift 16 bold')

        # arrange elements & widgets in grid
        self.space_label1.place(x=0, y=0)
        self.recs_btn.place(x=370, y=2)
        self.recs_btn.tkraise()
        self.search_btn.place(x=505, y=2)
        self.search_btn.tkraise()
        self.events_btn.place(x=640, y=2)
        self.events_btn.tkraise()
        self.contacts_btn.place(x=775, y=2)
        self.contacts_btn.tkraise()
        self.profile_btn.place(x=910, y=2)
        self.profile_btn.tkraise()
        self.get_details_btn.place(x=450, y=170)
        self.profile_pic_label.place(x=370, y=305)
        self.pic_btn.place(x=350, y=520)
        self.username_label.place(x=650, y=280)
        self.user_desc.place(x=650, y=380)
        self.save_details_btn.place(x=600, y=780)

        #Details
        self.name_label.place(x=130, y=300)
        self.name_entry.place(x=45, y=330)
        self.age_label.place(x=140, y=360)
        self.age_entry.place(x=45, y=390)
        self.nationality_label.place(x=110, y=420)
        self.nationality_entry.place(x=45, y=450)
        self.email_label.place(x=135, y=480)
        self.email_entry.place(x=45, y=510)
        self.github_label.place(x=35, y=540)
        self.github_entry.place(x=45, y=570)
        self.linkedIn_label.place(x=60, y=600)
        self.linkedIn_entry.place(x=45, y=630)
        self.specialize_label.place(x=35, y=660)
        self.specialize_entry.place(x=45, y=690)
        self.fieldYrs_label.place(x=65, y=720)
        self.fieldYrs_entry.place(x=45, y=750)
        self.meetPref.place(x=380, y=580)
        self.areaPref.place(x=380, y=620)

        #Proficiencies
        self.proficient_label.place(x=1020, y=315)
        self.experience1.place(x=1200, y=370)
        self.check1.place(x=1040, y=365)
        self.experience2.place(x=1200, y=410)
        self.check2.place(x=1040, y=408)
        self.experience3.place(x=1200, y=450)
        self.check3.place(x=1040, y=450)
        self.experience4.place(x=1200, y=490)
        self.check4.place(x=1040, y=488)
        self.experience5.place(x=1200, y=530)
        self.check5.place(x=1040, y=528)
        self.experience6.place(x=1200, y=570)
        self.check6.place(x=1040, y=568)
        self.experience7.place(x=1200, y=610)
        self.check7.place(x=1040, y=608)
        self.experience8.place(x=1200, y=650)
        self.check8.place(x=1040, y=648)
        self.experience9.place(x=1200, y=690)
        self.check9.place(x=1040, y=688)
        self.experience10.place(x=1200, y=730)
        self.check10.place(x=1040, y=728)
        self.error_label.place(x=830, y=800)