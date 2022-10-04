import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import sqlite3

class Search_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='red')
        self.controller = controller

        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg="#ff8c1a", borderwidth=2, relief='solid')

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

        #add elemets & widgets
        self.user_label = tk.Label(self, text='Looking for someone...?', font='Bahnschrift 40 bold underline', bg='red')
        self.search_user = tk.Entry(self, font=('arial', 18), width=30, relief='solid', bd=2)
        self.search_user.pack(ipady=18)
        self.label_block = tk.Label(self, bg='red', width=500, height=300)
        self.success_label = tk.Label(self, bg='red',fg='green', text='', font='Bahnschrift 30 bold ')
        self.fail_label = tk.Label(self,bg='red', fg='black', text='', font='Bahnschrift 30 bold ')
        #Gets the username entered into the the search bar and finds that user, returns appropriate messages if no user
        # is found and returns the found user if there exists one
        def search_user():
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            search_username = self.search_user.get()
            cursor.execute("SELECT profile_pic, username, short_Desc FROM User WHERE username = ?", [search_username])
            details = cursor.fetchall()
            try:
                profile_pic = details[0][0]
                if profile_pic != None:
                    load_profile_pic = Image.open(profile_pic)
                    default_pic = ImageTk.PhotoImage(load_profile_pic.resize((130, 130), Image.ANTIALIAS))
                    self.randomuser1_img.configure(image=default_pic)
                    self.randomuser1_img.image = default_pic
                search_username = details[0][1]
                self.randomuser1_username['text'] = search_username
                short_desc = details[0][2]
                self.randomuser1_desc['text'] = short_desc
                self.fail_label['text'] = ""
                self.label_block.lower()
            except IndexError:
                self.fail_label['text'] = "No user found, please check your input once more"
                self.fail_label.tkraise()
        self.usersearch_button = tk.Button(self, text='Search', font='Bahnschrift 16 bold', bg='Cyan', relief='raised', command=search_user)
        self.rect_label_1 = tk.Label(self, bg='orange', fg='black', relief='solid', height='10', width='80')
        self.load_randomuser1_img = tk.PhotoImage(file='images/profile_icon.png')
        self.randomuser1_img = tk.Label(self, image=self.load_randomuser1_img, bg='orange')
        self.randomuser1_username = tk.Label(self, text='Username', font='Bahnschrift 20 underline bold', bg='orange')
        self.randomuser1_desc = tk.Label(self, text='Experience Description...', font='Bahnschrift 14 bold', bg='orange')
        self.load_add_img = tk.PhotoImage(file='images/add_user_img.png')
        def add_user():
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]
            sql = 'Databases/' + username + '_db.db'
            connection = sqlite3.connect(sql)
            cursor = connection.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS Personal(userid INTEGER PRIMARY KEY AUTOINCREMENT, invite_received TEXT, invite_sent TEXT, proggies TEXT)''')
            connection.commit()
            cursor.execute('SELECT invite_sent FROM Personal')
            invited = cursor.fetchall()
            count = 0
            for name in invited:
                if self.search_user.get() == name[0]:
                    self.success_label['text'] = 'Request already sent!'
                    count += 1
            print(count)
            cursor.execute('SELECT proggies FROM Personal')
            proggies = cursor.fetchall()
            for name in proggies:
                if self.search_user.get() == name[0]:
                    self.success_label['text'] = 'You two are already Proggies!'
                    count +=1
            if count == 0:
                #sql = 'INSERT INTO Personal(invite_sent) VALUES(?)',(self.search_user.get())
                searched_username = str(self.search_user.get())
                cursor.execute('INSERT INTO Personal(invite_sent) VALUES(?)',(searched_username,))
                connection.commit()
                connection.close()
                sql = 'Databases/' + self.search_user.get() + '_db.db'
                connection = sqlite3.connect(sql)
                cursor = connection.cursor()
                cursor.execute(
                    '''CREATE TABLE IF NOT EXISTS Personal(userid INTEGER PRIMARY KEY AUTOINCREMENT, invite_received TEXT, invite_sent TEXT, proggies TEXT)''')
                connection.commit()
                #sql = 'INSERT INTO Personal(invite_sent) VALUES(?)', (self.search_user.get())
                cursor.execute('INSERT INTO Personal(invite_received) VALUES(?)', (username,))
                connection.commit()
                connection.close()
                self.success_label['text'] = 'Friend Request Sent!'
        self.add_img_btn1 = tk.Button(self, image=self.load_add_img, bg='orange', command=add_user)
        self.rect_label_2 = tk.Label(self, bg='orange', fg='black', relief='solid', height='10', width='80')
        self.randomuser2_img = tk.Label(self, image=self.load_randomuser1_img, bg='orange')
        self.randomuser2_username = tk.Label(self, text='Username', font='Bahnschrift 20 underline bold', bg='orange')
        self.randomuser2_desc = tk.Label(self, text='Experience Description...', font='Bahnschrift 14 bold',bg='orange')
        self.add_img_btn2 = tk.Button(self, image=self.load_add_img, bg='orange')
        self.rect_label_3 = tk.Label(self, bg='orange', fg='black', relief='solid', height='10', width='80')
        self.randomuser3_img = tk.Label(self, image=self.load_randomuser1_img, bg='orange')
        self.randomuser3_username = tk.Label(self, text='Username', font='Bahnschrift 20 underline bold', bg='orange')
        self.randomuser3_desc = tk.Label(self, text='Experience Description...', font='Bahnschrift 14 bold',bg='orange')
        self.add_img_btn3 = tk.Button(self, image=self.load_add_img, bg='orange')

        # arrange elements & widgets
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
        self.user_label.place(x=450, y=150)
        self.search_user.place(x=530, y=250)
        self.usersearch_button.place(x=930, y=245)
        self.rect_label_1.place(x=450, y=320)
        self.randomuser1_img.place(x=460, y=330)
        self.randomuser1_username.place(x=680, y=330)
        self.randomuser1_desc.place(x=630, y=380)
        self.add_img_btn1.place(x=900, y=360)
        self.label_block.place(x=0, y=300)
        self.label_block.tkraise()
        self.success_label.place(x=550, y=500)
        self.fail_label.place(x=300, y=500)
        '''
        self.rect_label_2.place(x=450, y=500)
        self.randomuser2_img.place(x=460, y=510)
        self.randomuser2_username.place(x=630, y=510)
        self.randomuser2_desc.place(x=630, y=580)
        self.add_img_btn2.place(x=900, y=540)
        self.rect_label_3.place(x=450, y=680)
        self.randomuser3_img.place(x=460, y=690)
        self.randomuser3_username.place(x=630, y=690)
        self.randomuser3_desc.place(x=630, y=760)
        self.add_img_btn3.place(x=900, y=720)
        '''

