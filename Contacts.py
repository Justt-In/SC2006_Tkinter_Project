import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

class Contacts_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller
        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg="#ff8c1a", borderwidth=2, relief='solid')
        #This function updates the contacts list and changes view to the recommendations page
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

        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="#ff8c1a", bd="3", height=130, relief="raised",
                                  command=goto_recs)
        #This function updates the contacts list and changes view to the search page
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
                #print(picture[0][0][25:])
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

        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="#ff8c1a", bd="3", height=130,
                                    relief="raised", command=goto_search)
        #This function updates the contacts list and changes view to the events page
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

        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="#ff8c1a", bd="3", height=130,
                                    relief="raised", command=goto_events)
        #This function updates the contacts list and changes view to the contacts page (like refreshing the page)
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

        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="#ff8c1a", bd="3", height=130,
                                      relief="raised", command=goto_contacts)
        #This function updates the contacts list and changes view to the profile page
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

        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="#ff8c1a", bd="3", height=130,
                                     relief="raised", command=goto_profile)
        # End of Toolbar

        #Add elements and widgets
        self.load_backdrop = Image.open("images/backdrop3.png")
        self.load_message = Image.open("images/message_logo.png")
        self.load_delete = Image.open("images/delete_icon.png")
        self.load_user_image = Image.open("images/default_profile_img.png")
        self.load_view_prof_image = Image.open("images/view_prof_icon.png")
        self.backdrops = ImageTk.PhotoImage(self.load_backdrop.resize((500, 150), Image.ANTIALIAS))
        self.messages = ImageTk.PhotoImage(self.load_message.resize((55, 55), Image.ANTIALIAS))
        self.deletes = ImageTk.PhotoImage(self.load_delete.resize((55, 55), Image.ANTIALIAS))
        self.view_prof_image = ImageTk.PhotoImage(self.load_view_prof_image.resize((55, 55), Image.ANTIALIAS))
        self.profiles = ImageTk.PhotoImage(self.load_user_image.resize((100, 100), Image.ANTIALIAS))
        self.block_label = tk.Label(self, width=180, height=100, bg='blue')
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
                    print(name[0])
                    if name[0] == None:
                        noneCounter += 1
                if noneCounter == count:
                    tk.Label(newWindow, text='No requests yet, come back again later!', bg='yellow',
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
                        tk.Label(newWindow, text='No requests yet, come back again later!', bg='yellow', font='Bahnschrift 24 bold').grid(row=0, column=0)
                        return
                    self.resized_image[name] = ImageTk.PhotoImage(self.open_image[name].resize((200, 150), Image.ANTIALIAS))
                    self.picture[name] = tk.Label(newWindow, image=self.resized_image[name], bg='yellow', relief='solid').grid(row=name, column=0)
                    user = details[0][1]
                    user_list.append(user)
                    tk.Label(newWindow, text=user, font='Bahnschrift 24 bold', bg='yellow').grid(row=name, column=1)
                    self.accept[name] = Image.open('images/check_icon.png')
                    self.resized_accept[name] = ImageTk.PhotoImage(self.accept[name].resize((150, 150), Image.ANTIALIAS))
                    #This function will trigger when the logged in user accepts a request from the sender
                    def accept_request(btnName):
                        '''
                        if len(user_list) == 1:
                            adding = user_list[0]
                        else:
                            adding = user_list[btnName]
                        '''
                        for x in user_list:
                            adding = x
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
                    self.accept_button[name] = tk.Button(newWindow, bg='yellow', image=self.resized_accept[name], relief='solid', command= lambda text=name:accept_request(text)).grid(row=name,column=2)
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

                    self.decline_button[name] = tk.Button(newWindow, bg='yellow', image=self.resized_decline[name], relief='solid', command= lambda text=name:decline_request(text)).grid(row=name, column=3)
            #This function resets the scrollbar to the top of the page
            def onFrameConfigure(canvas):
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("700x500")
            canvas = tk.Canvas(root, borderwidth=0, background="yellow")
            frame = tk.Frame(canvas, background="yellow")
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
                    #print(name[0])
                    if name[0] == None:
                        break
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

        self.requests = tk.Button(self, image=self.requests_image, bg='#119975', command=view_requests, relief='solid')
        self.requests_label = tk.Label(self, text='View Invite\nRequests', font='Bahnschrift 16 bold', bg='blue', fg='white')
        self.load_proggies_image = Image.open("images/proggies_icon.png")
        self.proggies_image = ImageTk.PhotoImage(self.load_proggies_image.resize((100, 100), Image.ANTIALIAS))
        self.proggies = tk.Button(self, image=self.proggies_image, bg='#119975', command=view_proggies, relief='solid')
        self.proggies_label = tk.Label(self, text='View Your\nProggies', font='Bahnschrift 16 bold', bg='blue', fg='white')

        #This function allows the logged in user to remove a friend from their contacts list - friend 1
        def remove_proggy1():
            if self.username_label1.cget("text") == "Username":
                return
            MsgBox = tk.messagebox.askquestion('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == 'No':
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
            MsgBox = tk.messagebox.askquestion('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == 'No':
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
            MsgBox = tk.messagebox.askquestion('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == 'No':
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
            MsgBox = tk.messagebox.askquestion('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == 'No':
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
            MsgBox = tk.messagebox.askquestion('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == 'No':
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
            MsgBox = tk.messagebox.askquestion('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == 'No':
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
            MsgBox = tk.messagebox.askquestion('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == 'No':
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
            MsgBox = tk.messagebox.askquestion('Delete Proggy', 'Are you sure you want to delete this proggy?',icon='warning')
            if MsgBox == 'No':
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

        self.backdrop1 = tk.Label(self, image=self.backdrops, bg='blue')
        self.pic_label1 = tk.Label(self, image=self.profiles, bg='#119975')
        self.username_label1 = tk.Label(self, text='Username', bg='#119975', font='Bahnschrift 18 underline bold')
        self.view_prof_btn1 = tk.Button(self, image=self.view_prof_image, bg='#119975')
        self.delete_btn1 = tk.Button(self, image=self.deletes, bg='#119975', command=remove_proggy1)
        self.message_btn1 = tk.Button(self, image=self.messages, bg='#119975')

        self.backdrop2 = tk.Label(self, image=self.backdrops, bg='blue')
        self.pic_label2 = tk.Label(self, image=self.profiles, bg='#119975')
        self.username_label2 = tk.Label(self, text='Username', bg='#119975', font='Bahnschrift 18 underline bold')
        self.view_prof_btn2 = tk.Button(self, image=self.view_prof_image, bg='#119975')
        self.delete_btn2 = tk.Button(self, image=self.deletes, bg='#119975', command=remove_proggy2)
        self.message_btn2 = tk.Button(self, image=self.messages, bg='#119975')

        self.backdrop3 = tk.Label(self, image=self.backdrops, bg='blue')
        self.pic_label3 = tk.Label(self, image=self.profiles, bg='#119975')
        self.username_label3 = tk.Label(self, text='Username', bg='#119975', font='Bahnschrift 18 underline bold')
        self.view_prof_btn3 = tk.Button(self, image=self.view_prof_image, bg='#119975')
        self.delete_btn3 = tk.Button(self, image=self.deletes, bg='#119975', command=remove_proggy3)
        self.message_btn3 = tk.Button(self, image=self.messages, bg='#119975')

        self.backdrop4 = tk.Label(self, image=self.backdrops, bg='blue')
        self.pic_label4 = tk.Label(self, image=self.profiles, bg='#119975')
        self.username_label4 = tk.Label(self, text='Username', bg='#119975', font='Bahnschrift 18 underline bold')
        self.view_prof_btn4 = tk.Button(self, image=self.view_prof_image, bg='#119975')
        self.delete_btn4 = tk.Button(self, image=self.deletes, bg='#119975', command=remove_proggy4)
        self.message_btn4 = tk.Button(self, image=self.messages, bg='#119975')

        self.backdrop5 = tk.Label(self, image=self.backdrops, bg='blue')
        self.pic_label5 = tk.Label(self, image=self.profiles, bg='#119975')
        self.username_label5 = tk.Label(self, text='Username', bg='#119975', font='Bahnschrift 18 underline bold')
        self.view_prof_btn5 = tk.Button(self, image=self.view_prof_image, bg='#119975')
        self.delete_btn5 = tk.Button(self, image=self.deletes, bg='#119975', command=remove_proggy5)
        self.message_btn5 = tk.Button(self, image=self.messages, bg='#119975')

        self.backdrop6 = tk.Label(self, image=self.backdrops, bg='blue')
        self.pic_label6 = tk.Label(self, image=self.profiles, bg='#119975')
        self.username_label6 = tk.Label(self, text='Username', bg='#119975', font='Bahnschrift 18 underline bold')
        self.view_prof_btn6 = tk.Button(self, image=self.view_prof_image, bg='#119975')
        self.delete_btn6 = tk.Button(self, image=self.deletes, bg='#119975', command=remove_proggy6)
        self.message_btn6 = tk.Button(self, image=self.messages, bg='#119975')

        self.backdrop7 = tk.Label(self, image=self.backdrops, bg='blue')
        self.pic_label7 = tk.Label(self, image=self.profiles, bg='#119975')
        self.username_label7 = tk.Label(self, text='Username', bg='#119975', font='Bahnschrift 18 underline bold')
        self.view_prof_btn7 = tk.Button(self, image=self.view_prof_image, bg='#119975')
        self.delete_btn7 = tk.Button(self, image=self.deletes, bg='#119975', command=remove_proggy7)
        self.message_btn7 = tk.Button(self, image=self.messages, bg='#119975')

        self.backdrop8 = tk.Label(self, image=self.backdrops, bg='blue')
        self.pic_label8 = tk.Label(self, image=self.profiles, bg='#119975')
        self.username_label8 = tk.Label(self, text='Username', bg='#119975', font='Bahnschrift 18 underline bold')
        self.view_prof_btn8 = tk.Button(self, image=self.view_prof_image, bg='#119975')
        self.delete_btn8 = tk.Button(self, image=self.deletes, bg='#119975', command=remove_proggy8)
        self.message_btn8 = tk.Button(self, image=self.messages, bg='#119975')

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
        self.requests.place(x=1300, y=150)
        self.requests_label.place(x=1300, y=270)
        self.proggies.place(x=1300, y=350)
        self.proggies_label.place(x=1300, y=470)
        self.block_label.place(x=0, y=150)
        self.block_label.tkraise()
        #column1
        self.backdrop1.place(x=190, y=160)
        self.pic_label1.place(x=220, y=185)
        self.username_label1.place(x=370, y=205)
        self.view_prof_btn1.place(x=505, y=200)
        self.delete_btn1.place(x=570, y=175)
        self.message_btn1.place(x=570, y=240)

        self.backdrop2.place(x=190, y=320)
        self.pic_label2.place(x=220, y=345)
        self.username_label2.place(x=370, y=365)
        self.view_prof_btn2.place(x=505, y=360)
        self.delete_btn2.place(x=570, y=335)
        self.message_btn2.place(x=570, y=400)

        self.backdrop3.place(x=190, y=480)
        self.pic_label3.place(x=220, y=505)
        self.username_label3.place(x=370, y=525)
        self.view_prof_btn3.place(x=505, y=520)
        self.delete_btn3.place(x=570, y=495)
        self.message_btn3.place(x=570, y=560)

        self.backdrop4.place(x=190, y=640)
        self.pic_label4.place(x=220, y=665)
        self.username_label4.place(x=370, y=685)
        self.view_prof_btn4.place(x=505, y=680)
        self.delete_btn4.place(x=570, y=655)
        self.message_btn4.place(x=570, y=720)
        #column2
        self.backdrop5.place(x=760, y=160)
        self.pic_label5.place(x=790, y=185)
        self.username_label5.place(x=940, y=205)
        self.view_prof_btn5.place(x=1075, y=200)
        self.delete_btn5.place(x=1140, y=175)
        self.message_btn5.place(x=1140, y=240)

        self.backdrop6.place(x=760, y=320)
        self.pic_label6.place(x=790, y=345)
        self.username_label6.place(x=940, y=365)
        self.view_prof_btn6.place(x=1075, y=360)
        self.delete_btn6.place(x=1140, y=335)
        self.message_btn6.place(x=1140, y=400)

        self.backdrop7.place(x=760, y=480)
        self.pic_label7.place(x=790, y=505)
        self.username_label7.place(x=940, y=525)
        self.view_prof_btn7.place(x=1075, y=520)
        self.delete_btn7.place(x=1140, y=495)
        self.message_btn7.place(x=1140, y=560)

        self.backdrop8.place(x=760, y=640)
        self.pic_label8.place(x=790, y=665)
        self.username_label8.place(x=940, y=685)
        self.view_prof_btn8.place(x=1075, y=680)
        self.delete_btn8.place(x=1140, y=655)
        self.message_btn8.place(x=1140, y=720)
