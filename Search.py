import tkinter as tk
import psycopg2
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import customtkinter
import sqlite3

class Search_page(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        """
        Initialize parent class

        This function will initialize the parent class allowing for subclasses to be built on top of this class
        :return: parent class
        """
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
        else:
            path = "images/toolbar_image1.png"
            main_bg = "#464646"
            toolbar_bg = "#112938"
            accentColour = "#0077b6"
            accentColour2 = "#B63F00"
            accentColour3 = "#00b4d8"
            textColour = "black"
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
        self.recs_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Recommendations',
                                                text_color=textColour,
                                                text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                command=lambda: controller.show_frame("Recs_page"))
        self.search_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Search Users', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour2,
                                                  command=lambda: controller.show_frame("Search_page"))
        self.events_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='View Events', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                  command=lambda: controller.show_frame("Events_page"))
        self.contacts_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='My Contacts',
                                                    text_color=textColour,
                                                    text_font=['trebuchet MS bold', 12], height=30,
                                                    fg_color=accentColour,
                                                    command=lambda: controller.show_frame("Contacts_page"))
        self.profile_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='My Profile', text_color=textColour,
                                                   text_font=['trebuchet MS bold', 12], height=30,
                                                   fg_color=accentColour,
                                                   command=lambda: controller.show_frame("Profile_page"))
        # End of Toolbar

        #add elemets & widgets
        self.user_label = customtkinter.CTkLabel(self, text='Looking For Someone?', text_font=['trebuchet MS bold', 40],
                                                 corner_radius=20,bg_color=main_bg, fg_color=accentColour, text_color=textColour)

        self.search_user = customtkinter.CTkEntry(self, text_font=['arial', 18], width=400,height=40 , bg_color=main_bg,
                                                  text_color=textColour, fg_color='white')
        #self.search_user.pack(ipady=18)
        self.label_block = tk.Label(self, bg=main_bg, width=500, height=300)
        self.success_label = tk.Label(self, bg=main_bg,fg='#34B88A', text='', font='Bahnschrift 18 bold ')
        self.fail_label = tk.Label(self,bg=main_bg, fg='red', text='', font='Bahnschrift 18 bold ')
        #Gets the username entered into the the search bar and finds that user, returns appropriate messages if no user
        # is found and returns the found user if there exists one
        def search_user():
            """
            Searches database for inputted username, returns Error message if no user found or user searches themselves
            , displays user's data if username is found
            :return: Displays error message or user's data
            """
            search_username = self.search_user.get()
            file = open("Databases/logs.txt", "r").read()[:-1]
            if search_username == file:
                self.fail_label['text'] = "You are not allowed to send a proggy request to yourself!"
                self.fail_label.place(x=500, y=450)
                self.fail_label.tkraise()
                return
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            hCursor.execute("SELECT profile_pic, username, short_Desc, field_study, code_lang, meeting_mode FROM Users WHERE username = %s", [search_username])
            details = hCursor.fetchall()
            print(details)
            try:
                profile_pic = details[0][0]
                if profile_pic != None:
                    load_profile_pic = Image.open(profile_pic)
                    default_pic = ImageTk.PhotoImage(load_profile_pic.resize((130, 130), Image.ANTIALIAS))
                    self.randomuser1_img.configure(image=default_pic)
                    self.randomuser1_img.image = default_pic
                search_username = details[0][1]
                self.randomuser1_username.configure(text=search_username)
                short_desc = details[0][2]
                self.randomuser1_desc.configure(text="Short Description: \n" + short_desc)
                field_study = details[0][3]
                self.randomuser1_study.configure(text="Work/Study Field: " + field_study)
                meeting_mode = details[0][5]
                self.randomuser1_meeting.configure(text="Meeting Preference: " + meeting_mode)
                code_lang = details[0][4]
                code_lang = code_lang.split(',')
                code_text = '\n'.join(code_lang[1:])
                self.randomuser1_code.configure(text="Coding Experience: \n" + code_text)
                self.fail_label['text'] = ""
                self.label_block.lower()
            except IndexError:
                self.fail_label['text'] = "No user found, please check your input once more"
                self.fail_label.place(x=550, y=450)
                self.fail_label.tkraise()

        search_icon = Image.open("images/search_icon.png")
        search_icon = ImageTk.PhotoImage(search_icon.resize((70, 70), Image.ANTIALIAS))
        self.usersearch_button = customtkinter.CTkButton(self, text="", bg_color=main_bg, fg_color=accentColour3,
                                                         image=search_icon, width=30, corner_radius=20, command=search_user)
        self.rect_label_1 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, height=350, width=600,
                                                   corner_radius=20, text="")
        self.load_randomuser1_img = tk.PhotoImage(file='images/profile_icon.png')
        self.randomuser1_img = customtkinter.CTkLabel(self, image=self.load_randomuser1_img, bg_color=accentColour,
                                                      fg_color=accentColour2)
        self.randomuser1_username = customtkinter.CTkLabel(self, text='Username', text_font=['trebuchet MS bold', 30],
                                                           bg_color=accentColour, text_color=textColour)
        self.randomuser1_desc = customtkinter.CTkLabel(self, text='Experience Description...', text_font=['Bahnschrift bold', 14],
                                                       bg_color=accentColour, text_color=textColour)
        self.randomuser1_study = customtkinter.CTkLabel(self, text='Field of study...',
                                                       text_font=['Bahnschrift bold', 14],
                                                       bg_color=accentColour, text_color=textColour)
        self.randomuser1_code = customtkinter.CTkLabel(self, text='Coding\nLanguages\nOf\nUser',
                                                       text_font=['Bahnschrift bold', 14],
                                                       bg_color=accentColour, text_color=textColour)
        self.randomuser1_meeting = customtkinter.CTkLabel(self, text='Meeting Mode...',
                                                       text_font=['Bahnschrift bold', 14],
                                                       bg_color=accentColour, text_color=textColour)

        self.load_add_img = tk.PhotoImage(file='images/add_user_img.png')
        def add_user():
            """
            Updates user's dedicated table with an invite sent and updates receiving user's dedicated table with invite
            received. Checks if invite has been sent before and thus does not send another one, displays error message
            if does so.
            :return:Updates both inviter and receiver's tables, or displays error message
            """
            file = open("Databases/logs.txt", "r").read()
            username = str(file[:-1])
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            sql = 'CREATE TABLE IF NOT EXISTS ' + username + ' (userid SERIAL PRIMARY KEY, invite_received TEXT, invite_sent TEXT, proggies TEXT, chat_logs TEXT)'
            hCursor.execute(sql)
            hConn.commit()
            sql = 'SELECT invite_sent FROM ' + username
            hCursor.execute(sql)
            invited = hCursor.fetchall()
            count = 0
            for name in invited:
                if self.search_user.get() == name[0]:
                    self.success_label['text'] = 'Request already sent!'
                    self.success_label.place(x=690, y=450)
                    count += 1
            print(count)
            sql = 'SELECT proggies FROM ' + username
            hCursor.execute(sql)
            proggies = hCursor.fetchall()
            for name in proggies:
                if self.search_user.get() == name[0]:
                    self.success_label['text'] = 'You two are already Proggies!'
                    self.success_label.place(x=700, y=450)
                    count +=1
            if count == 0:
                #sql = 'INSERT INTO Personal(invite_sent) VALUES(?)',(self.search_user.get())
                searched_username = str(self.search_user.get())
                sql = "INSERT INTO {0}(invite_sent) VALUES('{1}')".format(username, searched_username)

                hCursor.execute(sql)
                hConn.commit()
                hConn.close()
                sql = 'Databases/' + self.search_user.get() + '_db.db'
                hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                         user="wfpsdpcxvibamf",
                                         password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                         port="5432")
                hCursor = hConn.cursor()
                sql = 'CREATE TABLE IF NOT EXISTS ' + searched_username + ' (userid SERIAL PRIMARY KEY, invite_received TEXT, invite_sent TEXT, proggies TEXT, chat_logs TEXT)'
                hCursor.execute(sql)
                hConn.commit()
                #sql = 'INSERT INTO ' + searched_username + '(invite_sent) VALUES(%s)' + ',(' + username + ')'
                sql = "INSERT INTO {0}(invite_received) VALUES('{1}')".format(searched_username, username)
                hCursor.execute(sql)
                hConn.commit()
                hConn.close()
                self.success_label['text'] = 'Friend Request Sent!'
                self.success_label.place(x=790, y=450)
        self.add_img_btn1 = customtkinter.CTkButton(self, image=self.load_add_img, bg_color=accentColour, command=add_user,
                                                    text="", fg_color=accentColour3)

        # arrange elements & widgets
        #self.space_label1.place(x=0, y=0)
        self.recs_btn.place(x=2, y=2)
        self.search_btn.place(x=158, y=2)
        self.events_btn.place(x=300, y=2)
        self.contacts_btn.place(x=442, y=2)
        self.profile_btn.place(x=584, y=2)
        self.user_label.place(x=330, y=180)
        self.search_user.place(x=440, y=260)
        self.usersearch_button.place(x=850, y=255)
        self.rect_label_1.place(x=330, y=340)
        self.randomuser1_img.place(x=400, y=370)
        self.randomuser1_username.place(x=390, y=550)
        self.randomuser1_desc.place(x=620, y=360)
        self.randomuser1_study.place(x=620, y=420)
        self.randomuser1_meeting.place(x=620, y=460)
        self.randomuser1_code.place(x=620, y=500)
        self.add_img_btn1.place(x=410, y=610)
        self.label_block.place(x=0, y=470)
        self.label_block.tkraise()
        self.success_label.place(x=700, y=450)
        self.fail_label.place(x=600, y=450)