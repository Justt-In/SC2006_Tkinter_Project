import tkinter as tk
import customtkinter
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

class Contacts_page(customtkinter.CTkFrame):

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

        # This function updates the contacts list and changes view to the recommendations page
        def goto_recs():
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]
            sql = 'Databases/' + username + '_db.db'
            refresh_conn1 = sqlite3.connect(sql)
            refresh_cursor1 = refresh_conn1.cursor()
            refresh_cursor1.execute('SELECT proggies from Personal')
            proggies_list = refresh_cursor1.fetchall()
            # print(proggies_list[0][0])
            refresh_conn2 = sqlite3.connect('Databases/User_database.db')
            refresh_cursor2 = refresh_conn2.cursor()
            count = 0
            for name in proggies_list:
                refresh_cursor2.execute('SELECT profile_pic FROM User WHERE username = ?', (name[0],))
                picture = refresh_cursor2.fetchall()
                # print(picture[0][0][25:])
                try:
                    if count == 0:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image1 = Image.open(filepath)
                            self.proggy_image1 = ImageTk.PhotoImage(
                                self.load_proggy_image1.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label1.configure(image=self.proggy_image1)
                            self.pic_label1.image = self.proggy_image1
                        self.username_label1['text'] = name[0]
                    elif count == 1:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image2 = Image.open(filepath)
                            self.proggy_image2 = ImageTk.PhotoImage(
                                self.load_proggy_image2.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label2.configure(image=self.proggy_image2)
                            self.pic_label2.image = self.proggy_image2
                        self.username_label2['text'] = name[0]
                    elif count == 2:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image3 = Image.open(filepath)
                            self.proggy_image3 = ImageTk.PhotoImage(
                                self.load_proggy_image3.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label3.configure(image=self.proggy_image3)
                            self.pic_label3.image = self.proggy_image3
                        self.username_label3['text'] = name[0]
                    elif count == 3:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image4 = Image.open(filepath)
                            self.proggy_image4 = ImageTk.PhotoImage(
                                self.load_proggy_image4.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label4.configure(image=self.proggy_image4)
                            self.pic_label4.image = self.proggy_image4
                        self.username_label4['text'] = name[0]
                    elif count == 4:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image5 = Image.open(filepath)
                            self.proggy_image5 = ImageTk.PhotoImage(
                                self.load_proggy_image5.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label5.configure(image=self.proggy_image5)
                            self.pic_label5.image = self.proggy_image5
                        self.username_label5['text'] = name[0]
                    elif count == 5:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image6 = Image.open(filepath)
                            self.proggy_image6 = ImageTk.PhotoImage(
                                self.load_proggy_image6.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label6.configure(image=self.proggy_image6)
                            self.pic_label6.image = self.proggy_image6
                        self.username_label6['text'] = name[0]
                    elif count == 6:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image7 = Image.open(filepath)
                            self.proggy_image7 = ImageTk.PhotoImage(
                                self.load_proggy_image7.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label7.configure(image=self.proggy_image7)
                            self.pic_label7.image = self.proggy_image7
                        self.username_label7['text'] = name[0]
                    elif count == 7:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image8 = Image.open(filepath)
                            self.proggy_image8 = ImageTk.PhotoImage(
                                self.load_proggy_image8.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label8.configure(image=self.proggy_image8)
                            self.pic_label8.image = self.proggy_image8
                        self.username_label8['text'] = name[0]
                    count += 1
                except IndexError:
                    break
            controller.show_frame('Recs_page')
        self.recs_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Recommendations',
                                                text_color=textColour,
                                                text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                command=goto_recs)

        # This function updates the contacts list and changes view to the search page
        def goto_search():
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]
            sql = 'Databases/' + username + '_db.db'
            refresh_conn1 = sqlite3.connect(sql)
            refresh_cursor1 = refresh_conn1.cursor()
            refresh_cursor1.execute('SELECT proggies from Personal')
            proggies_list = refresh_cursor1.fetchall()
            # print(proggies_list[0][0])
            refresh_conn2 = sqlite3.connect('Databases/User_database.db')
            refresh_cursor2 = refresh_conn2.cursor()
            count = 0
            for name in proggies_list:
                refresh_cursor2.execute('SELECT profile_pic FROM User WHERE username = ?', (name[0],))
                picture = refresh_cursor2.fetchall()
                # print(picture[0][0][25:])
                try:
                    if count == 0:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image1 = Image.open(filepath)
                            self.proggy_image1 = ImageTk.PhotoImage(
                                self.load_proggy_image1.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label1.configure(image=self.proggy_image1)
                            self.pic_label1.image = self.proggy_image1
                        self.username_label1['text'] = name[0]
                    elif count == 1:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image2 = Image.open(filepath)
                            self.proggy_image2 = ImageTk.PhotoImage(
                                self.load_proggy_image2.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label2.configure(image=self.proggy_image2)
                            self.pic_label2.image = self.proggy_image2
                        self.username_label2['text'] = name[0]
                    elif count == 2:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image3 = Image.open(filepath)
                            self.proggy_image3 = ImageTk.PhotoImage(
                                self.load_proggy_image3.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label3.configure(image=self.proggy_image3)
                            self.pic_label3.image = self.proggy_image3
                        self.username_label3['text'] = name[0]
                    elif count == 3:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image4 = Image.open(filepath)
                            self.proggy_image4 = ImageTk.PhotoImage(
                                self.load_proggy_image4.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label4.configure(image=self.proggy_image4)
                            self.pic_label4.image = self.proggy_image4
                        self.username_label4['text'] = name[0]
                    elif count == 4:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image5 = Image.open(filepath)
                            self.proggy_image5 = ImageTk.PhotoImage(
                                self.load_proggy_image5.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label5.configure(image=self.proggy_image5)
                            self.pic_label5.image = self.proggy_image5
                        self.username_label5['text'] = name[0]
                    elif count == 5:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image6 = Image.open(filepath)
                            self.proggy_image6 = ImageTk.PhotoImage(
                                self.load_proggy_image6.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label6.configure(image=self.proggy_image6)
                            self.pic_label6.image = self.proggy_image6
                        self.username_label6['text'] = name[0]
                    elif count == 6:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image7 = Image.open(filepath)
                            self.proggy_image7 = ImageTk.PhotoImage(
                                self.load_proggy_image7.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label7.configure(image=self.proggy_image7)
                            self.pic_label7.image = self.proggy_image7
                        self.username_label7['text'] = name[0]
                    elif count == 7:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image8 = Image.open(filepath)
                            self.proggy_image8 = ImageTk.PhotoImage(
                                self.load_proggy_image8.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label8.configure(image=self.proggy_image8)
                            self.pic_label8.image = self.proggy_image8
                        self.username_label8['text'] = name[0]
                    count += 1
                except IndexError:
                    break
            controller.show_frame('Search_page')
        self.search_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Search Users', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                  command=goto_search)

        # This function updates the contacts list and changes view to the events page
        def goto_events():
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]
            sql = 'Databases/' + username + '_db.db'
            refresh_conn1 = sqlite3.connect(sql)
            refresh_cursor1 = refresh_conn1.cursor()
            refresh_cursor1.execute('SELECT proggies from Personal')
            proggies_list = refresh_cursor1.fetchall()
            # print(proggies_list[0][0])
            refresh_conn2 = sqlite3.connect('Databases/User_database.db')
            refresh_cursor2 = refresh_conn2.cursor()
            count = 0
            for name in proggies_list:
                refresh_cursor2.execute('SELECT profile_pic FROM User WHERE username = ?', (name[0],))
                picture = refresh_cursor2.fetchall()
                # print(picture[0][0][25:])
                try:
                    if count == 0:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image1 = Image.open(filepath)
                            self.proggy_image1 = ImageTk.PhotoImage(
                                self.load_proggy_image1.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label1.configure(image=self.proggy_image1)
                            self.pic_label1.image = self.proggy_image1
                        self.username_label1['text'] = name[0]
                    elif count == 1:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image2 = Image.open(filepath)
                            self.proggy_image2 = ImageTk.PhotoImage(
                                self.load_proggy_image2.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label2.configure(image=self.proggy_image2)
                            self.pic_label2.image = self.proggy_image2
                        self.username_label2['text'] = name[0]
                    elif count == 2:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image3 = Image.open(filepath)
                            self.proggy_image3 = ImageTk.PhotoImage(
                                self.load_proggy_image3.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label3.configure(image=self.proggy_image3)
                            self.pic_label3.image = self.proggy_image3
                        self.username_label3['text'] = name[0]
                    elif count == 3:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image4 = Image.open(filepath)
                            self.proggy_image4 = ImageTk.PhotoImage(
                                self.load_proggy_image4.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label4.configure(image=self.proggy_image4)
                            self.pic_label4.image = self.proggy_image4
                        self.username_label4['text'] = name[0]
                    elif count == 4:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image5 = Image.open(filepath)
                            self.proggy_image5 = ImageTk.PhotoImage(
                                self.load_proggy_image5.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label5.configure(image=self.proggy_image5)
                            self.pic_label5.image = self.proggy_image5
                        self.username_label5['text'] = name[0]
                    elif count == 5:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image6 = Image.open(filepath)
                            self.proggy_image6 = ImageTk.PhotoImage(
                                self.load_proggy_image6.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label6.configure(image=self.proggy_image6)
                            self.pic_label6.image = self.proggy_image6
                        self.username_label6['text'] = name[0]
                    elif count == 6:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image7 = Image.open(filepath)
                            self.proggy_image7 = ImageTk.PhotoImage(
                                self.load_proggy_image7.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label7.configure(image=self.proggy_image7)
                            self.pic_label7.image = self.proggy_image7
                        self.username_label7['text'] = name[0]
                    elif count == 7:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image8 = Image.open(filepath)
                            self.proggy_image8 = ImageTk.PhotoImage(
                                self.load_proggy_image8.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label8.configure(image=self.proggy_image8)
                            self.pic_label8.image = self.proggy_image8
                        self.username_label8['text'] = name[0]
                    count += 1
                except IndexError:
                    break
            controller.show_frame('Events_page')
        self.events_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='View Events', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30,fg_color=accentColour,
                                                  command=goto_events)

        def goto_contacts():
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]
            sql = 'Databases/' + username + '_db.db'
            refresh_conn1 = sqlite3.connect(sql)
            refresh_cursor1 = refresh_conn1.cursor()
            refresh_cursor1.execute('SELECT proggies from Personal')
            proggies_list = refresh_cursor1.fetchall()
            # print(proggies_list[0][0])
            refresh_conn2 = sqlite3.connect('Databases/User_database.db')
            refresh_cursor2 = refresh_conn2.cursor()
            count = 0
            for name in proggies_list:
                refresh_cursor2.execute('SELECT profile_pic FROM User WHERE username = ?', (name[0],))
                picture = refresh_cursor2.fetchall()
                # print(picture[0][0][25:])
                try:
                    if count == 0:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image1 = Image.open(filepath)
                            self.proggy_image1 = ImageTk.PhotoImage(
                                self.load_proggy_image1.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label1.configure(image=self.proggy_image1)
                            self.pic_label1.image = self.proggy_image1
                        self.username_label1['text'] = name[0]
                    elif count == 1:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image2 = Image.open(filepath)
                            self.proggy_image2 = ImageTk.PhotoImage(
                                self.load_proggy_image2.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label2.configure(image=self.proggy_image2)
                            self.pic_label2.image = self.proggy_image2
                        self.username_label2['text'] = name[0]
                    elif count == 2:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image3 = Image.open(filepath)
                            self.proggy_image3 = ImageTk.PhotoImage(
                                self.load_proggy_image3.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label3.configure(image=self.proggy_image3)
                            self.pic_label3.image = self.proggy_image3
                        self.username_label3['text'] = name[0]
                    elif count == 3:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image4 = Image.open(filepath)
                            self.proggy_image4 = ImageTk.PhotoImage(
                                self.load_proggy_image4.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label4.configure(image=self.proggy_image4)
                            self.pic_label4.image = self.proggy_image4
                        self.username_label4['text'] = name[0]
                    elif count == 4:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image5 = Image.open(filepath)
                            self.proggy_image5 = ImageTk.PhotoImage(
                                self.load_proggy_image5.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label5.configure(image=self.proggy_image5)
                            self.pic_label5.image = self.proggy_image5
                        self.username_label5['text'] = name[0]
                    elif count == 5:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image6 = Image.open(filepath)
                            self.proggy_image6 = ImageTk.PhotoImage(
                                self.load_proggy_image6.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label6.configure(image=self.proggy_image6)
                            self.pic_label6.image = self.proggy_image6
                        self.username_label6['text'] = name[0]
                    elif count == 6:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image7 = Image.open(filepath)
                            self.proggy_image7 = ImageTk.PhotoImage(
                                self.load_proggy_image7.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label7.configure(image=self.proggy_image7)
                            self.pic_label7.image = self.proggy_image7
                        self.username_label7['text'] = name[0]
                    elif count == 7:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image8 = Image.open(filepath)
                            self.proggy_image8 = ImageTk.PhotoImage(
                                self.load_proggy_image8.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label8.configure(image=self.proggy_image8)
                            self.pic_label8.image = self.proggy_image8
                        self.username_label8['text'] = name[0]
                    count += 1
                except IndexError:
                    break
            controller.show_frame('Contacts_page')
        self.contacts_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='My Contacts',text_color=textColour,
                                                    text_font=['trebuchet MS bold', 12], height=30,fg_color=accentColour2,
                                                    command=goto_contacts)

        def goto_profile():
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]
            sql = 'Databases/' + username + '_db.db'
            refresh_conn1 = sqlite3.connect(sql)
            refresh_cursor1 = refresh_conn1.cursor()
            refresh_cursor1.execute('SELECT proggies from Personal')
            proggies_list = refresh_cursor1.fetchall()
            # print(proggies_list[0][0])
            refresh_conn2 = sqlite3.connect('Databases/User_database.db')
            refresh_cursor2 = refresh_conn2.cursor()
            count = 0
            for name in proggies_list:
                refresh_cursor2.execute('SELECT profile_pic FROM User WHERE username = ?', (name[0],))
                picture = refresh_cursor2.fetchall()
                # print(picture[0][0][25:])
                try:
                    if count == 0:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image1 = Image.open(filepath)
                            self.proggy_image1 = ImageTk.PhotoImage(
                                self.load_proggy_image1.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label1.configure(image=self.proggy_image1)
                            self.pic_label1.image = self.proggy_image1
                        self.username_label1['text'] = name[0]
                    elif count == 1:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image2 = Image.open(filepath)
                            self.proggy_image2 = ImageTk.PhotoImage(
                                self.load_proggy_image2.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label2.configure(image=self.proggy_image2)
                            self.pic_label2.image = self.proggy_image2
                        self.username_label2['text'] = name[0]
                    elif count == 2:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image3 = Image.open(filepath)
                            self.proggy_image3 = ImageTk.PhotoImage(
                                self.load_proggy_image3.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label3.configure(image=self.proggy_image3)
                            self.pic_label3.image = self.proggy_image3
                        self.username_label3['text'] = name[0]
                    elif count == 3:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image4 = Image.open(filepath)
                            self.proggy_image4 = ImageTk.PhotoImage(
                                self.load_proggy_image4.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label4.configure(image=self.proggy_image4)
                            self.pic_label4.image = self.proggy_image4
                        self.username_label4['text'] = name[0]
                    elif count == 4:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image5 = Image.open(filepath)
                            self.proggy_image5 = ImageTk.PhotoImage(
                                self.load_proggy_image5.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label5.configure(image=self.proggy_image5)
                            self.pic_label5.image = self.proggy_image5
                        self.username_label5['text'] = name[0]
                    elif count == 5:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image6 = Image.open(filepath)
                            self.proggy_image6 = ImageTk.PhotoImage(
                                self.load_proggy_image6.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label6.configure(image=self.proggy_image6)
                            self.pic_label6.image = self.proggy_image6
                        self.username_label6['text'] = name[0]
                    elif count == 6:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image7 = Image.open(filepath)
                            self.proggy_image7 = ImageTk.PhotoImage(
                                self.load_proggy_image7.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label7.configure(image=self.proggy_image7)
                            self.pic_label7.image = self.proggy_image7
                        self.username_label7['text'] = name[0]
                    elif count == 7:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image8 = Image.open(filepath)
                            self.proggy_image8 = ImageTk.PhotoImage(
                                self.load_proggy_image8.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label8.configure(image=self.proggy_image8)
                            self.pic_label8.image = self.proggy_image8
                        self.username_label8['text'] = name[0]
                    count += 1
                except IndexError:
                    break
            controller.show_frame('Profile_page')
        self.profile_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='My Profile', text_color=textColour,
                                                   text_font=['trebuchet MS bold', 12], height=30,fg_color=accentColour,
                                                   command=goto_profile)
        # End of Toolbar

        #Add elements and widgets
        self.load_backdrop = Image.open("images/backdrop_v2_2.png")
        self.load_message = Image.open("images/message_logo.png")
        self.load_delete = Image.open("images/delete_icon.png")
        self.load_user_image = Image.open("images/default_profile_img.png")
        self.load_view_prof_image = Image.open("images/view_prof_icon.png")
        self.backdrops = ImageTk.PhotoImage(self.load_backdrop.resize((500, 150), Image.ANTIALIAS))
        self.messages = ImageTk.PhotoImage(self.load_message.resize((55, 55), Image.ANTIALIAS))
        self.deletes = ImageTk.PhotoImage(self.load_delete.resize((55, 55), Image.ANTIALIAS))
        self.view_prof_image = ImageTk.PhotoImage(self.load_view_prof_image.resize((55, 55), Image.ANTIALIAS))
        self.profiles = ImageTk.PhotoImage(self.load_user_image.resize((100, 100), Image.ANTIALIAS))
        self.block_label = tk.Label(self, width=160, height=100, bg=main_bg)
        self.load_requests_image = Image.open("images/add_user_img.png")
        self.requests_image = ImageTk.PhotoImage(self.load_requests_image.resize((100, 100), Image.ANTIALIAS))
        #This function allows the user to view all the requests sent to them, it checks their personal database and
        # retrieves the username's of senders and number of invites received
        def view_requests():
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]
            sql = 'Databases/' + username + '_db.db'
            connection = sqlite3.connect(sql)
            cursor = connection.cursor()
            cursor.execute('SELECT invite_received from Personal')
            received_requests = cursor.fetchall()
            count = len(received_requests)
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            #this function opens a new window and populates a grid with all the sender's usernames and profile pictures
            def populate(newWindow):
                noneCounter = 0
                for name in received_requests:
                    #print(name[0])
                    if name[0] == None:
                        noneCounter += 1
                if noneCounter == count:
                    tk.Label(newWindow, text='No requests yet, come back again later!', bg='#33A1FD',
                             font='Bahnschrift 24 bold').grid(row=0, column=0)
                    return
                self.picture = {}
                self.accept = {}
                self.resized_accept = {}
                self.accept_button = {}
                self.decline = {}
                self.resized_decline = {}
                self.decline_button = {}
                self.open_image = {}
                self.resized_image = {}
                user_list = []
                #print(count)
                for name in range(count):
                    person = received_requests[name][0]
                    #print(person)
                    if person == None:
                        continue
                    #print(person)
                    cursor.execute('SELECT profile_pic, username FROM User WHERE username = ?', [person])
                    details = cursor.fetchall()
                    try:
                        if details[0][0] == None or details[0][0] == '':
                            self.open_image[name] = Image.open('images/default_profile_img.png')
                        else:
                            filepath = "images/" + details[0][0][25:]
                            self.open_image[name] = Image.open(filepath)
                    except:
                        print("Some error")
                        tk.Label(newWindow, text='No requests yet, come back again later!', bg='#33A1FD', font='Bahnschrift 24 bold').grid(row=0, column=0)
                        return
                    self.resized_image[name] = ImageTk.PhotoImage(self.open_image[name].resize((200, 150), Image.ANTIALIAS))
                    self.picture[name] = tk.Label(newWindow, image=self.resized_image[name], bg='#33A1FD', relief='solid').grid(row=name, column=0)
                    user = details[0][1]
                    user_list.append(user)
                    tk.Label(newWindow, text=user, font='Bahnschrift 24 bold', bg='#33A1FD').grid(row=name, column=1)
                    self.accept[name] = Image.open('images/check_icon.png')
                    self.resized_accept[name] = ImageTk.PhotoImage(self.accept[name].resize((150, 150), Image.ANTIALIAS))
                    #This function will trigger when the logged in user accepts a request from the sender
                    def accept_request(btnName):

                        if len(user_list) == 1:
                            adding = user_list[0]
                        else:
                            print("btnName: " + str(btnName))
                            adding = user_list[btnName-3]
                            print("adding: " + adding)
                        #for x in user_list:
                            #adding = x
                        sql = "Databases/" + username + '_db.db'
                        newConnection1 = sqlite3.connect(sql)
                        newCursor1 = newConnection1.cursor()
                        sql = "Databases/" + adding + '_db.db'
                        newConnection2 = sqlite3.connect(sql)
                        newCursor2 = newConnection2.cursor()
                        #update logged in user's database
                        newCursor1.execute('UPDATE Personal SET invite_received = ?, proggies = ? WHERE invite_received = ?', (None, adding, adding,))
                        newConnection1.commit()
                        #update sender's database
                        newCursor2.execute('UPDATE Personal SET invite_sent = ?, proggies = ? WHERE invite_sent = ?',(None, username, username,))
                        newConnection2.commit()
                        tk.messagebox.showinfo("New Proggy", "Proggy Request Accepted!")
                    self.accept_button[name] = tk.Button(newWindow, bg='#33A1FD', image=self.resized_accept[name], relief='solid', command= lambda text=name:accept_request(text)).grid(row=name,column=2)
                    self.decline[name] = Image.open('images/delete_icon.png')
                    self.resized_decline[name] = ImageTk.PhotoImage(self.decline[name].resize((150, 150), Image.ANTIALIAS))
                    #This function triggers when the sender declines a request from a sender
                    def decline_request(btnName):
                        sql = "Databases/" + username + '_db.db'
                        newConnection1 = sqlite3.connect(sql)
                        newCursor1 = newConnection1.cursor()
                        sql = "Databases/" + user_list[btnName] + '_db.db'
                        newConnection2 = sqlite3.connect(sql)
                        newCursor2 = newConnection2.cursor()
                        #update logged in user's database
                        newCursor1.execute('DELETE FROM Personal WHERE invite_received = ?', (user_list[btnName],))
                        newConnection1.commit()
                        # update sender's database
                        newCursor2.execute('DELETE FROM Personal WHERE invite_sent = ?',(username,))
                        newConnection2.commit()
                        tk.messagebox.showinfo("Decline Proggy", "Proggy Request Declined")

                    self.decline_button[name] = tk.Button(newWindow, bg='#33A1FD', image=self.resized_decline[name], relief='solid', command= lambda text=name:decline_request(text)).grid(row=name, column=3)
            #This function resets the scrollbar to the top of the page
            def onFrameConfigure(canvas):
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("700x500")
            canvas = tk.Canvas(root, borderwidth=0, background="#33A1FD")
            frame = tk.Frame(canvas, background="#33A1FD")
            vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=vsb.set)
            hsb = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
            canvas.configure(xscrollcommand=hsb.set)

            vsb.pack(side="right", fill="y")
            hsb.pack(side="bottom", fill="x")
            canvas.pack(side="left", fill="both", expand=True)
            canvas.create_window((4, 4), window=frame, anchor="nw")

            frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

            populate(frame)
            connection.close()

        #this function gets all the contacts that are currently friends with the logged in user from the database and
        #displays it on the screen
        def view_proggies():
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]
            sql = 'Databases/' + username + '_db.db'
            refresh_conn1 = sqlite3.connect(sql)
            refresh_cursor1 = refresh_conn1.cursor()
            refresh_cursor1.execute('SELECT proggies from Personal')
            proggies_list = refresh_cursor1.fetchall()
            #print(proggies_list[0][0])
            refresh_conn2 = sqlite3.connect('Databases/User_database.db')
            refresh_cursor2 = refresh_conn2.cursor()
            count = 0
            try:
                for name in proggies_list:
                    if name[0] == None:
                        continue
                    refresh_cursor2.execute('SELECT profile_pic FROM User WHERE username = ?', (name[0],))
                    picture = refresh_cursor2.fetchall()
                    if count == 0:
                        if picture[0][0] != None :
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image1 = Image.open(filepath)
                            self.proggy_image1 = ImageTk.PhotoImage(
                                self.load_proggy_image1.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label1.configure(image=self.proggy_image1)
                            self.pic_label1.image = self.proggy_image1
                        self.username_label1['text'] = name[0]
                    elif count == 1:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image2 = Image.open(filepath)
                            self.proggy_image2 = ImageTk.PhotoImage(
                                self.load_proggy_image2.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label2.configure(image=self.proggy_image2)
                            self.pic_label2.image = self.proggy_image2
                        self.username_label2['text'] = name[0]
                    elif count == 2:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image3 = Image.open(filepath)
                            self.proggy_image3 = ImageTk.PhotoImage(
                                self.load_proggy_image3.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label3.configure(image=self.proggy_image3)
                            self.pic_label3.image = self.proggy_image3
                        self.username_label3['text'] = name[0]
                    elif count == 3:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image4 = Image.open(filepath)
                            self.proggy_image4 = ImageTk.PhotoImage(
                                self.load_proggy_image4.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label4.configure(image=self.proggy_image4)
                            self.pic_label4.image = self.proggy_image4
                        self.username_label4['text'] = name[0]
                    elif count == 4:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image5 = Image.open(filepath)
                            self.proggy_image5 = ImageTk.PhotoImage(
                                self.load_proggy_image5.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label5.configure(image=self.proggy_image5)
                            self.pic_label5.image = self.proggy_image5
                        self.username_label5['text'] = name[0]
                    elif count == 5:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image6 = Image.open(filepath)
                            self.proggy_image6 = ImageTk.PhotoImage(
                                self.load_proggy_image6.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label6.configure(image=self.proggy_image6)
                            self.pic_label6.image = self.proggy_image6
                        self.username_label6['text'] = name[0]
                    elif count == 6:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image7 = Image.open(filepath)
                            self.proggy_image7 = ImageTk.PhotoImage(
                                self.load_proggy_image7.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label7.configure(image=self.proggy_image7)
                            self.pic_label7.image = self.proggy_image7
                        self.username_label7['text'] = name[0]
                    elif count == 7:
                        if picture[0][0] != None:
                            filepath = "images/" + picture[0][0][25:]
                            self.load_proggy_image8 = Image.open(filepath)
                            self.proggy_image8 = ImageTk.PhotoImage(
                                self.load_proggy_image8.resize((100, 100), Image.ANTIALIAS))
                            self.pic_label8.configure(image=self.proggy_image8)
                            self.pic_label8.image = self.proggy_image8
                        self.username_label8['text'] = name[0]
                    count += 1
                self.block_label.lower()
            except IndexError:
                tk.messagebox.showerror("Page Error", "Error loading page, please relaunch application")

        self.requests = customtkinter.CTkButton(self, image=self.requests_image, bg=main_bg, text="View Invites",
                                                text_color=textColour, text_font=["trebuchet MS bold", 19], compound="top",
                                                command=view_requests)
        #self.requests_label = tk.Label(self, text='View Invite\nRequests', font='Bahnschrift 16 bold', bg='#2176FF', fg='white')
        self.load_proggies_image = Image.open("images/proggies_icon.png")
        self.proggies_image = ImageTk.PhotoImage(self.load_proggies_image.resize((100, 100), Image.ANTIALIAS))
        self.proggies = customtkinter.CTkButton(self, image=self.proggies_image, bg_color=main_bg,text="View Your Proggies",
                                                text_color=textColour, text_font=["trebuchet MS bold", 12], compound="top",
                                                command=view_proggies)
        self.proggies_label = tk.Label(self, text='View Your\nProggies', font='Bahnschrift 16 bold', bg='#2176FF', fg='white')

        #This function allows the logged in user to remove a friend from their contacts list - friend 1
        def remove_proggy1():
            if self.username_label1.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askyesno('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == False:
                return
            else:
                proggy = self.username_label1.cget("text")
                #connect to logged in user's db
                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]
                sql = 'Databases/' + username + '_db.db'
                delete_conn1 = sqlite3.connect(sql)
                delete_cursor1 = delete_conn1.cursor()
                delete_cursor1.execute('DELETE FROM Personal WHERE proggies = ?',(proggy,))
                delete_conn1.commit()
                sql = 'Databases/' + proggy + '_db.db'
                delete_conn2 = sqlite3.connect(sql)
                delete_cursor2 = delete_conn2.cursor()
                delete_cursor2.execute('DELETE FROM Personal WHERE proggies = ?',(username,))
                delete_conn2.commit()
                tk.messagebox.showinfo("Delete Success", "Proggy Deleted Successfully")
                count = 0
                username1 = self.username_label1.cget('text')
                if username1 != "Username":
                    count += 1
                username2 = self.username_label2.cget('text')
                if username2 != "Username":
                    count += 1
                username3 = self.username_label3.cget('text')
                if username3 != "Username":
                    count += 1
                username4 = self.username_label4.cget('text')
                if username4 != "Username":
                    count += 1
                username5 = self.username_label5.cget('text')
                if username5 != "Username":
                    count += 1
                username6 = self.username_label6.cget('text')
                if username6 != "Username":
                    count += 1
                username7 = self.username_label7.cget('text')
                if username7 != "Username":
                    count += 1
                username8 = self.username_label8.cget('text')
                if username8 != "Username":
                    count += 1

                if count == 1:
                    self.pic_label1.configure(image=self.profiles)
                    self.username_label1['text'] = 'Username'
                elif count == 2:
                    self.pic_label2.configure(image=self.profiles)
                    self.username_label2['text'] = 'Username'
                elif count == 3:
                    self.pic_label3.configure(image=self.profiles)
                    self.username_label3['text'] = 'Username'
                elif count == 4:
                    self.pic_label4.configure(image=self.profiles)
                    self.username_label4['text'] = 'Username'
                elif count == 5:
                    self.pic_label5.configure(image=self.profiles)
                    self.username_label5['text'] = 'Username'
                elif count == 6:
                    self.pic_label6.configure(image=self.profiles)
                    self.username_label6['text'] = 'Username'
                elif count == 7:
                    self.pic_label7.configure(image=self.profiles)
                    self.username_label7['text'] = 'Username'
                elif count == 8:
                    self.pic_label8.configure(image=self.profiles)
                    self.username_label8['text'] = 'Username'

        # This function allows the logged in user to remove a friend from their contacts list - friend 2
        def remove_proggy2():
            if self.username_label2.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askyesno('Delete Proggy', 'Are you sure you want to delete this proggy?',
                                            icon='warning')
            if MsgBox == False:
                return
            else:
                proggy = self.username_label2.cget("text")
                #connect to logged in user's db
                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]
                sql = 'Databases/' + username + '_db.db'
                delete_conn1 = sqlite3.connect(sql)
                delete_cursor1 = delete_conn1.cursor()
                delete_cursor1.execute('DELETE FROM Personal WHERE proggies = ?',(proggy,))
                delete_conn1.commit()
                sql = 'Databases/' + proggy + '_db.db'
                delete_conn2 = sqlite3.connect(sql)
                delete_cursor2 = delete_conn2.cursor()
                delete_cursor2.execute('DELETE FROM Personal WHERE proggies = ?',(username,))
                delete_conn2.commit()
                tk.messagebox.showinfo("Delete Success", "Proggy Deleted Successfully")
                count = 0
                username1 = self.username_label1.cget('text')
                if username1 != "Username":
                    count += 1
                username2 = self.username_label2.cget('text')
                if username2 != "Username":
                    count += 1
                username3 = self.username_label3.cget('text')
                if username3 != "Username":
                    count += 1
                username4 = self.username_label4.cget('text')
                if username4 != "Username":
                    count += 1
                username5 = self.username_label5.cget('text')
                if username5 != "Username":
                    count += 1
                username6 = self.username_label6.cget('text')
                if username6 != "Username":
                    count += 1
                username7 = self.username_label7.cget('text')
                if username7 != "Username":
                    count += 1
                username8 = self.username_label8.cget('text')
                if username8 != "Username":
                    count += 1

                if count == 1:
                    self.pic_label1.configure(image=self.profiles)
                    self.username_label1['text'] = 'Username'
                elif count == 2:
                    self.pic_label2.configure(image=self.profiles)
                    self.username_label2['text'] = 'Username'
                elif count == 3:
                    self.pic_label3.configure(image=self.profiles)
                    self.username_label3['text'] = 'Username'
                elif count == 4:
                    self.pic_label4.configure(image=self.profiles)
                    self.username_label4['text'] = 'Username'
                elif count == 5:
                    self.pic_label5.configure(image=self.profiles)
                    self.username_label5['text'] = 'Username'
                elif count == 6:
                    self.pic_label6.configure(image=self.profiles)
                    self.username_label6['text'] = 'Username'
                elif count == 7:
                    self.pic_label7.configure(image=self.profiles)
                    self.username_label7['text'] = 'Username'
                elif count == 8:
                    self.pic_label8.configure(image=self.profiles)
                    self.username_label8['text'] = 'Username'

        # This function allows the logged in user to remove a friend from their contacts list - friend 3
        def remove_proggy3():
            if self.username_label3.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askyesno('Delete Proggy', 'Are you sure you want to delete this proggy?',
                                            icon='warning')
            if MsgBox == False:
                return
            else:
                proggy = self.username_label3.cget("text")
                #connect to logged in user's db
                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]
                sql = 'Databases/' + username + '_db.db'
                delete_conn1 = sqlite3.connect(sql)
                delete_cursor1 = delete_conn1.cursor()
                delete_cursor1.execute('DELETE FROM Personal WHERE proggies = ?',(proggy,))
                delete_conn1.commit()
                sql = 'Databases/' + proggy + '_db.db'
                delete_conn2 = sqlite3.connect(sql)
                delete_cursor2 = delete_conn2.cursor()
                delete_cursor2.execute('DELETE FROM Personal WHERE proggies = ?',(username,))
                delete_conn2.commit()
                tk.messagebox.showinfo("Delete Success", "Proggy Deleted Successfully")
                count = 0
                username1 = self.username_label1.cget('text')
                if username1 != "Username":
                    count += 1
                username2 = self.username_label2.cget('text')
                if username2 != "Username":
                    count += 1
                username3 = self.username_label3.cget('text')
                if username3 != "Username":
                    count += 1
                username4 = self.username_label4.cget('text')
                if username4 != "Username":
                    count += 1
                username5 = self.username_label5.cget('text')
                if username5 != "Username":
                    count += 1
                username6 = self.username_label6.cget('text')
                if username6 != "Username":
                    count += 1
                username7 = self.username_label7.cget('text')
                if username7 != "Username":
                    count += 1
                username8 = self.username_label8.cget('text')
                if username8 != "Username":
                    count += 1

                if count == 1:
                    self.pic_label1.configure(image=self.profiles)
                    self.username_label1['text'] = 'Username'
                elif count == 2:
                    self.pic_label2.configure(image=self.profiles)
                    self.username_label2['text'] = 'Username'
                elif count == 3:
                    self.pic_label3.configure(image=self.profiles)
                    self.username_label3['text'] = 'Username'
                elif count == 4:
                    self.pic_label4.configure(image=self.profiles)
                    self.username_label4['text'] = 'Username'
                elif count == 5:
                    self.pic_label5.configure(image=self.profiles)
                    self.username_label5['text'] = 'Username'
                elif count == 6:
                    self.pic_label6.configure(image=self.profiles)
                    self.username_label6['text'] = 'Username'
                elif count == 7:
                    self.pic_label7.configure(image=self.profiles)
                    self.username_label7['text'] = 'Username'
                elif count == 8:
                    self.pic_label8.configure(image=self.profiles)
                    self.username_label8['text'] = 'Username'

        # This function allows the logged in user to remove a friend from their contacts list - friend 4
        def remove_proggy4():
            if self.username_label4.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askyesno('Delete Proggy', 'Are you sure you want to delete this proggy?',
                                            icon='warning')
            if MsgBox == False:
                return
            else:
                proggy = self.username_label4.cget("text")
                #connect to logged in user's db
                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]
                sql = 'Databases/' + username + '_db.db'
                delete_conn1 = sqlite3.connect(sql)
                delete_cursor1 = delete_conn1.cursor()
                delete_cursor1.execute('DELETE FROM Personal WHERE proggies = ?',(proggy,))
                delete_conn1.commit()
                sql = 'Databases/' + proggy + '_db.db'
                delete_conn2 = sqlite3.connect(sql)
                delete_cursor2 = delete_conn2.cursor()
                delete_cursor2.execute('DELETE FROM Personal WHERE proggies = ?',(username,))
                delete_conn2.commit()
                tk.messagebox.showinfo("Delete Success", "Proggy Deleted Successfully")
                count = 0
                username1 = self.username_label1.cget('text')
                if username1 != "Username":
                    count += 1
                username2 = self.username_label2.cget('text')
                if username2 != "Username":
                    count += 1
                username3 = self.username_label3.cget('text')
                if username3 != "Username":
                    count += 1
                username4 = self.username_label4.cget('text')
                if username4 != "Username":
                    count += 1
                username5 = self.username_label5.cget('text')
                if username5 != "Username":
                    count += 1
                username6 = self.username_label6.cget('text')
                if username6 != "Username":
                    count += 1
                username7 = self.username_label7.cget('text')
                if username7 != "Username":
                    count += 1
                username8 = self.username_label8.cget('text')
                if username8 != "Username":
                    count += 1

                if count == 1:
                    self.pic_label1.configure(image=self.profiles)
                    self.username_label1['text'] = 'Username'
                elif count == 2:
                    self.pic_label2.configure(image=self.profiles)
                    self.username_label2['text'] = 'Username'
                elif count == 3:
                    self.pic_label3.configure(image=self.profiles)
                    self.username_label3['text'] = 'Username'
                elif count == 4:
                    self.pic_label4.configure(image=self.profiles)
                    self.username_label4['text'] = 'Username'
                elif count == 5:
                    self.pic_label5.configure(image=self.profiles)
                    self.username_label5['text'] = 'Username'
                elif count == 6:
                    self.pic_label6.configure(image=self.profiles)
                    self.username_label6['text'] = 'Username'
                elif count == 7:
                    self.pic_label7.configure(image=self.profiles)
                    self.username_label7['text'] = 'Username'
                elif count == 8:
                    self.pic_label8.configure(image=self.profiles)
                    self.username_label8['text'] = 'Username'

        # This function allows the logged in user to remove a friend from their contacts list - friend 5
        def remove_proggy5():
            if self.username_label5.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askyesno('Delete Proggy', 'Are you sure you want to delete this proggy?',
                                            icon='warning')
            if MsgBox == False:
                return
            else:
                proggy = self.username_label5.cget("text")
                #connect to logged in user's db
                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]
                sql = 'Databases/' + username + '_db.db'
                delete_conn1 = sqlite3.connect(sql)
                delete_cursor1 = delete_conn1.cursor()
                delete_cursor1.execute('DELETE FROM Personal WHERE proggies = ?',(proggy,))
                delete_conn1.commit()
                sql = 'Databases/' + proggy + '_db.db'
                delete_conn2 = sqlite3.connect(sql)
                delete_cursor2 = delete_conn2.cursor()
                delete_cursor2.execute('DELETE FROM Personal WHERE proggies = ?',(username,))
                delete_conn2.commit()
                tk.messagebox.showinfo("Delete Success", "Proggy Deleted Successfully")
                count = 0
                username1 = self.username_label1.cget('text')
                if username1 != "Username":
                    count += 1
                username2 = self.username_label2.cget('text')
                if username2 != "Username":
                    count += 1
                username3 = self.username_label3.cget('text')
                if username3 != "Username":
                    count += 1
                username4 = self.username_label4.cget('text')
                if username4 != "Username":
                    count += 1
                username5 = self.username_label5.cget('text')
                if username5 != "Username":
                    count += 1
                username6 = self.username_label6.cget('text')
                if username6 != "Username":
                    count += 1
                username7 = self.username_label7.cget('text')
                if username7 != "Username":
                    count += 1
                username8 = self.username_label8.cget('text')
                if username8 != "Username":
                    count += 1

                if count == 1:
                    self.pic_label1.configure(image=self.profiles)
                    self.username_label1['text'] = 'Username'
                elif count == 2:
                    self.pic_label2.configure(image=self.profiles)
                    self.username_label2['text'] = 'Username'
                elif count == 3:
                    self.pic_label3.configure(image=self.profiles)
                    self.username_label3['text'] = 'Username'
                elif count == 4:
                    self.pic_label4.configure(image=self.profiles)
                    self.username_label4['text'] = 'Username'
                elif count == 5:
                    self.pic_label5.configure(image=self.profiles)
                    self.username_label5['text'] = 'Username'
                elif count == 6:
                    self.pic_label6.configure(image=self.profiles)
                    self.username_label6['text'] = 'Username'
                elif count == 7:
                    self.pic_label7.configure(image=self.profiles)
                    self.username_label7['text'] = 'Username'
                elif count == 8:
                    self.pic_label8.configure(image=self.profiles)
                    self.username_label8['text'] = 'Username'

        # This function allows the logged in user to remove a friend from their contacts list - friend 6
        def remove_proggy6():
            if self.username_label6.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askyesno('Delete Proggy', 'Are you sure you want to delete this proggy?',
                                            icon='warning')
            if MsgBox == False:
                return
            else:
                proggy = self.username_label6.cget("text")
                #connect to logged in user's db
                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]
                sql = 'Databases/' + username + '_db.db'
                delete_conn1 = sqlite3.connect(sql)
                delete_cursor1 = delete_conn1.cursor()
                delete_cursor1.execute('DELETE FROM Personal WHERE proggies = ?',(proggy,))
                delete_conn1.commit()
                sql = 'Databases/' + proggy + '_db.db'
                delete_conn2 = sqlite3.connect(sql)
                delete_cursor2 = delete_conn2.cursor()
                delete_cursor2.execute('DELETE FROM Personal WHERE proggies = ?',(username,))
                delete_conn2.commit()
                tk.messagebox.showinfo("Delete Success", "Proggy Deleted Successfully")
                count = 0
                username1 = self.username_label1.cget('text')
                username1 = self.username_label1.cget('text')
                if username1 != "Username":
                    count += 1
                username2 = self.username_label2.cget('text')
                if username2 != "Username":
                    count += 1
                username3 = self.username_label3.cget('text')
                if username3 != "Username":
                    count += 1
                username4 = self.username_label4.cget('text')
                if username4 != "Username":
                    count += 1
                username5 = self.username_label5.cget('text')
                if username5 != "Username":
                    count += 1
                username6 = self.username_label6.cget('text')
                if username6 != "Username":
                    count += 1
                username7 = self.username_label7.cget('text')
                if username7 != "Username":
                    count += 1
                username8 = self.username_label8.cget('text')
                if username8 != "Username":
                    count += 1

                if count == 1:
                    self.pic_label1.configure(image=self.profiles)
                    self.username_label1['text'] = 'Username'
                elif count == 2:
                    self.pic_label2.configure(image=self.profiles)
                    self.username_label2['text'] = 'Username'
                elif count == 3:
                    self.pic_label3.configure(image=self.profiles)
                    self.username_label3['text'] = 'Username'
                elif count == 4:
                    self.pic_label4.configure(image=self.profiles)
                    self.username_label4['text'] = 'Username'
                elif count == 5:
                    self.pic_label5.configure(image=self.profiles)
                    self.username_label5['text'] = 'Username'
                elif count == 6:
                    self.pic_label6.configure(image=self.profiles)
                    self.username_label6['text'] = 'Username'
                elif count == 7:
                    self.pic_label7.configure(image=self.profiles)
                    self.username_label7['text'] = 'Username'
                elif count == 8:
                    self.pic_label8.configure(image=self.profiles)
                    self.username_label8['text'] = 'Username'

        # This function allows the logged in user to remove a friend from their contacts list - friend 7
        def remove_proggy7():
            if self.username_label7.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askyesno('Delete Proggy', 'Are you sure you want to delete this proggy?',
                                            icon='warning')
            if MsgBox == False:
                return
            else:
                proggy = self.username_label7.cget("text")
                #connect to logged in user's db
                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]
                sql = 'Databases/' + username + '_db.db'
                delete_conn1 = sqlite3.connect(sql)
                delete_cursor1 = delete_conn1.cursor()
                delete_cursor1.execute('DELETE FROM Personal WHERE proggies = ?',(proggy,))
                delete_conn1.commit()
                sql = 'Databases/' + proggy + '_db.db'
                delete_conn2 = sqlite3.connect(sql)
                delete_cursor2 = delete_conn2.cursor()
                delete_cursor2.execute('DELETE FROM Personal WHERE proggies = ?',(username,))
                delete_conn2.commit()
                tk.messagebox.showinfo("Delete Success", "Proggy Deleted Successfully")
                count = 0
                username1 = self.username_label1.cget('text')
                if username1 != "Username":
                    count += 1
                username2 = self.username_label2.cget('text')
                if username2 != "Username":
                    count += 1
                username3 = self.username_label3.cget('text')
                if username3 != "Username":
                    count += 1
                username4 = self.username_label4.cget('text')
                if username4 != "Username":
                    count += 1
                username5 = self.username_label5.cget('text')
                if username5 != "Username":
                    count += 1
                username6 = self.username_label6.cget('text')
                if username6 != "Username":
                    count += 1
                username7 = self.username_label7.cget('text')
                if username7 != "Username":
                    count += 1
                username8 = self.username_label8.cget('text')
                if username8 != "Username":
                    count += 1

                if count == 1:
                    self.pic_label1.configure(image=self.profiles)
                    self.username_label1['text'] = 'Username'
                elif count == 2:
                    self.pic_label2.configure(image=self.profiles)
                    self.username_label2['text'] = 'Username'
                elif count == 3:
                    self.pic_label3.configure(image=self.profiles)
                    self.username_label3['text'] = 'Username'
                elif count == 4:
                    self.pic_label4.configure(image=self.profiles)
                    self.username_label4['text'] = 'Username'
                elif count == 5:
                    self.pic_label5.configure(image=self.profiles)
                    self.username_label5['text'] = 'Username'
                elif count == 6:
                    self.pic_label6.configure(image=self.profiles)
                    self.username_label6['text'] = 'Username'
                elif count == 7:
                    self.pic_label7.configure(image=self.profiles)
                    self.username_label7['text'] = 'Username'
                elif count == 8:
                    self.pic_label8.configure(image=self.profiles)
                    self.username_label8['text'] = 'Username'

        # This function allows the logged in user to remove a friend from their contacts list - friend 8
        def remove_proggy8():
            if self.username_label8.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askyesno('Delete Proggy', 'Are you sure you want to delete this proggy?',
                                            icon='warning')
            if MsgBox == False:
                return
            else:
                proggy = self.username_label8.cget("text")
                #connect to logged in user's db
                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]
                sql = 'Databases/' + username + '_db.db'
                delete_conn1 = sqlite3.connect(sql)
                delete_cursor1 = delete_conn1.cursor()
                delete_cursor1.execute('DELETE FROM Personal WHERE proggies = ?',(proggy,))
                delete_conn1.commit()
                sql = 'Databases/' + proggy + '_db.db'
                delete_conn2 = sqlite3.connect(sql)
                delete_cursor2 = delete_conn2.cursor()
                delete_cursor2.execute('DELETE FROM Personal WHERE proggies = ?',(username,))
                delete_conn2.commit()
                tk.messagebox.showinfo("Delete Success", "Proggy Deleted Successfully")
                count = 0
                username1 = self.username_label1.cget('text')
                if username1 != "Username":
                    count += 1
                username2 = self.username_label2.cget('text')
                if username2 != "Username":
                    count += 1
                username3 = self.username_label3.cget('text')
                if username3 != "Username":
                    count += 1
                username4 = self.username_label4.cget('text')
                if username4 != "Username":
                    count += 1
                username5 = self.username_label5.cget('text')
                if username5 != "Username":
                    count += 1
                username6 = self.username_label6.cget('text')
                if username6 != "Username":
                    count += 1
                username7 = self.username_label7.cget('text')
                if username7 != "Username":
                    count += 1
                username8 = self.username_label8.cget('text')
                if username8 != "Username":
                    count += 1

                if count == 1:
                    self.pic_label1.configure(image=self.profiles)
                    self.username_label1['text'] = 'Username'
                elif count == 2:
                    self.pic_label2.configure(image=self.profiles)
                    self.username_label2['text'] = 'Username'
                elif count == 3:
                    self.pic_label3.configure(image=self.profiles)
                    self.username_label3['text'] = 'Username'
                elif count == 4:
                    self.pic_label4.configure(image=self.profiles)
                    self.username_label4['text'] = 'Username'
                elif count == 5:
                    self.pic_label5.configure(image=self.profiles)
                    self.username_label5['text'] = 'Username'
                elif count == 6:
                    self.pic_label6.configure(image=self.profiles)
                    self.username_label6['text'] = 'Username'
                elif count == 7:
                    self.pic_label7.configure(image=self.profiles)
                    self.username_label7['text'] = 'Username'
                elif count == 8:
                    self.pic_label8.configure(image=self.profiles)
                    self.username_label8['text'] = 'Username'

        def view_proggy_prof1():
            username = self.username_label1.cget('text')
            if username == "Username":
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x1000")
            newWindow.configure(bg='#33A1FD')
            query_data = cursor.fetchall()
            print(query_data)
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = "images/" + str(query_data[0][1][25:])
            except TypeError:
                filepath = "images/default_profile_img.png"
            self.load_prof_image = Image.open(filepath)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((150, 150), Image.ANTIALIAS))
            newWindow.profile_pic = tk.Label(newWindow, image=self.prof_image, bg='#33A1FD').pack(side='top')
            newWindow.code_lang = tk.Label(newWindow, text='', bg='#33A1FD', fg='black',font='Bahnschrift 14 bold')
            newWindow.code_lang.pack(side='top')
            coding_languages = query_data[0][12]
            coding_languages = coding_languages.split(',')
            code_text = '\n'.join(coding_languages[1:])
            newWindow.code_lang["text"] = code_text[:-1]
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.fullname = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold underline')
            newWindow.fullname.pack(side='top')
            newWindow.fullname["text"] = "Name: " + query_data[0][4]
            newWindow.age = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.age.pack(side='top')
            newWindow.age["text"] = str(query_data[0][6]) + " Years Old"
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
            newWindow.email = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.email.pack(side='top')
            newWindow.email["text"] = "Email: " + query_data[0][9]
            newWindow.github = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.github.pack(side='top')
            newWindow.github["text"] = "Github Username: " + query_data[0][10]
            newWindow.linkedIn = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.linkedIn.pack(side='top')
            newWindow.linkedIn["text"] = "LinkedIn URL: " + query_data[0][11]
            newWindow.field = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.field.pack(side='top')
            newWindow.field["text"] = "Specialization/Field of study: " + query_data[0][16]
            newWindow.fieldYrs = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.fieldYrs.pack(side='top')
            if query_data[0][17] > 1:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Years"
            else:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Year"
            connection.close()
        def view_proggy_prof2():
            username = self.username_label2.cget('text')
            if username == "Username":
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x1000")
            newWindow.configure(bg='#33A1FD')
            query_data = cursor.fetchall()
            print(query_data)
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = "images/" + str(query_data[0][1][25:])
            except TypeError:
                filepath = "images/default_profile_img.png"
            self.load_prof_image = Image.open(filepath)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((150, 150), Image.ANTIALIAS))
            newWindow.profile_pic = tk.Label(newWindow, image=self.prof_image, bg='#33A1FD').pack(side='top')
            newWindow.code_lang = tk.Label(newWindow, text='', bg='#33A1FD', fg='black',font='Bahnschrift 14 bold')
            newWindow.code_lang.pack(side='top')
            coding_languages = query_data[0][12]
            coding_languages = coding_languages.split(',')
            code_text = '\n'.join(coding_languages[1:])
            newWindow.code_lang["text"] = code_text[:-1]
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.fullname = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold underline')
            newWindow.fullname.pack(side='top')
            newWindow.fullname["text"] = "Name: " + query_data[0][4]
            newWindow.age = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.age.pack(side='top')
            newWindow.age["text"] = str(query_data[0][6]) + " Years Old"
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
            newWindow.email = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.email.pack(side='top')
            newWindow.email["text"] = "Email: " + query_data[0][9]
            newWindow.github = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.github.pack(side='top')
            newWindow.github["text"] = "Github Username: " + query_data[0][10]
            newWindow.linkedIn = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.linkedIn.pack(side='top')
            newWindow.linkedIn["text"] = "LinkedIn URL: " + query_data[0][11]
            newWindow.field = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.field.pack(side='top')
            newWindow.field["text"] = "Specialization/Field of study: " + query_data[0][16]
            newWindow.fieldYrs = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.fieldYrs.pack(side='top')
            if query_data[0][17] > 1:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Years"
            else:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Year"
            connection.close()
        def view_proggy_prof3():
            username = self.username_label3.cget('text')
            if username == "Username":
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x1000")
            newWindow.configure(bg='#33A1FD')
            query_data = cursor.fetchall()
            print(query_data)
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = "images/" + str(query_data[0][1][25:])
            except TypeError:
                filepath = "images/default_profile_img.png"
            self.load_prof_image = Image.open(filepath)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((150, 150), Image.ANTIALIAS))
            newWindow.profile_pic = tk.Label(newWindow, image=self.prof_image, bg='#33A1FD').pack(side='top')
            newWindow.code_lang = tk.Label(newWindow, text='', bg='#33A1FD', fg='black',font='Bahnschrift 14 bold')
            newWindow.code_lang.pack(side='top')
            coding_languages = query_data[0][12]
            coding_languages = coding_languages.split(',')
            code_text = '\n'.join(coding_languages[1:])
            newWindow.code_lang["text"] = code_text[:-1]
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.fullname = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold underline')
            newWindow.fullname.pack(side='top')
            newWindow.fullname["text"] = "Name: " + query_data[0][4]
            newWindow.age = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.age.pack(side='top')
            newWindow.age["text"] = str(query_data[0][6]) + " Years Old"
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
            newWindow.email = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.email.pack(side='top')
            newWindow.email["text"] = "Email: " + query_data[0][9]
            newWindow.github = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.github.pack(side='top')
            newWindow.github["text"] = "Github Username: " + query_data[0][10]
            newWindow.linkedIn = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.linkedIn.pack(side='top')
            newWindow.linkedIn["text"] = "LinkedIn URL: " + query_data[0][11]
            newWindow.field = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.field.pack(side='top')
            newWindow.field["text"] = "Specialization/Field of study: " + query_data[0][16]
            newWindow.fieldYrs = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.fieldYrs.pack(side='top')
            if query_data[0][17] > 1:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Years"
            else:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Year"
            connection.close()
        def view_proggy_prof4():
            username = self.username_label4.cget('text')
            if username == "Username":
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x1000")
            newWindow.configure(bg='#33A1FD')
            query_data = cursor.fetchall()
            print(query_data)
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = "images/" + str(query_data[0][1][25:])
            except TypeError:
                filepath = "images/default_profile_img.png"
            self.load_prof_image = Image.open(filepath)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((150, 150), Image.ANTIALIAS))
            newWindow.profile_pic = tk.Label(newWindow, image=self.prof_image, bg='#33A1FD').pack(side='top')
            newWindow.code_lang = tk.Label(newWindow, text='', bg='#33A1FD', fg='black',font='Bahnschrift 14 bold')
            newWindow.code_lang.pack(side='top')
            coding_languages = query_data[0][12]
            coding_languages = coding_languages.split(',')
            code_text = '\n'.join(coding_languages[1:])
            newWindow.code_lang["text"] = code_text[:-1]
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.fullname = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold underline')
            newWindow.fullname.pack(side='top')
            newWindow.fullname["text"] = "Name: " + query_data[0][4]
            newWindow.age = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.age.pack(side='top')
            newWindow.age["text"] = str(query_data[0][6]) + " Years Old"
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
            newWindow.email = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.email.pack(side='top')
            newWindow.email["text"] = "Email: " + query_data[0][9]
            newWindow.github = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.github.pack(side='top')
            newWindow.github["text"] = "Github Username: " + query_data[0][10]
            newWindow.linkedIn = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.linkedIn.pack(side='top')
            newWindow.linkedIn["text"] = "LinkedIn URL: " + query_data[0][11]
            newWindow.field = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.field.pack(side='top')
            newWindow.field["text"] = "Specialization/Field of study: " + query_data[0][16]
            newWindow.fieldYrs = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.fieldYrs.pack(side='top')
            if query_data[0][17] > 1:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Years"
            else:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Year"
            connection.close()
        def view_proggy_prof5():
            username = self.username_label5.cget('text')
            if username == "Username":
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x1000")
            newWindow.configure(bg='#33A1FD')
            query_data = cursor.fetchall()
            print(query_data)
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = "images/" + str(query_data[0][1][25:])
            except TypeError:
                filepath = "images/default_profile_img.png"
            self.load_prof_image = Image.open(filepath)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((150, 150), Image.ANTIALIAS))
            newWindow.profile_pic = tk.Label(newWindow, image=self.prof_image, bg='#33A1FD').pack(side='top')
            newWindow.code_lang = tk.Label(newWindow, text='', bg='#33A1FD', fg='black',font='Bahnschrift 14 bold')
            newWindow.code_lang.pack(side='top')
            coding_languages = query_data[0][12]
            coding_languages = coding_languages.split(',')
            code_text = '\n'.join(coding_languages[1:])
            newWindow.code_lang["text"] = code_text[:-1]
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.fullname = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold underline')
            newWindow.fullname.pack(side='top')
            newWindow.fullname["text"] = "Name: " + query_data[0][4]
            newWindow.age = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.age.pack(side='top')
            newWindow.age["text"] = str(query_data[0][6]) + " Years Old"
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
            newWindow.email = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.email.pack(side='top')
            newWindow.email["text"] = "Email: " + query_data[0][9]
            newWindow.github = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.github.pack(side='top')
            newWindow.github["text"] = "Github Username: " + query_data[0][10]
            newWindow.linkedIn = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.linkedIn.pack(side='top')
            newWindow.linkedIn["text"] = "LinkedIn URL: " + query_data[0][11]
            newWindow.field = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.field.pack(side='top')
            newWindow.field["text"] = "Specialization/Field of study: " + query_data[0][16]
            newWindow.fieldYrs = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.fieldYrs.pack(side='top')
            if query_data[0][17] > 1:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Years"
            else:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Year"
            connection.close()
        def view_proggy_prof6():
            username = self.username_label6.cget('text')
            if username == "Username":
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x1000")
            newWindow.configure(bg='#33A1FD')
            query_data = cursor.fetchall()
            print(query_data)
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = "images/" + str(query_data[0][1][25:])
            except TypeError:
                filepath = "images/default_profile_img.png"
            self.load_prof_image = Image.open(filepath)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((150, 150), Image.ANTIALIAS))
            newWindow.profile_pic = tk.Label(newWindow, image=self.prof_image, bg='#33A1FD').pack(side='top')
            newWindow.code_lang = tk.Label(newWindow, text='', bg='#33A1FD', fg='black',font='Bahnschrift 14 bold')
            newWindow.code_lang.pack(side='top')
            coding_languages = query_data[0][12]
            coding_languages = coding_languages.split(',')
            code_text = '\n'.join(coding_languages[1:])
            newWindow.code_lang["text"] = code_text[:-1]
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.fullname = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold underline')
            newWindow.fullname.pack(side='top')
            newWindow.fullname["text"] = "Name: " + query_data[0][4]
            newWindow.age = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.age.pack(side='top')
            newWindow.age["text"] = str(query_data[0][6]) + " Years Old"
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
            newWindow.email = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.email.pack(side='top')
            newWindow.email["text"] = "Email: " + query_data[0][9]
            newWindow.github = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.github.pack(side='top')
            newWindow.github["text"] = "Github Username: " + query_data[0][10]
            newWindow.linkedIn = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.linkedIn.pack(side='top')
            newWindow.linkedIn["text"] = "LinkedIn URL: " + query_data[0][11]
            newWindow.field = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.field.pack(side='top')
            newWindow.field["text"] = "Specialization/Field of study: " + query_data[0][16]
            newWindow.fieldYrs = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.fieldYrs.pack(side='top')
            if query_data[0][17] > 1:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Years"
            else:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Year"
            connection.close()
        def view_proggy_prof7():
            username = self.username_label7.cget('text')
            if username == "Username":
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x1000")
            newWindow.configure(bg='#33A1FD')
            query_data = cursor.fetchall()
            print(query_data)
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = "images/" + str(query_data[0][1][25:])
            except TypeError:
                filepath = "images/default_profile_img.png"
            self.load_prof_image = Image.open(filepath)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((150, 150), Image.ANTIALIAS))
            newWindow.profile_pic = tk.Label(newWindow, image=self.prof_image, bg='#33A1FD').pack(side='top')
            newWindow.code_lang = tk.Label(newWindow, text='', bg='#33A1FD', fg='black',font='Bahnschrift 14 bold')
            newWindow.code_lang.pack(side='top')
            coding_languages = query_data[0][12]
            coding_languages = coding_languages.split(',')
            code_text = '\n'.join(coding_languages[1:])
            newWindow.code_lang["text"] = code_text[:-1]
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.fullname = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold underline')
            newWindow.fullname.pack(side='top')
            newWindow.fullname["text"] = "Name: " + query_data[0][4]
            newWindow.age = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.age.pack(side='top')
            newWindow.age["text"] = str(query_data[0][6]) + " Years Old"
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
            newWindow.email = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.email.pack(side='top')
            newWindow.email["text"] = "Email: " + query_data[0][9]
            newWindow.github = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.github.pack(side='top')
            newWindow.github["text"] = "Github Username: " + query_data[0][10]
            newWindow.linkedIn = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.linkedIn.pack(side='top')
            newWindow.linkedIn["text"] = "LinkedIn URL: " + query_data[0][11]
            newWindow.field = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.field.pack(side='top')
            newWindow.field["text"] = "Specialization/Field of study: " + query_data[0][16]
            newWindow.fieldYrs = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.fieldYrs.pack(side='top')
            if query_data[0][17] > 1:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Years"
            else:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Year"
            connection.close()
        def view_proggy_prof8():
            username = self.username_label8.cget('text')
            if username == "Username":
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x1000")
            newWindow.configure(bg='#33A1FD')
            query_data = cursor.fetchall()
            print(query_data)
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = "images/" + str(query_data[0][1][25:])
            except TypeError:
                filepath = "images/default_profile_img.png"
            self.load_prof_image = Image.open(filepath)
            self.prof_image = ImageTk.PhotoImage(self.load_prof_image.resize((150, 150), Image.ANTIALIAS))
            newWindow.profile_pic = tk.Label(newWindow, image=self.prof_image, bg='#33A1FD').pack(side='top')
            newWindow.code_lang = tk.Label(newWindow, text='', bg='#33A1FD', fg='black',font='Bahnschrift 14 bold')
            newWindow.code_lang.pack(side='top')
            coding_languages = query_data[0][12]
            coding_languages = coding_languages.split(',')
            code_text = '\n'.join(coding_languages[1:])
            newWindow.code_lang["text"] = code_text[:-1]
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.fullname = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold underline')
            newWindow.fullname.pack(side='top')
            newWindow.fullname["text"] = "Name: " + query_data[0][4]
            newWindow.age = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.age.pack(side='top')
            newWindow.age["text"] = str(query_data[0][6]) + " Years Old"
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
            newWindow.email = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.email.pack(side='top')
            newWindow.email["text"] = "Email: " + query_data[0][9]
            newWindow.github = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.github.pack(side='top')
            newWindow.github["text"] = "Github Username: " + query_data[0][10]
            newWindow.linkedIn = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.linkedIn.pack(side='top')
            newWindow.linkedIn["text"] = "LinkedIn URL: " + query_data[0][11]
            newWindow.field = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.field.pack(side='top')
            newWindow.field["text"] = "Specialization/Field of study: " + query_data[0][16]
            newWindow.fieldYrs = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.fieldYrs.pack(side='top')
            if query_data[0][17] > 1:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Years"
            else:
                newWindow.fieldYrs["text"] = "Years in field/Specialization: " + str(query_data[0][17]) + " Year"
            connection.close()

        self.load_send_img = Image.open("images/send_message_icon.png")
        self.send_img = ImageTk.PhotoImage(self.load_send_img.resize((40, 40), Image.ANTIALIAS))
        def message_proggy1():
            username = self.username_label1.cget('text')
            if username == "Username":
                return
            file = open("Databases/logs.txt", "r")
            logged_in = file.read()
            file.close()
            logged_in = logged_in[:-1]
            sql = "Databases/" + logged_in + "_db.db"
            connection = sqlite3.connect(sql)
            chat_cursor = connection.cursor()
            chat_cursor.execute('SELECT chat_logs FROM Personal WHERE proggies = ?', [username])
            openWindow = tk.Toplevel(parent)
            openWindow.title("Chatting with " + username)
            openWindow.geometry("400x600")
            openWindow.configure(bg='#33A1FD')
            chat_log = chat_cursor.fetchall()[0]
            if chat_log == None:
                chat_log = ""
            openWindow.chat_scrolledtext = scrolledtext.ScrolledText(openWindow, wrap=tk.WORD, width=30, height=20,
                                                       font='Bahnschrift 16 bold', bd='3', relief='solid')
            openWindow.chat_scrolledtext.place(x=10, y=10)
            for line in chat_log:
                if line == None:
                    continue
                else:
                    openWindow.chat_scrolledtext.insert('insert', line)
            openWindow.chat_scrolledtext.configure(state='disabled')
            openWindow.chat_entry = tk.Entry(openWindow, font='Bahnschrift 20', bd='3', relief='solid', width=20)
            openWindow.chat_entry.place(x=10, y=530)
            def send_message():
                openWindow.chat_scrolledtext.configure(state="normal")
                sql = 'Databases/' + username + '_db.db'
                proggy_conn = sqlite3.connect(sql)
                proggy_cursor = proggy_conn.cursor()
                send_text = "\n" + logged_in + ": " + str(openWindow.chat_entry.get())
                openWindow.chat_entry.delete(0, 'end')
                chat_log = openWindow.chat_scrolledtext.get("1.0", "end-1c")
                openWindow.chat_scrolledtext.delete('1.0', 'end')
                chat_log = chat_log + send_text
                openWindow.chat_scrolledtext.insert('end', chat_log)
                chat_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, username])
                connection.commit()
                proggy_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, logged_in])
                proggy_conn.commit()
                proggy_conn.close()
                openWindow.chat_scrolledtext.configure(state="disabled")
            openWindow.chat_send = tk.Button(openWindow, image=self.send_img, bg="#FDCA40", bd="3", relief="raised", command=send_message)
            openWindow.chat_send.place(x=330, y=527)
        def message_proggy2():
            username = self.username_label2.cget('text')
            if username == "Username":
                return
            file = open("Databases/logs.txt", "r")
            logged_in = file.read()
            file.close()
            logged_in = logged_in[:-1]
            sql = "Databases/" + logged_in + "_db.db"
            connection = sqlite3.connect(sql)
            chat_cursor = connection.cursor()
            chat_cursor.execute('SELECT chat_logs FROM Personal WHERE proggies = ?', [username])
            openWindow = tk.Toplevel(parent)
            openWindow.title("Chatting with " + username)
            openWindow.geometry("400x600")
            openWindow.configure(bg='#33A1FD')
            chat_log = chat_cursor.fetchall()[0]
            if chat_log == None:
                chat_log = ""
            openWindow.chat_scrolledtext = scrolledtext.ScrolledText(openWindow, wrap=tk.WORD, width=30, height=20,
                                                       font='Bahnschrift 16 bold', bd='3', relief='solid')
            openWindow.chat_scrolledtext.place(x=10, y=10)
            for line in chat_log:
                if line == None:
                    continue
                else:
                    openWindow.chat_scrolledtext.insert('insert', line)
            openWindow.chat_scrolledtext.configure(state='disabled')
            openWindow.chat_entry = tk.Entry(openWindow, font='Bahnschrift 20', bd='3', relief='solid', width=20)
            openWindow.chat_entry.place(x=10, y=530)
            def send_message():
                openWindow.chat_scrolledtext.configure(state="normal")
                sql = 'Databases/' + username + '_db.db'
                proggy_conn = sqlite3.connect(sql)
                proggy_cursor = proggy_conn.cursor()
                send_text = "\n" + logged_in + ": " + str(openWindow.chat_entry.get())
                openWindow.chat_entry.delete(0, 'end')
                chat_log = openWindow.chat_scrolledtext.get("1.0", "end-1c")
                openWindow.chat_scrolledtext.delete('1.0', 'end')
                chat_log = chat_log + send_text
                openWindow.chat_scrolledtext.insert('end', chat_log)
                chat_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, username])
                connection.commit()
                proggy_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, logged_in])
                proggy_conn.commit()
                proggy_conn.close()
                openWindow.chat_scrolledtext.configure(state="disabled")
            openWindow.chat_send = tk.Button(openWindow, image=self.send_img, bg="#FDCA40", bd="3", relief="raised", command=send_message)
            openWindow.chat_send.place(x=330, y=527)
        def message_proggy3():
            username = self.username_label3.cget('text')
            if username == "Username":
                return
            file = open("Databases/logs.txt", "r")
            logged_in = file.read()
            file.close()
            logged_in = logged_in[:-1]
            sql = "Databases/" + logged_in + "_db.db"
            connection = sqlite3.connect(sql)
            chat_cursor = connection.cursor()
            chat_cursor.execute('SELECT chat_logs FROM Personal WHERE proggies = ?', [username])
            openWindow = tk.Toplevel(parent)
            openWindow.title("Chatting with " + username)
            openWindow.geometry("400x600")
            openWindow.configure(bg='#33A1FD')
            chat_log = chat_cursor.fetchall()[0]
            if chat_log == None:
                chat_log = ""
            openWindow.chat_scrolledtext = scrolledtext.ScrolledText(openWindow, wrap=tk.WORD, width=30, height=20,
                                                       font='Bahnschrift 16 bold', bd='3', relief='solid')
            openWindow.chat_scrolledtext.place(x=10, y=10)
            for line in chat_log:
                if line == None:
                    continue
                else:
                    openWindow.chat_scrolledtext.insert('insert', line)
            openWindow.chat_scrolledtext.configure(state='disabled')
            openWindow.chat_entry = tk.Entry(openWindow, font='Bahnschrift 20', bd='3', relief='solid', width=20)
            openWindow.chat_entry.place(x=10, y=530)
            def send_message():
                openWindow.chat_scrolledtext.configure(state="normal")
                sql = 'Databases/' + username + '_db.db'
                proggy_conn = sqlite3.connect(sql)
                proggy_cursor = proggy_conn.cursor()
                send_text = "\n" + logged_in + ": " + str(openWindow.chat_entry.get())
                openWindow.chat_entry.delete(0, 'end')
                chat_log = openWindow.chat_scrolledtext.get("1.0", "end-1c")
                openWindow.chat_scrolledtext.delete('1.0', 'end')
                chat_log = chat_log + send_text
                openWindow.chat_scrolledtext.insert('end', chat_log)
                chat_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, username])
                connection.commit()
                proggy_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, logged_in])
                proggy_conn.commit()
                proggy_conn.close()
                openWindow.chat_scrolledtext.configure(state="disabled")
            openWindow.chat_send = tk.Button(openWindow, image=self.send_img, bg="#FDCA40", bd="3", relief="raised", command=send_message)
            openWindow.chat_send.place(x=330, y=527)
        def message_proggy4():
            username = self.username_label4.cget('text')
            if username == "Username":
                return
            file = open("Databases/logs.txt", "r")
            logged_in = file.read()
            file.close()
            logged_in = logged_in[:-1]
            sql = "Databases/" + logged_in + "_db.db"
            connection = sqlite3.connect(sql)
            chat_cursor = connection.cursor()
            chat_cursor.execute('SELECT chat_logs FROM Personal WHERE proggies = ?', [username])
            openWindow = tk.Toplevel(parent)
            openWindow.title("Chatting with " + username)
            openWindow.geometry("400x600")
            openWindow.configure(bg='#33A1FD')
            chat_log = chat_cursor.fetchall()[0]
            if chat_log == None:
                chat_log = ""
            openWindow.chat_scrolledtext = scrolledtext.ScrolledText(openWindow, wrap=tk.WORD, width=30, height=20,
                                                       font='Bahnschrift 16 bold', bd='3', relief='solid')
            openWindow.chat_scrolledtext.place(x=10, y=10)
            for line in chat_log:
                if line == None:
                    continue
                else:
                    openWindow.chat_scrolledtext.insert('insert', line)
            openWindow.chat_scrolledtext.configure(state='disabled')
            openWindow.chat_entry = tk.Entry(openWindow, font='Bahnschrift 20', bd='3', relief='solid', width=20)
            openWindow.chat_entry.place(x=10, y=530)
            def send_message():
                openWindow.chat_scrolledtext.configure(state="normal")
                sql = 'Databases/' + username + '_db.db'
                proggy_conn = sqlite3.connect(sql)
                proggy_cursor = proggy_conn.cursor()
                send_text = "\n" + logged_in + ": " + str(openWindow.chat_entry.get())
                openWindow.chat_entry.delete(0, 'end')
                chat_log = openWindow.chat_scrolledtext.get("1.0", "end-1c")
                openWindow.chat_scrolledtext.delete('1.0', 'end')
                chat_log = chat_log + send_text
                openWindow.chat_scrolledtext.insert('end', chat_log)
                chat_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, username])
                connection.commit()
                proggy_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, logged_in])
                proggy_conn.commit()
                proggy_conn.close()
                openWindow.chat_scrolledtext.configure(state="disabled")
            openWindow.chat_send = tk.Button(openWindow, image=self.send_img, bg="#FDCA40", bd="3", relief="raised", command=send_message)
            openWindow.chat_send.place(x=330, y=527)
        def message_proggy5():
            username = self.username_label5.cget('text')
            if username == "Username":
                return
            file = open("Databases/logs.txt", "r")
            logged_in = file.read()
            file.close()
            logged_in = logged_in[:-1]
            sql = "Databases/" + logged_in + "_db.db"
            connection = sqlite3.connect(sql)
            chat_cursor = connection.cursor()
            chat_cursor.execute('SELECT chat_logs FROM Personal WHERE proggies = ?', [username])
            openWindow = tk.Toplevel(parent)
            openWindow.title("Chatting with " + username)
            openWindow.geometry("400x600")
            openWindow.configure(bg='#33A1FD')
            chat_log = chat_cursor.fetchall()[0]
            if chat_log == None:
                chat_log = ""
            openWindow.chat_scrolledtext = scrolledtext.ScrolledText(openWindow, wrap=tk.WORD, width=30, height=20,
                                                       font='Bahnschrift 16 bold', bd='3', relief='solid')
            openWindow.chat_scrolledtext.place(x=10, y=10)
            for line in chat_log:
                if line == None:
                    continue
                else:
                    openWindow.chat_scrolledtext.insert('insert', line)
            openWindow.chat_scrolledtext.configure(state='disabled')
            openWindow.chat_entry = tk.Entry(openWindow, font='Bahnschrift 20', bd='3', relief='solid', width=20)
            openWindow.chat_entry.place(x=10, y=530)
            def send_message():
                openWindow.chat_scrolledtext.configure(state="normal")
                sql = 'Databases/' + username + '_db.db'
                proggy_conn = sqlite3.connect(sql)
                proggy_cursor = proggy_conn.cursor()
                send_text = "\n" + logged_in + ": " + str(openWindow.chat_entry.get())
                openWindow.chat_entry.delete(0, 'end')
                chat_log = openWindow.chat_scrolledtext.get("1.0", "end-1c")
                openWindow.chat_scrolledtext.delete('1.0', 'end')
                chat_log = chat_log + send_text
                openWindow.chat_scrolledtext.insert('end', chat_log)
                chat_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, username])
                connection.commit()
                proggy_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, logged_in])
                proggy_conn.commit()
                proggy_conn.close()
                openWindow.chat_scrolledtext.configure(state="disabled")
            openWindow.chat_send = tk.Button(openWindow, image=self.send_img, bg="#FDCA40", bd="3", relief="raised", command=send_message)
            openWindow.chat_send.place(x=330, y=527)
        def message_proggy6():
            username = self.username_label6.cget('text')
            if username == "Username":
                return
            file = open("Databases/logs.txt", "r")
            logged_in = file.read()
            file.close()
            logged_in = logged_in[:-1]
            sql = "Databases/" + logged_in + "_db.db"
            connection = sqlite3.connect(sql)
            chat_cursor = connection.cursor()
            chat_cursor.execute('SELECT chat_logs FROM Personal WHERE proggies = ?', [username])
            openWindow = tk.Toplevel(parent)
            openWindow.title("Chatting with " + username)
            openWindow.geometry("400x600")
            openWindow.configure(bg='#33A1FD')
            chat_log = chat_cursor.fetchall()[0]
            if chat_log == None:
                chat_log = ""
            openWindow.chat_scrolledtext = scrolledtext.ScrolledText(openWindow, wrap=tk.WORD, width=30, height=20,
                                                       font='Bahnschrift 16 bold', bd='3', relief='solid')
            openWindow.chat_scrolledtext.place(x=10, y=10)
            for line in chat_log:
                if line == None:
                    continue
                else:
                    openWindow.chat_scrolledtext.insert('insert', line)
            openWindow.chat_scrolledtext.configure(state='disabled')
            openWindow.chat_entry = tk.Entry(openWindow, font='Bahnschrift 20', bd='3', relief='solid', width=20)
            openWindow.chat_entry.place(x=10, y=530)
            def send_message():
                openWindow.chat_scrolledtext.configure(state="normal")
                sql = 'Databases/' + username + '_db.db'
                proggy_conn = sqlite3.connect(sql)
                proggy_cursor = proggy_conn.cursor()
                send_text = "\n" + logged_in + ": " + str(openWindow.chat_entry.get())
                openWindow.chat_entry.delete(0, 'end')
                chat_log = openWindow.chat_scrolledtext.get("1.0", "end-1c")
                openWindow.chat_scrolledtext.delete('1.0', 'end')
                chat_log = chat_log + send_text
                openWindow.chat_scrolledtext.insert('end', chat_log)
                chat_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, username])
                connection.commit()
                proggy_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, logged_in])
                proggy_conn.commit()
                proggy_conn.close()
                openWindow.chat_scrolledtext.configure(state="disabled")
            openWindow.chat_send = tk.Button(openWindow, image=self.send_img, bg="#FDCA40", bd="3", relief="raised", command=send_message)
            openWindow.chat_send.place(x=330, y=527)
        def message_proggy7():
            username = self.username_label7.cget('text')
            if username == "Username":
                return
            file = open("Databases/logs.txt", "r")
            logged_in = file.read()
            file.close()
            logged_in = logged_in[:-1]
            sql = "Databases/" + logged_in + "_db.db"
            connection = sqlite3.connect(sql)
            chat_cursor = connection.cursor()
            chat_cursor.execute('SELECT chat_logs FROM Personal WHERE proggies = ?', [username])
            openWindow = tk.Toplevel(parent)
            openWindow.title("Chatting with " + username)
            openWindow.geometry("400x600")
            openWindow.configure(bg='#33A1FD')
            chat_log = chat_cursor.fetchall()[0]
            if chat_log == None:
                chat_log = ""
            openWindow.chat_scrolledtext = scrolledtext.ScrolledText(openWindow, wrap=tk.WORD, width=30, height=20,
                                                       font='Bahnschrift 16 bold', bd='3', relief='solid')
            openWindow.chat_scrolledtext.place(x=10, y=10)
            for line in chat_log:
                if line == None:
                    continue
                else:
                    openWindow.chat_scrolledtext.insert('insert', line)
            openWindow.chat_scrolledtext.configure(state='disabled')
            openWindow.chat_entry = tk.Entry(openWindow, font='Bahnschrift 20', bd='3', relief='solid', width=20)
            openWindow.chat_entry.place(x=10, y=530)
            def send_message():
                openWindow.chat_scrolledtext.configure(state="normal")
                sql = 'Databases/' + username + '_db.db'
                proggy_conn = sqlite3.connect(sql)
                proggy_cursor = proggy_conn.cursor()
                send_text = "\n" + logged_in + ": " + str(openWindow.chat_entry.get())
                openWindow.chat_entry.delete(0, 'end')
                chat_log = openWindow.chat_scrolledtext.get("1.0", "end-1c")
                openWindow.chat_scrolledtext.delete('1.0', 'end')
                chat_log = chat_log + send_text
                openWindow.chat_scrolledtext.insert('end', chat_log)
                chat_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, username])
                connection.commit()
                proggy_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, logged_in])
                proggy_conn.commit()
                proggy_conn.close()
                openWindow.chat_scrolledtext.configure(state="disabled")
            openWindow.chat_send = tk.Button(openWindow, image=self.send_img, bg="#FDCA40", bd="3", relief="raised", command=send_message)
            openWindow.chat_send.place(x=330, y=527)
        def message_proggy8():
            username = self.username_label8.cget('text')
            if username == "Username":
                return
            file = open("Databases/logs.txt", "r")
            logged_in = file.read()
            file.close()
            logged_in = logged_in[:-1]
            sql = "Databases/" + logged_in + "_db.db"
            connection = sqlite3.connect(sql)
            chat_cursor = connection.cursor()
            chat_cursor.execute('SELECT chat_logs FROM Personal WHERE proggies = ?', [username])
            openWindow = tk.Toplevel(parent)
            openWindow.title("Chatting with " + username)
            openWindow.geometry("400x600")
            openWindow.configure(bg='#33A1FD')
            chat_log = chat_cursor.fetchall()[0]
            if chat_log == None:
                chat_log = ""
            openWindow.chat_scrolledtext = scrolledtext.ScrolledText(openWindow, wrap=tk.WORD, width=30, height=20,
                                                       font='Bahnschrift 16 bold', bd='3', relief='solid')
            openWindow.chat_scrolledtext.place(x=10, y=10)
            for line in chat_log:
                if line == None:
                    continue
                else:
                    openWindow.chat_scrolledtext.insert('insert', line)
            openWindow.chat_scrolledtext.configure(state='disabled')
            openWindow.chat_entry = tk.Entry(openWindow, font='Bahnschrift 20', bd='3', relief='solid', width=20)
            openWindow.chat_entry.place(x=10, y=530)
            def send_message():
                openWindow.chat_scrolledtext.configure(state="normal")
                sql = 'Databases/' + username + '_db.db'
                proggy_conn = sqlite3.connect(sql)
                proggy_cursor = proggy_conn.cursor()
                send_text = "\n" + logged_in + ": " + str(openWindow.chat_entry.get())
                openWindow.chat_entry.delete(0, 'end')
                chat_log = openWindow.chat_scrolledtext.get("1.0", "end-1c")
                openWindow.chat_scrolledtext.delete('1.0', 'end')
                chat_log = chat_log + send_text
                openWindow.chat_scrolledtext.insert('end', chat_log)
                chat_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, username])
                connection.commit()
                proggy_cursor.execute('UPDATE Personal SET chat_logs = ? WHERE proggies = ?',[chat_log, logged_in])
                proggy_conn.commit()
                proggy_conn.close()
                openWindow.chat_scrolledtext.configure(state="disabled")
            openWindow.chat_send = tk.Button(openWindow, image=self.send_img, bg="#FDCA40", bd="3", relief="raised", command=send_message)
            openWindow.chat_send.place(x=330, y=527)

        self.backdrop1 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, text="",
                                                corner_radius=20, width=400, height=100)
        self.pic_label1 = tk.Label(self, image=self.profiles, bg=accentColour)
        self.username_label1 = tk.Label(self, text='Username', bg=accentColour, font='Bahnschrift 18 underline bold')
        self.view_prof_btn1 = customtkinter.CTkButton(self, image=self.view_prof_image, bg_color=accentColour, width=50,
                                                      fg_color=accentColour2, text="", command=view_proggy_prof1)
        self.delete_btn1 = customtkinter.CTkButton(self, image=self.deletes, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=remove_proggy1)
        self.message_btn1 = customtkinter.CTkButton(self, image=self.messages, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=message_proggy1)

        self.backdrop2 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, text="",
                                                corner_radius=20, width=400, height=100)
        self.pic_label2 = tk.Label(self, image=self.profiles, bg=accentColour)
        self.username_label2 = tk.Label(self, text='Username', bg=accentColour, font='Bahnschrift 18 underline bold')
        self.view_prof_btn2 = customtkinter.CTkButton(self, image=self.view_prof_image, bg_color=accentColour, width=50,
                                                      fg_color=accentColour2, text="", command=view_proggy_prof2)
        self.delete_btn2 = customtkinter.CTkButton(self, image=self.deletes, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=remove_proggy2)
        self.message_btn2 = customtkinter.CTkButton(self, image=self.messages, bg_color=accentColour, width=50,
                                                    fg_color=accentColour2, text="", command=message_proggy2)

        self.backdrop3 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, text="",
                                                corner_radius=20, width=400, height=100)
        self.pic_label3 = tk.Label(self, image=self.profiles, bg=accentColour)
        self.username_label3 = tk.Label(self, text='Username', bg=accentColour, font='Bahnschrift 18 underline bold')
        self.view_prof_btn3 = customtkinter.CTkButton(self, image=self.view_prof_image, bg_color=accentColour, width=50,
                                                      fg_color=accentColour2, text="", command=view_proggy_prof3)
        self.delete_btn3 = customtkinter.CTkButton(self, image=self.deletes, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=remove_proggy3)
        self.message_btn3 = customtkinter.CTkButton(self, image=self.messages, bg_color=accentColour, width=50,
                                                    fg_color=accentColour2, text="", command=message_proggy3)

        self.backdrop4 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, text="",
                                                corner_radius=20, width=400, height=100)
        self.pic_label4 = tk.Label(self, image=self.profiles, bg=accentColour)
        self.username_label4 = tk.Label(self, text='Username', bg=accentColour, font='Bahnschrift 18 underline bold')
        self.view_prof_btn4 = customtkinter.CTkButton(self, image=self.view_prof_image, bg_color=accentColour, width=50,
                                                      fg_color=accentColour2, text="", command=view_proggy_prof4)
        self.delete_btn4 = customtkinter.CTkButton(self, image=self.deletes, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=remove_proggy4)
        self.message_btn4 = customtkinter.CTkButton(self, image=self.messages, bg_color=accentColour, width=50,
                                                    fg_color=accentColour2, text="", command=message_proggy4)

        self.backdrop5 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, text="",
                                                corner_radius=20, width=400, height=100)
        self.pic_label5 = tk.Label(self, image=self.profiles, bg=accentColour)
        self.username_label5 = tk.Label(self, text='Username', bg=accentColour, font='Bahnschrift 18 underline bold')
        self.view_prof_btn5 = customtkinter.CTkButton(self, image=self.view_prof_image, bg_color=accentColour, width=50,
                                                      fg_color=accentColour2, text="", command=view_proggy_prof5)
        self.delete_btn5 = customtkinter.CTkButton(self, image=self.deletes, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=remove_proggy5)
        self.message_btn5 = customtkinter.CTkButton(self, image=self.messages, bg_color=accentColour, width=50,
                                                    fg_color=accentColour2, text="", command=message_proggy5)

        self.backdrop6 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, text="",
                                                corner_radius=20, width=400, height=100)
        self.pic_label6 = tk.Label(self, image=self.profiles, bg=accentColour)
        self.username_label6 = tk.Label(self, text='Username', bg=accentColour, font='Bahnschrift 18 underline bold')
        self.view_prof_btn6 = customtkinter.CTkButton(self, image=self.view_prof_image, bg_color=accentColour, width=50,
                                                      fg_color=accentColour2, text="", command=view_proggy_prof6)
        self.delete_btn6 = customtkinter.CTkButton(self, image=self.deletes, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=remove_proggy6)
        self.message_btn6 = customtkinter.CTkButton(self, image=self.messages, bg_color=accentColour, width=50,
                                                    fg_color=accentColour2, text="", command=message_proggy6)

        self.backdrop7 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, text="",
                                                corner_radius=20, width=400, height=100)
        self.pic_label7 = tk.Label(self, image=self.profiles, bg=accentColour)
        self.username_label7 = tk.Label(self, text='Username', bg=accentColour, font='Bahnschrift 18 underline bold')
        self.view_prof_btn7 = customtkinter.CTkButton(self, image=self.view_prof_image, bg_color=accentColour, width=50,
                                                      fg_color=accentColour2, text="", command=view_proggy_prof7)
        self.delete_btn7 = customtkinter.CTkButton(self, image=self.deletes, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=remove_proggy7)
        self.message_btn7 = customtkinter.CTkButton(self, image=self.messages, bg_color=accentColour, width=50,
                                                    fg_color=accentColour2, text="", command=message_proggy7)

        self.backdrop8 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, text="",
                                                corner_radius=20, width=400, height=100)
        self.pic_label8 = tk.Label(self, image=self.profiles, bg=accentColour)
        self.username_label8 = tk.Label(self, text='Username', bg=accentColour, font='Bahnschrift 18 underline bold')
        self.view_prof_btn8 = customtkinter.CTkButton(self, image=self.view_prof_image, bg_color=accentColour, width=50,
                                                      fg_color=accentColour2, text="", command=view_proggy_prof8)
        self.delete_btn8 = customtkinter.CTkButton(self, image=self.deletes, bg_color=accentColour, width=50,
                                                   fg_color=accentColour2, text="", command=remove_proggy8)
        self.message_btn8 = customtkinter.CTkButton(self, image=self.messages, bg_color=accentColour, width=50,
                                                    fg_color=accentColour2, text="", command=message_proggy8)

        # arrange elements & widgets in grid
        self.recs_btn.place(x=2, y=2)
        self.search_btn.place(x=158, y=2)
        self.events_btn.place(x=300, y=2)
        self.contacts_btn.place(x=442, y=2)
        self.profile_btn.place(x=584, y=2)

        self.requests.place(x=1100, y=200)
        self.proggies.place(x=1100, y=330)
        self.block_label.place(x=0, y=270)
        self.block_label.tkraise()

        #column1
        self.backdrop1.place(x=130, y=190)
        self.pic_label1.place(x=210, y=310)
        self.username_label1.place(x=325, y=330)
        self.view_prof_btn1.place(x=350, y=220)
        self.delete_btn1.place(x=410, y=220)
        self.message_btn1.place(x=470, y=220)

        self.backdrop2.place(x=130, y=310)
        self.pic_label2.place(x=210, y=490)
        self.username_label2.place(x=325, y=510)
        self.view_prof_btn2.place(x=350, y=340)
        self.delete_btn2.place(x=410, y=340)
        self.message_btn2.place(x=470, y=340)

        self.backdrop3.place(x=130, y=430)
        self.pic_label3.place(x=210, y=670)
        self.username_label3.place(x=325, y=690)
        self.view_prof_btn3.place(x=350, y=460)
        self.delete_btn3.place(x=410, y=460)
        self.message_btn3.place(x=470, y=460)

        self.backdrop4.place(x=130, y=550)
        self.pic_label4.place(x=210, y=850)
        self.username_label4.place(x=325, y=870)
        self.view_prof_btn4.place(x=350, y=580)
        self.delete_btn4.place(x=410, y=580)
        self.message_btn4.place(x=470, y=580)

        self.backdrop5.place(x=600, y=190)
        self.pic_label5.place(x=915, y=310)
        self.username_label5.place(x=1030, y=330)
        self.view_prof_btn5.place(x=820, y=220)
        self.delete_btn5.place(x=880, y=220)
        self.message_btn5.place(x=940, y=220)

        self.backdrop6.place(x=600, y=310)
        self.pic_label6.place(x=915, y=490)
        self.username_label6.place(x=1030, y=510)
        self.view_prof_btn6.place(x=820, y=340)
        self.delete_btn6.place(x=880, y=340)
        self.message_btn6.place(x=940, y=340)

        self.backdrop7.place(x=600, y=430)
        self.pic_label7.place(x=915, y=670)
        self.username_label7.place(x=1030, y=690)
        self.view_prof_btn7.place(x=820, y=460)
        self.delete_btn7.place(x=880, y=460)
        self.message_btn7.place(x=940, y=460)

        self.backdrop8.place(x=600, y=550)
        self.pic_label8.place(x=915, y=850)
        self.username_label8.place(x=1030, y=870)
        self.view_prof_btn8.place(x=820, y=580)
        self.delete_btn8.place(x=880, y=580)
        self.message_btn8.place(x=940, y=580)