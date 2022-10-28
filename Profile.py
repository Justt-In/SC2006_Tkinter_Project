import tkinter as tk
import psycopg2
import customtkinter
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

class Profile_page(customtkinter.CTkFrame):
    #Initialises the Tkinter frame
    def __init__(self, parent, controller):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        if customtkinter.get_appearance_mode() == "light" or customtkinter.get_appearance_mode() == "Light":
            path = "images/toolbar_image2.jpg"
            main_bg = "#ffe5d9"
            toolbar_bg = "#e1edfb"
            accentColour = "#48CAE4"
            accentColour2 = "#E46248"
            accentColour3 = "#00b4d8"
            textColour = "black"
            backdrop1 = "images/backdropv3_1"
        else:
            path = "images/toolbar_image1.png"
            main_bg = "#464646"
            toolbar_bg = "#112938"
            accentColour = "#0077b6"
            accentColour2 = "#B63F00"
            accentColour3 = "#00b4d8"
            textColour = "black"
            backdrop1 = "images/backdropv3_3"
        customtkinter.CTkFrame.__init__(self, parent, fg_color=main_bg)
        self.controller = controller
        # Toolbar
        # Top Toolbar
        # Create Canvas
        canvas1 = tk.Canvas(self, width=400, height=250, bd=0, highlightthickness=0)
        canvas1.pack(fill="x", side='top')

        # Display image

        self.toolbarImg = Image.open(path)
        self.toolbarImg = ImageTk.PhotoImage(self.toolbarImg.resize((1930, 300), Image.ANTIALIAS))
        canvas1.create_image(0, 0, image=self.toolbarImg, anchor="nw")
        # Display image

        self.toolbarImg = Image.open(path)
        self.toolbarImg = ImageTk.PhotoImage(self.toolbarImg.resize((1930, 300), Image.ANTIALIAS))
        canvas1.create_image(0, 0, image=self.toolbarImg, anchor="nw")

        def goto_recs():
            self.username_label['text'] = "Username"
            self.name_entry.delete(0, 'end')
            self.age_entry.delete(0, 'end')
            self.nationality_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.github_entry.delete(0, 'end')
            self.linkedIn_entry.delete(0, 'end')
            self.specialize_entry.delete(0, 'end')
            self.fieldYrs_entry.delete(0, 'end')
            if var1.get() == 1:
                self.switch1.deselect()
                self.experience1.set("Experience")
            if var2.get() == 1:
                self.switch2.deselect()
                self.experience2.set("Experience")
            if var3.get() == 1:
                self.switch3.deselect()
                self.experience3.set("Experience")
            if var4.get() == 1:
                self.switch4.deselect()
                self.experience4.set("Experience")
            if var5.get() == 1:
                self.switch5.deselect()
                self.experience5.set("Experience")
            if var6.get() == 1:
                self.switch6.deselect()
                self.experience6.set("Experience")
            if var7.get() == 1:
                self.switch7.deselect()
                self.experience7.set("Experience")
            if var8.get() == 1:
                self.switch8.deselect()
                self.experience8.set("Experience")
            if var9.get() == 1:
                self.switch9.deselect()
                self.experience9.set("Experience")
            if var10.get() == 1:
                self.switch10.deselect()
                self.experience10.set("Experience")
            self.experience1.set("Experience")
            self.experience2.set("Experience")
            self.experience3.set("Experience")
            self.experience4.set("Experience")
            self.experience5.set("Experience")
            self.experience6.set("Experience")
            self.experience7.set("Experience")
            self.experience8.set("Experience")
            self.experience9.set("Experience")
            self.experience10.set("Experience")
            self.profile_pic_label.configure(image=self.default_pic)
            self.meet_pref_dd.set("Meeting Preference")
            self.locale_pref_dd.set("Preferred Area")
            self.user_desc.delete('1.0', 'end')
            self.error_label['text'] = ""
            controller.show_frame("Recs_page")
        self.recs_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Recommendations',
                                                text_color=textColour,
                                                text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                command=goto_recs)
        def goto_search():
            self.username_label['text'] = "Username"
            self.name_entry.delete(0, 'end')
            self.age_entry.delete(0, 'end')
            self.nationality_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.github_entry.delete(0, 'end')
            self.linkedIn_entry.delete(0, 'end')
            self.specialize_entry.delete(0, 'end')
            self.fieldYrs_entry.delete(0, 'end')
            if var1.get() == 1:
                self.switch1.deselect()
                self.experience1.set("Experience")
            if var2.get() == 1:
                self.switch2.deselect()
                self.experience2.set("Experience")
            if var3.get() == 1:
                self.switch3.deselect()
                self.experience3.set("Experience")
            if var4.get() == 1:
                self.switch4.deselect()
                self.experience4.set("Experience")
            if var5.get() == 1:
                self.switch5.deselect()
                self.experience5.set("Experience")
            if var6.get() == 1:
                self.switch6.deselect()
                self.experience6.set("Experience")
            if var7.get() == 1:
                self.switch7.deselect()
                self.experience7.set("Experience")
            if var8.get() == 1:
                self.switch8.deselect()
                self.experience8.set("Experience")
            if var9.get() == 1:
                self.switch9.deselect()
                self.experience9.set("Experience")
            if var10.get() == 1:
                self.switch10.deselect()
                self.experience10.set("Experience")
            self.experience1.set("Experience")
            self.experience2.set("Experience")
            self.experience3.set("Experience")
            self.experience4.set("Experience")
            self.experience5.set("Experience")
            self.experience6.set("Experience")
            self.experience7.set("Experience")
            self.experience8.set("Experience")
            self.experience9.set("Experience")
            self.experience10.set("Experience")
            self.profile_pic_label.configure(image=self.default_pic)
            self.meet_pref_dd.set("Meeting Preference")
            self.locale_pref_dd.set("Preferred Area")
            self.user_desc.delete('1.0', 'end')
            self.error_label['text'] = ""
            controller.show_frame("Search_page")
        self.search_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Search Users', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                  command=goto_search)

        def goto_events():
            self.username_label['text'] = "Username"
            self.name_entry.delete(0, 'end')
            self.age_entry.delete(0, 'end')
            self.nationality_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.github_entry.delete(0, 'end')
            self.linkedIn_entry.delete(0, 'end')
            self.specialize_entry.delete(0, 'end')
            self.fieldYrs_entry.delete(0, 'end')
            if var1.get() == 1:
                self.switch1.deselect()
                self.experience1.set("Experience")
            if var2.get() == 1:
                self.switch2.deselect()
                self.experience2.set("Experience")
            if var3.get() == 1:
                self.switch3.deselect()
                self.experience3.set("Experience")
            if var4.get() == 1:
                self.switch4.deselect()
                self.experience4.set("Experience")
            if var5.get() == 1:
                self.switch5.deselect()
                self.experience5.set("Experience")
            if var6.get() == 1:
                self.switch6.deselect()
                self.experience6.set("Experience")
            if var7.get() == 1:
                self.switch7.deselect()
                self.experience7.set("Experience")
            if var8.get() == 1:
                self.switch8.deselect()
                self.experience8.set("Experience")
            if var9.get() == 1:
                self.switch9.deselect()
                self.experience9.set("Experience")
            if var10.get() == 1:
                self.switch10.deselect()
                self.experience10.set("Experience")
            self.experience1.set("Experience")
            self.experience2.set("Experience")
            self.experience3.set("Experience")
            self.experience4.set("Experience")
            self.experience5.set("Experience")
            self.experience6.set("Experience")
            self.experience7.set("Experience")
            self.experience8.set("Experience")
            self.experience9.set("Experience")
            self.experience10.set("Experience")
            self.profile_pic_label.configure(image=self.default_pic)
            self.meet_pref_dd.set("Meeting Preference")
            self.locale_pref_dd.set("Preferred Area")
            self.user_desc.delete('1.0', 'end')
            self.error_label['text'] = ""
            controller.show_frame("Events_page")
        self.events_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='View Events', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                  command=goto_events)
        def goto_contacts():
            self.username_label['text'] = "Username"
            self.name_entry.delete(0, 'end')
            self.age_entry.delete(0, 'end')
            self.nationality_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.github_entry.delete(0, 'end')
            self.linkedIn_entry.delete(0, 'end')
            self.specialize_entry.delete(0, 'end')
            self.fieldYrs_entry.delete(0, 'end')
            if var1.get() == 1:
                self.switch1.deselect()
                self.experience1.set("Experience")
            if var2.get() == 1:
                self.switch2.deselect()
                self.experience2.set("Experience")
            if var3.get() == 1:
                self.switch3.deselect()
                self.experience3.set("Experience")
            if var4.get() == 1:
                self.switch4.deselect()
                self.experience4.set("Experience")
            if var5.get() == 1:
                self.switch5.deselect()
                self.experience5.set("Experience")
            if var6.get() == 1:
                self.switch6.deselect()
                self.experience6.set("Experience")
            if var7.get() == 1:
                self.switch7.deselect()
                self.experience7.set("Experience")
            if var8.get() == 1:
                self.switch8.deselect()
                self.experience8.set("Experience")
            if var9.get() == 1:
                self.switch9.deselect()
                self.experience9.set("Experience")
            if var10.get() == 1:
                self.switch10.deselect()
                self.experience10.set("Experience")
            self.experience1.set("Experience")
            self.experience2.set("Experience")
            self.experience3.set("Experience")
            self.experience4.set("Experience")
            self.experience5.set("Experience")
            self.experience6.set("Experience")
            self.experience7.set("Experience")
            self.experience8.set("Experience")
            self.experience9.set("Experience")
            self.experience10.set("Experience")
            self.profile_pic_label.configure(image=self.default_pic)
            self.meet_pref_dd.set("Meeting Preference")
            self.locale_pref_dd.set("Preferred Area")
            self.user_desc.delete('1.0', 'end')
            self.error_label['text'] = ""
            controller.show_frame("Contacts_page")
        self.contacts_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='My Contacts',
                                                    text_color=textColour,
                                                    text_font=['trebuchet MS bold', 12], height=30,
                                                    fg_color=accentColour,
                                                    command=goto_contacts)
        def goto_profile():
            self.username_label['text'] = "Username"
            self.name_entry.delete(0, 'end')
            self.age_entry.delete(0, 'end')
            self.nationality_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.github_entry.delete(0, 'end')
            self.linkedIn_entry.delete(0, 'end')
            self.specialize_entry.delete(0, 'end')
            self.fieldYrs_entry.delete(0, 'end')
            if var1.get() == 1:
                self.switch1.deselect()
                self.experience1.set("Experience")
            if var2.get() == 1:
                self.switch2.deselect()
                self.experience2.set("Experience")
            if var3.get() == 1:
                self.switch3.deselect()
                self.experience3.set("Experience")
            if var4.get() == 1:
                self.switch4.deselect()
                self.experience4.set("Experience")
            if var5.get() == 1:
                self.switch5.deselect()
                self.experience5.set("Experience")
            if var6.get() == 1:
                self.switch6.deselect()
                self.experience6.set("Experience")
            if var7.get() == 1:
                self.switch7.deselect()
                self.experience7.set("Experience")
            if var8.get() == 1:
                self.switch8.deselect()
                self.experience8.set("Experience")
            if var9.get() == 1:
                self.switch9.deselect()
                self.experience9.set("Experience")
            if var10.get() == 1:
                self.switch10.deselect()
                self.experience10.set("Experience")
            self.experience1.set("Experience")
            self.experience2.set("Experience")
            self.experience3.set("Experience")
            self.experience4.set("Experience")
            self.experience5.set("Experience")
            self.experience6.set("Experience")
            self.experience7.set("Experience")
            self.experience8.set("Experience")
            self.experience9.set("Experience")
            self.experience10.set("Experience")
            self.profile_pic_label.configure(image=self.default_pic)
            self.meet_pref_dd.set("Meeting Preference")
            self.locale_pref_dd.set("Preferred Area")
            self.user_desc.delete('1.0', 'end')
            self.error_label['text'] = ""
            controller.show_frame("Profile_page")
        self.profile_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='My Profile', text_color=textColour,
                                                   text_font=['trebuchet MS bold', 12], height=30,
                                                   fg_color=accentColour2,
                                                   command=goto_profile)
        # End of Toolbar

        def reset_page():
            self.username_label['text'] = "Username"
            self.name_entry.delete(0, 'end')
            self.name_entry.configure(state="normal")
            self.age_entry.delete(0, 'end')
            self.age_entry.configure(state="normal")
            self.nationality_entry.delete(0, 'end')
            self.nationality_entry.configure(state="normal")
            self.email_entry.delete(0, 'end')
            self.email_entry.configure(state="normal")
            self.github_entry.delete(0, 'end')
            self.github_entry.configure(state="normal")
            self.linkedIn_entry.delete(0, 'end')
            self.linkedIn_entry.configure(state="normal")
            self.specialize_entry.delete(0, 'end')
            self.specialize_entry.configure(state="normal")
            self.fieldYrs_entry.delete(0, 'end')
            self.fieldYrs_entry.configure(state="normal")
            if var1.get() == 1:
                self.switch1.deselect()
                self.experience1.set("Experience")
            if var2.get() == 1:
                self.switch2.deselect()
                self.experience2.set("Experience")
            if var3.get() == 1:
                self.switch3.deselect()
                self.experience3.set("Experience")
            if var4.get() == 1:
                self.switch4.deselect()
                self.experience4.set("Experience")
            if var5.get() == 1:
                self.switch5.deselect()
                self.experience5.set("Experience")
            if var6.get() == 1:
                self.switch6.deselect()
                self.experience6.set("Experience")
            if var7.get() == 1:
                self.switch7.deselect()
                self.experience7.set("Experience")
            if var8.get() == 1:
                self.switch8.deselect()
                self.experience8.set("Experience")
            if var9.get() == 1:
                self.switch9.deselect()
                self.experience9.set("Experience")
            if var10.get() == 1:
                self.switch10.deselect()
                self.experience10.set("Experience")
            self.experience1.set("Experience")
            self.experience2.set("Experience")
            self.experience3.set("Experience")
            self.experience4.set("Experience")
            self.experience5.set("Experience")
            self.experience6.set("Experience")
            self.experience7.set("Experience")
            self.experience8.set("Experience")
            self.experience9.set("Experience")
            self.experience10.set("Experience")
            self.profile_pic_label.configure(image=self.default_pic)
            self.meet_pref_dd.set("Meeting Preference")
            self.locale_pref_dd.set("Preferred Area")
            self.user_desc.delete('1.0', 'end')
            self.error_label['text'] = ""

        #Create elements & widgets
        self.name_label = tk.Label(self, text='Name', font='Bahnschrift 16 bold', bg=main_bg)
        self.name_entry = tk.Entry(self, font='Bahnschrift 16')

        self.email_label = tk.Label(self, text='Email', font='Bahnschrift 16 bold', bg=main_bg)
        self.email_entry = tk.Entry(self, font='Bahnschrift 16')

        self.nationality_label = tk.Label(self, text='Nationality', font='Bahnschrift 16 bold', bg=main_bg)
        self.nationality_entry = tk.Entry(self, font='Bahnschrift 16')

        self.meet_pref_dd = customtkinter.CTkOptionMenu(self, values=["Virtual", "Physical", "None"])
        self.meet_pref_dd.set("Meeting Preference")
        self.meet_pref_dd.configure(text_font='Bahnschrift 16 bold', bg_color=main_bg, fg_color=accentColour,
                                    text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                    dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 16 bold',
                                    width=190)

        self.locale_pref_dd = customtkinter.CTkOptionMenu(self, values=["Central SG", "North SG", "East SG", "South SG",
                                                                        "West SG"])
        self.locale_pref_dd.set("Preferred Area")
        self.locale_pref_dd.configure(text_font='Bahnschrift 16 bold', bg_color=main_bg, fg_color=accentColour,
                                      text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                      dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 16 bold',
                                      width=190)

        self.github_label = tk.Label(self, text='Github Username (Optional)', font='Bahnschrift 16 bold', bg=main_bg)
        self.github_entry = tk.Entry(self, font='Bahnschrift 16')
        self.linkedIn_label = tk.Label(self, text='LinkedIn Url (Optional)', font='Bahnschrift 16 bold', bg=main_bg)
        self.linkedIn_entry = tk.Entry(self, font='Bahnschrift 16')
        self.age_label = tk.Label(self, text='Age', font='Bahnschrift 16 bold', bg=main_bg)
        self.age_entry = tk.Entry(self, font='Bahnschrift 16')
        self.specialize_label = tk.Label(self, text='Specialization/Field of study', font='Bahnschrift 16 bold', bg=main_bg)
        self.specialize_entry = tk.Entry(self, font='Bahnschrift 16')
        self.fieldYrs_label = tk.Label(self, text='Years in Specialization', font='Bahnschrift 16 bold', bg=main_bg)
        self.fieldYrs_entry = tk.Entry(self, font='Bahnschrift 16')
        self.load_profile_pic = Image.open('images/default_profile_img.png')
        self.default_pic = ImageTk.PhotoImage(self.load_profile_pic.resize((200, 200), Image.ANTIALIAS))
        self.profile_pic_label = tk.Label(self, image=self.default_pic, bg=main_bg)

        #This function allows the user to change their profile picture and updates dynamically upon update, it also
        # saves the image to the database immediately
        def change_pic():
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            file = open("Databases/logs.txt", "r")
            username = file.read()
            file.close()
            username = username[:-1]
            hCursor.execute("SELECT profile_pic FROM Users WHERE username = %s", [username])
            file_path = str(hCursor.fetchall())[3:-4]
            filename = filedialog.askopenfilename(initialdir="C:\\", filetypes=(
            ("PNG file", "*.png"), ("JPEG File", "*.jpeg"), ("JPG File", "*.jpg"), ("All File Types", "*.*")))
            if filename == None or filename == '':
                filename = file_path
            hCursor.execute("UPDATE Users SET profile_pic = %s WHERE username = %s", [filename, username])
            hConn.commit()
            hConn.close()
            #stgImg = ImageTk.PhotoImage(file=filename)
            self.load_prof_image = Image.open(filename)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((200, 200), Image.ANTIALIAS))
            self.profile_pic_label.configure(image=self.prof_image)
            self.profile_pic_label.image = self.prof_image

        submit_img = Image.open("images/submit_icon.png")
        submit_img = ImageTk.PhotoImage(submit_img.resize((50, 50), Image.ANTIALIAS))
        self.pic_btn = customtkinter.CTkButton(self, text='Change Picture', width=20, height=1, text_color=textColour,
                                               text_font=['trebuchet MS bold', 16], bg_color=main_bg, image=submit_img,
                                               fg_color=accentColour, command=change_pic)
        self.username_label = tk.Label(self, text='Username', font='Bahnschrift 30 underline bold', bg=main_bg)

        #This function gets the data of the logged in user from the database and displays his/her details on screen
        def start_edits():
            reset_page()
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            file = open("Databases/logs.txt", "r")
            username = file.read()
            file.close()
            username = username[:-1]
            self.username_label["text"] = username
            hCursor.execute("SELECT profile_pic FROM Users WHERE username = %s", [username])
            file_path = str(hCursor.fetchall())[3:-4]
            print(file_path)
            #file_path = "images/" + file_path[25:]
            img2 = ImageTk.PhotoImage(Image.open(file_path))
            self.profile_pic_label.configure(image=img2)
            self.profile_pic_label.image = img2
            hCursor.execute("SELECT short_Desc FROM Users WHERE username = %s", [username])
            for line in hCursor.fetchall()[0]:
                if line == None:
                    continue
                else:
                    self.user_desc.insert('insert', line)
            hCursor.execute("SELECT fullname FROM Users WHERE username = %s", [username])
            fullname = str(hCursor.fetchall())[3:-4]
            self.name_entry.insert('insert', fullname)
            hCursor.execute("SELECT age FROM Users WHERE username = %s", [username])
            age = str(hCursor.fetchall()[0][0])
            self.age_entry.insert('insert', age)
            hCursor.execute("SELECT nationality FROM Users WHERE username = %s", [username])
            nationality = str(hCursor.fetchall())[3:-4]
            self.nationality_entry.insert('insert', nationality)
            hCursor.execute("SELECT email FROM Users WHERE username = %s", [username])
            email = str(hCursor.fetchall())[3:-4]
            self.email_entry.insert('insert', email)
            hCursor.execute("SELECT github FROM Users WHERE username = %s", [username])
            github = str(hCursor.fetchall())[3:-4]
            self.github_entry.insert('insert', github)
            hCursor.execute("SELECT linkedIn FROM Users WHERE username = %s", [username])
            linkedIn = str(hCursor.fetchall())[3:-4]
            self.linkedIn_entry.insert('insert', linkedIn)
            hCursor.execute("SELECT field_study FROM Users WHERE username = %s", [username])
            field_study = str(hCursor.fetchall())[3:-4]
            self.specialize_entry.insert('insert', field_study)
            hCursor.execute("SELECT years_in_field FROM Users WHERE username = %s", [username])
            yrsField = str(hCursor.fetchall()[0][0])
            self.fieldYrs_entry.insert('insert', yrsField)
            hCursor.execute("SELECT meeting_mode FROM Users WHERE username = %s", [username])
            meet_mode = str(hCursor.fetchall())[3:-4]
            self.meet_pref_dd.set(meet_mode)
            hCursor.execute("SELECT meeting_region FROM Users WHERE username = %s", [username])
            meet_region = str(hCursor.fetchall())[3:-4]
            self.locale_pref_dd.set(meet_region)
            hCursor.execute("SELECT code_lang FROM Users WHERE username = %s", [username])
            code_lang = str(hCursor.fetchall())[3:-4]
            code_lang = code_lang.split(',')
            for x in code_lang:
                if x == '':
                    continue
                language_year = x[1:].split(" ")
                if language_year[0] == "Python":
                    self.switch1.select()
                    self.experience1.set(language_year[1])
                elif language_year[0] == "C++":
                    self.switch2.select()
                    self.experience2.set(language_year[1])
                elif language_year[0] == "C#":
                    self.switch3.select()
                    self.experience3.set(language_year[1])
                elif language_year[0] == "C":
                    self.switch4.select()
                    self.experience4.set(language_year[1])
                elif language_year[0] == "Java":
                    self.switch5.select()
                    self.experience5.set(language_year[1])
                elif language_year[0] == "Javascript":
                    self.switch6.select()
                    self.experience6.set(language_year[1])
                elif language_year[0] == "PHP":
                    self.switch7.select()
                    self.experience7.set(language_year[1])
                elif language_year[0] == "SQL":
                    self.switch8.select()
                    self.experience8.set(language_year[1])
                elif language_year[0] == "HTML":
                    self.switch9.select()
                    self.experience9.set(language_year[1])
                elif language_year[0] == "CSS":
                    self.switch10.select()
                    self.experience10.set(language_year[1])
            hConn.close()
        self.get_details_btn = customtkinter.CTkButton(self, text='Get Current Profile Details', text_color=textColour,
                                                       text_font=['trebuchet MS bold', 32], bg_color=main_bg,
                                                       fg_color="#0d9c8c", command=start_edits)

        #Proficiencies
        self.proficient_label = customtkinter.CTkLabel(self, text='Proficient Languages', text_color=textColour,
                                                       text_font=['trebuchet MS bold', 20], bg_color=main_bg)
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
        self.experience1.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)
        self.switch1 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var1, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel1 = customtkinter.CTkLabel(self, text='Python', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience2 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience2.set("Experience")
        self.experience2.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch2 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var2, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel2 = customtkinter.CTkLabel(self, text='C++', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience3 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience3.set("Experience")
        self.experience3.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch3 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var3, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel3 = customtkinter.CTkLabel(self, text='C#', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience4 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience4.set("Experience")
        self.experience4.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch4 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var4, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel4 = customtkinter.CTkLabel(self, text='C', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience5 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience5.set("Experience")
        self.experience5.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch5 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var5, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel5 = customtkinter.CTkLabel(self, text='Java', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience6 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience6.set("Experience")
        self.experience6.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch6 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var6, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel6 = customtkinter.CTkLabel(self, text='Javascript', text_font='Bahnschrift 12 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience7 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience7.set("Experience")
        self.experience7.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch7 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var7, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel7 = customtkinter.CTkLabel(self, text='PHP', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience8 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience8.set("Experience")
        self.experience8.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch8 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var8, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel8 = customtkinter.CTkLabel(self, text='SQL', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience9 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience9.set("Experience")
        self.experience9.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                   text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch9 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var9, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel9 = customtkinter.CTkLabel(self, text='HTML', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience10 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience10.set("Experience")
        self.experience10.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                    text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                    dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                    width=100)

        self.switch10 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var10, fg_color='red',
                                                progress_color='#2BD447')
        self.switchLabel10 = customtkinter.CTkLabel(self, text='CSS', text_font='Bahnschrift 14 bold',
                                                    bg_color=main_bg, text_color=textColour)
        self.error_label = tk.Label(self, text="",font='Bahnschrift 20 underline', bg=main_bg, bd=3, fg='#a00000')

        #This function collects the data in all the entry widgets and saves it to the overall user database
        def save_edits():
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com",
                                         database="ddipmu7if1umsi",
                                         user="wfpsdpcxvibamf",
                                         password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                         port="5432")
            hCursor = hConn.cursor()
            file = open("Databases/logs.txt", "r")
            username = file.read()
            file.close()
            username = username[:-1]
            shortDesc = self.user_desc.get("1.0", "end-1c")
            hCursor.execute("UPDATE Users SET short_Desc = %s WHERE username = %s", [shortDesc, username])
            hConn.commit()
            email = self.email_entry.get()
            email = email.strip()
            if email == None or email == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            hCursor.execute("UPDATE Users SET email = %s WHERE username = %s", [email, username])
            hConn.commit()
            fullname = self.name_entry.get()
            fullname = fullname.strip()
            if fullname == None or fullname == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            hCursor.execute("UPDATE Users SET fullname = %s WHERE username = %s", [fullname, username])
            hConn.commit()
            age = self.age_entry.get()
            age = age.strip()
            if age == None or age == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            elif not age.isdigit():
                self.error_label['text'] = "Please ensure your age is an integer"
                return
            hCursor.execute("UPDATE Users SET age = %s WHERE username = %s", [age, username])
            hConn.commit()
            nationality = self.nationality_entry.get()
            nationality = nationality.strip()
            if nationality == None or nationality == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            hCursor.execute("UPDATE Users SET nationality = %s WHERE username = %s", [nationality, username])
            hConn.commit()
            github = self.github_entry.get()
            hCursor.execute("UPDATE Users SET github = %s WHERE username = %s", [github, username])
            hConn.commit()
            linkedIn = self.linkedIn_entry.get()
            hCursor.execute("UPDATE Users SET linkedIn = %s WHERE username = %s", [linkedIn, username])
            hConn.commit()
            specialization = self.specialize_entry.get()
            specialization = specialization.strip()
            if specialization == None or specialization == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            hCursor.execute("UPDATE Users SET field_study = %s WHERE username = %s", [specialization, username])
            hConn.commit()
            years_field = self.fieldYrs_entry.get()
            years_field = years_field.strip()
            if years_field == None or years_field == '':
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            elif not years_field.isdigit():
                self.error_label['text'] = "Please ensure your age is an integer"
                return
            hCursor.execute("UPDATE Users SET years_in_field = %s WHERE username = %s", [years_field, username])
            hConn.commit()

            # coding knowledge
            count = 0
            coding_prof = ''
            print('var1:' + str(var1.get()))
            if var1.get() == 1:
                python = self.experience1.get()
                if python == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Python ' + python
            if var2.get() == 1:
                c_plus = self.experience2.get()
                if c_plus == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C++ ' + c_plus
            if var3.get() == 1:
                c_sharp = self.experience3.get()
                if c_sharp == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C# ' + c_sharp
            if var4.get() == 1:
                c_only = self.experience4.get()
                if c_only == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C ' + c_only
            if var5.get() == 1:
                java = self.experience5.get()
                if java == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Java ' + java
            if var6.get() == 1:
                javascript = self.experience6.get()
                if javascript == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Javascript ' + javascript
            if var7.get() == 1:
                php = self.experience7.get()
                if php == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', PHP ' + php
            if var8.get() == 1:
                s_q_l = self.experience8.get()
                if s_q_l == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', SQL ' + s_q_l
            if var9.get() == 1:
                html = self.experience9.get()
                if html == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', HTML ' + html
            if var10.get() == 1:
                css = self.experience10.get()
                if css == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', CSS ' + css
            if count != 0:
                self.error_label['text'] = "Please check that all required fields are filled"
                return
            hCursor.execute("UPDATE Users SET code_lang = %s WHERE username = %s", [coding_prof, username])
            self.error_label['text'] = ""
            tk.messagebox.showinfo("Success", "Edits saved successfully!")
            hConn.commit()
            hConn.close()
        self.save_details_btn = customtkinter.CTkButton(self, text='Save Edits', text_font=['trebuchet MS bold',28],
                                                        text_color=textColour, bg_color=main_bg, fg_color='red',
                                                        command=save_edits)
        self.user_desc = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=25, height=6, font='Bahnschrift 16 bold')

        # arrange elements & widgets in grid
        self.recs_btn.place(x=2, y=2)
        self.search_btn.place(x=158, y=2)
        self.events_btn.place(x=300, y=2)
        self.contacts_btn.place(x=442, y=2)
        self.profile_btn.place(x=584, y=2)

        self.get_details_btn.place(x=360, y=185)
        self.profile_pic_label.place(x=580, y=400)
        self.pic_btn.place(x=350, y=415)

        self.username_label.place(x=1000, y=370)
        self.user_desc.place(x=900, y=450)
        self.save_details_btn.place(x=550, y=660)

        #Details
        self.meet_pref_dd.place(x=600, y=470)
        self.locale_pref_dd.place(x=350, y=470)
        self.name_label.place(x=670, y=770)
        self.name_entry.place(x=530, y=820)
        self.age_label.place(x=1150, y=770)
        self.age_entry.place(x=1000, y=820)
        self.email_label.place(x=670, y=870)
        self.email_entry.place(x=530, y=920)
        self.nationality_label.place(x=1110, y=870)
        self.nationality_entry.place(x=1000, y=920)


        self.github_label.place(x=35, y=570)
        self.github_entry.place(x=50, y=620)
        self.linkedIn_label.place(x=70, y=670)
        self.linkedIn_entry.place(x=50, y=720)
        self.specialize_label.place(x=30, y=770)
        self.specialize_entry.place(x=50, y=820)
        self.fieldYrs_label.place(x=65, y=870)
        self.fieldYrs_entry.place(x=50, y=920)

        #Proficiencies
        self.proficient_label.place(x=980, y=260)
        self.experience1.place(x=1110, y=310)
        self.experience1.tkraise()
        self.switchLabel1.place(x=990, y=310)
        self.switch1.place(x=980, y=315)
        self.switch1.tkraise()
        self.experience2.place(x=1110, y=350)
        self.experience2.tkraise()
        self.switchLabel2.place(x=980, y=350)
        self.switch2.place(x=980, y=355)
        self.switch2.tkraise()
        self.experience3.place(x=1110, y=390)
        self.experience3.tkraise()
        self.switchLabel3.place(x=975, y=390)
        self.switch3.place(x=980, y=395)
        self.switch3.tkraise()
        self.experience4.place(x=1110, y=430)
        self.experience4.tkraise()
        self.switchLabel4.place(x=980, y=430)
        self.switch4.place(x=980, y=435)
        self.switch4.tkraise()
        self.experience5.place(x=1110, y=470)
        self.experience5.tkraise()
        self.switchLabel5.place(x=980, y=470)
        self.switch5.place(x=980, y=475)
        self.switch5.tkraise()
        self.experience6.place(x=1110, y=510)
        self.experience6.tkraise()
        self.switchLabel6.place(x=990, y=510)
        self.switch6.place(x=980, y=515)
        self.switch6.tkraise()
        self.experience7.place(x=1110, y=550)
        self.experience7.tkraise()
        self.switchLabel7.place(x=980, y=550)
        self.switch7.place(x=980, y=555)
        self.switch7.tkraise()
        self.experience8.place(x=1110, y=590)
        self.experience8.tkraise()
        self.switchLabel8.place(x=980, y=590)
        self.switch8.place(x=980, y=595)
        self.switch8.tkraise()
        self.experience9.place(x=1110, y=630)
        self.experience9.tkraise()
        self.switchLabel9.place(x=980, y=630)
        self.switch9.place(x=980, y=635)
        self.switch9.tkraise()
        self.experience10.place(x=1110, y=670)
        self.experience10.tkraise()
        self.switchLabel10.place(x=980, y=670)
        self.switch10.place(x=980, y=675)
        self.switch10.tkraise()