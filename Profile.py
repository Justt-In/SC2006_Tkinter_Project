import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import sqlite3

class Profile_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='green')
        self.controller = controller
        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg='#ff8c1a', borderwidth=2, relief='solid')

        def goto_recs():
            controller.show_frame('Recs_page')

        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="#ff8c1a", bd="3", height=130, relief="raised",
                                  command=lambda: controller.show_frame("Recs_page"))

        def goto_search():
            controller.show_frame('Search_page')

        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="#ff8c1a", bd="3", height=130,
                                    relief="raised", command=lambda: controller.show_frame("Search_page"))

        def goto_events():
            controller.show_frame('Events_page')

        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="#ff8c1a", bd="3", height=130,
                                    relief="raised", command=lambda: controller.show_frame("Events_page"))

        def goto_contacts():
            controller.show_frame('Contacts_page')

        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="#ff8c1a", bd="3", height=130,
                                      relief="raised", command=lambda: controller.show_frame("Contacts_page"))

        def goto_profile():
            controller.show_frame('Profile_page')

        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="#ff8c1a", bd="3", height=130,
                                     relief="raised", command=lambda: controller.show_frame("Profile_page"))
        # End of Toolbar

        #Create elements & widgets
        self.load_profile_pic = Image.open('images/default_profile_img.png')
        self.default_pic = ImageTk.PhotoImage(self.load_profile_pic.resize((300, 300), Image.ANTIALIAS))
        self.profile_pic_label = tk.Label(self, image=self.default_pic, bg='green')
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
        self.user_desc = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=25, height=14, font='Bahnschrift 16 bold')
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
            connection.close()
        self.get_details_btn = tk.Button(self, text='Get Current Profile Details', font='Bahnschrift 32 bold', bg='cyan', relief='solid', command=start_edits)

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
            connection.close()
        self.save_details_btn = tk.Button(self, text='Save Edits', font='Bahnschrift 28 bold', bg='Red', relief='solid', command=save_edits)

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
        self.profile_pic_label.place(x=300, y=380)
        self.pic_btn.place(x=330, y=695)
        self.username_label.place(x=750, y=280)
        self.user_desc.place(x=750, y=380)
        self.save_details_btn.place(x=600, y=780)