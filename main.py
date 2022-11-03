import time
import customtkinter
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import tkinterwidgets as tkw
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
# postgresql-globular-06874
from customtkinter import CTk

from Recommendations import Recs_page
from Events import Events_page
from Search import Search_page
from Contacts import Contacts_page
from Profile import Profile_page
from Registration import Register_page
from Register_Confirmation import Register_confirmation_page
from PIL import ImageTk, Image
from tkcalendar import Calendar
import sqlite3
from hashlib import blake2b
import pylint

'''
hConn = psycopg2.connect(host = "ec2-3-213-66-35.compute-1.amazonaws.com", database = "ddipmu7if1umsi",
                            user="wfpsdpcxvibamf", password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432" ,
                            port="5432")
hCursor = hConn.cursor()
'''
#hCursor.execute('''DROP TABLE Users, Events''')
#hCursor.execute('''DROP TABLE testing, tester''')
'''
hConn.commit()
hConn.close()
'''

#configure and connect to Postgres
hConn = psycopg2.connect(host = "ec2-3-213-66-35.compute-1.amazonaws.com", database = "ddipmu7if1umsi",
                            user="wfpsdpcxvibamf", password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432" ,
                            port="5432")
hCursor = hConn.cursor()
hCursor.execute('''CREATE TABLE IF NOT EXISTS Users(userid SERIAL PRIMARY KEY, profile_pic TEXT, creation_date TEXT, data_protect BOOLEAN, fullname TEXT, password TEXT, age INT, nationality TEXT, username TEXT, email TEXT, github TEXT, linkedIn TEXT, code_lang TEXT, events TEXT, meeting_mode TEXT, meeting_region TEXT, field_study TEXT, years_in_field INT, short_Desc TEXT, users_preference TEXT)''')
hConn.commit()
hConn.close()
hConn = psycopg2.connect(host = "ec2-3-213-66-35.compute-1.amazonaws.com", database = "ddipmu7if1umsi",
                            user="wfpsdpcxvibamf", password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432" ,
                            port="5432")
hCursor = hConn.cursor()
hCursor.execute('''CREATE TABLE IF NOT EXISTS Events(eventid SERIAL PRIMARY KEY, event_pic TEXT, creation_date TEXT, event_date TEXT, eventname TEXT, location TEXT, event_type TEXT, short_Desc TEXT)''')
hConn.commit()
hConn.close()

class BinaryApp(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        """
        Initialize parent class

        This function will initialize the parent class allowing for subclasses to be built on top of this class
        :return: parent class
        """
        super().__init__()
        customtkinter.CTk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.geometry("1280x720")
        self.resizable(False, False)
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Register_page, Register_confirmation_page, Recs_page, Events_page, Search_page, Contacts_page, Profile_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        """
        This function will bring forward the chosen frame

        Show a frame for the given page name
        :return: Returns chosen frame
        """
        frame = self.frames[page_name]
        frame.tkraise()

class Login(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        """
        Initialize parent class

        This function will initialize the parent class allowing for subclasses to be built on top of this class
        :return: parent class
        """
        super().__init__()
        customtkinter.CTkFrame.__init__(self, parent)
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.controller = controller
        self.controller.title("Binary")

        global bg
        if customtkinter.get_appearance_mode() == "light" or customtkinter.get_appearance_mode() == "Light":
            bg = Image.open("images/light_wallpaper.png")
            bg = ImageTk.PhotoImage(bg.resize((1920, 1080), Image.ANTIALIAS))
            widget_bg = "#a6d6c8"
            toolbar_bg = "#e1edfb"
            #widget_bg = "#05243c"
            accentColour = "#48CAE4"
            accentColour2 = "#E46248"
            textColour = "black"
            loginColour = "black"
        else:
            bg = Image.open("images/dark_wallpaper.png")
            bg = ImageTk.PhotoImage(bg.resize((1920, 1080), Image.ANTIALIAS))
            #widget_bg = "#001ccf"
            #widget_bg = "#EAE4D9"
            widget_bg = "#94c7e8"
            toolbar_bg = "#112938"
            accentColour = "#0077b6"
            accentColour2 = "#B63F00"
            textColour = "black"
            loginColour = "white"

        # Create Canvas
        canvas1 = tk.Canvas(self, width=400,height=400, bd=0, highlightthickness=0, relief='solid')
        canvas1.pack(fill="both", expand=True)

        # Display image
        canvas1.create_image(0, 0, image=bg, anchor="nw")

        # Create Widgets
        # ALL
        login_username_label = customtkinter.CTkLabel(text_font=['trebuchet MS bold', 20],
                                                      bg_color=toolbar_bg, text_color=loginColour)
        # self.login_block_label = customtkinter.CTkLabel(font='Bahnschrift 20 underline bold', bg="#2176FF", width=20, height=10)
        bg_label = customtkinter.CTkLabel(self, text="", width=400, height=530, relief='solid', bg_color=widget_bg)
        image = Image.open("images/binary_home.png")
        photo = ImageTk.PhotoImage(image.resize((400, 339), Image.ANTIALIAS))
        label_img = customtkinter.CTkLabel(self, image=photo)
        label_img.image = photo

        username_label = customtkinter.CTkLabel(self, text="Username", text_font=('trbuchet MS', 20, 'bold'),
                                                bg_color=widget_bg, text_color=textColour)
        username = customtkinter.StringVar()
        username_box = customtkinter.CTkEntry(self, textvariable=username, text_font=('arial', 12), width=200,
                                              bg_color=widget_bg, fg_color='white', text_color="black")
        username_box.focus_set()

        password_label = customtkinter.CTkLabel(self, text="Password", text_font=('trebuchet MS', 20, 'bold'), bg_color=widget_bg, text_color=textColour)
        password = customtkinter.StringVar()
        password_box = customtkinter.CTkEntry(self, textvariable=password, text_font=('arial', 12), width=200,
                                              bg_color=widget_bg,fg_color='white', text_color="black")

        def check_login():
            """
            This function checks the login credentials based on the username entered

            If the username == abc and password == 123, the user will enter a 'bypass' account to enter the
            application without creating an account
            If the username and password == admin, the admin window will appear
            If the username is neither of the ones mentioned, it will search the database for the same username and
            determine if the hashed password matches the one inputted by the user (after input password is hashed)
            :returns: Recommendations page, admin window or login error message
            """
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            username = username_box.get()
            password = password_box.get()
            password_hash = password.encode()
            h = blake2b()
            h.update(password_hash)
            password_hash = "[('" + h.hexdigest() + "',)]"
            try:
                hCursor.execute("SELECT password FROM Users WHERE username = %s", [username])
            except psycopg2.errors.UndefinedColumn:
                incorrect_password_label_canvas = canvas1.create_window(985, 1000, anchor="center", width=500,
                                                                        window=incorrect_password_label)
                return
            db_password = str(hCursor.fetchall())
            if username == "abc" and password == '123':
                file = open("Databases/logs.txt", "w")
                file.write(username + "\n")
                file.close()
                file = open("Databases/logs.txt", "r").read()
                login_username_label.configure(text="Logged in as:\n" + file[:-1])
                login_username_label.tkraise()
                login_username_label.place(x=1000, y=15)
                controller.show_frame('Recs_page')
            #Admin Login
            elif username == "admin" and password == "admin":
                # Toplevel object which will
                # be treated as a new window
                newWindow = customtkinter.CTkToplevel(parent, bg="#2176ff")
                # sets the title of the
                # Toplevel widget
                newWindow.title("Admin System")
                # sets the geometry of toplevel
                newWindow.geometry("500x700")
                customtkinter.CTkLabel(newWindow,text="Add New Event", text_font='Bahnschrift 20 underline bold', text_color='black').pack()
                newWindow.load_event_pic = Image.open('images/default_profile_img.png')
                newWindow.default_pic = ImageTk.PhotoImage(newWindow.load_event_pic.resize((150, 150), Image.ANTIALIAS))
                newWindow.event_pic_label = customtkinter.CTkLabel(newWindow, image=newWindow.default_pic)
                newWindow.event_pic_label.place(x=30, y=70)
                incorrect_password_label.destroy()

                def change_pic():
                    """
                    Allows the admin to change the picture of the event

                    :return: new image replaces default image
                    """
                    file = open("Databases/event.txt", "w")
                    filename = filedialog.askopenfilename(initialdir="C:\\", filetypes=(
                    ("PNG file", "*.png"), ("JPEG File", "*.jpeg"), ("JPG File", "*.jpg"), ("All File Types", "*.*")))
                    file.write(filename)
                    file.close()
                    stgImg = Image.open(filename)
                    stgImg = ImageTk.PhotoImage(stgImg.resize((150,100), Image.ANTIALIAS))
                    newWindow.event_pic_label.configure(image=stgImg)
                    newWindow.event_pic_label.image = stgImg
                change_pic_btn = customtkinter.CTkButton(newWindow, text="Upload Image", width=20, text_font='Bahnschrift 12 bold',
                                                         relief='solid', command=change_pic, fg_color="#FFAA21", text_color='black')

                change_pic_btn.place(x=35, y=180)
                event_name_label = customtkinter.CTkLabel(newWindow,text='Event name', text_font='Bahnschrift 16 bold', text_color='black')
                event_name_label.place(x=275, y=50)
                event_name_entry = customtkinter.CTkEntry(newWindow, width=275, relief='solid', fg_color='white',
                                                          text_color='black', border_color='black', bg_color='#2176ff')
                event_name_entry.place(x=200,y=85)

                cal = Calendar(newWindow, selectmode='day',year=2022, month=9,day=29)
                cal.place(x=340, y=200)

                newWindow.location_dd = customtkinter.CTkOptionMenu(newWindow, values=["Singapore",
                                                                                       "Malaysia", "Indonesia", "China",
                                                                                       "Vietnam"])
                newWindow.location_dd.set("Location")
                newWindow.location_dd.configure(text_font='Bahnschrift 12 bold', bg_color='#2176ff', fg_color="#FFAA21",
                                                text_color='black', button_color='#FFAA21', dropdown_color='#FFAA21',
                                                dropdown_text_color='black', dropdown_text_font='Bahnschrift 12 bold',
                                                width=190)
                newWindow.location_dd.place(x=220, y=310)

                newWindow.comboboxEvent = customtkinter.CTkOptionMenu(master=newWindow, values=["Hackathon", "Codathon",
                                                                                                "Bug Hunt", "Seminars & Olympiads"])
                newWindow.comboboxEvent.configure(text_font='Bahnschrift 12 bold', bg_color='#2176ff', fg_color="#FFAA21",
                                                text_color='black', button_color='#FFAA21', dropdown_color='#FFAA21',
                                                dropdown_text_color='black', dropdown_text_font='Bahnschrift 12 bold',
                                                width=190)
                newWindow.comboboxEvent.place(x=220, y=360)
                newWindow.comboboxEvent.set("Event Type")  # set initial value

                newWindow.short_desc_label = customtkinter.CTkLabel(newWindow, text="Event Description", text_font='Bahnschrift 16 bold'
                                                                    ,text_color='black')
                newWindow.short_desc_label.place(x=150, y=410)
                newWindow.short_desc = scrolledtext.ScrolledText(newWindow, wrap=tk.WORD, width=35, height=5
                                                                 ,font='Bahnschrift 16 bold', relief='solid')
                newWindow.short_desc.place(x=20, y=670)
                def submit_event():
                    """
                    Gets all the details about the event:

                    Image path, event name, event description, date of event, location and event type
                    :return: Returns success message if successful else error message to fill missing details
                    """
                    hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                             user="wfpsdpcxvibamf",
                                             password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                             port="5432")
                    hCursor = hConn.cursor()
                    file = open("Databases/event.txt", "r")
                    filename = file.read()
                    file.close()
                    #filename = filename.split("/")
                    #filename = filename[-1]
                    print(filename)
                    date_time = str(datetime.now())
                    #date_time = date_time.split()
                    #date_time = "/".join(date_time)
                    #date_time = date_time.replace(':','-')
                    print(date_time)
                    event_date = str(cal.get_date())
                    event_name = event_name_entry.get()
                    location = newWindow.location_dd.get()
                    eventType = newWindow.comboboxEvent.get()
                    shortDesc = newWindow.short_desc.get("1.0","end-1c")
                    error_count = 0
                    if event_name == '':
                        error_count+=1
                    if location == "Location":
                        error_count+=1
                    if eventType == "Event Type":
                        error_count+=1
                    if error_count == 0:

                        sql = 'INSERT INTO Events(event_pic, creation_date, event_date, eventname, location, event_type, short_Desc)' + ' VALUES(' + str(filename) + ',' + date_time + ',' + event_date + ',' + event_name + ',' + location + ',' + eventType + ',' + shortDesc + ')'
                        print(sql)
                        hCursor.execute('INSERT INTO Events(event_pic, creation_date, event_date, eventname, location, event_type, short_Desc) VALUES(%s,%s,%s,%s,%s,%s,%s)',(filename, date_time, event_date, event_name, location, eventType, shortDesc))
                        hConn.commit()

                        newWindow.success_label.text = "Successfully submitted"
                        newWindow.success_label.place(x=130, y=650)
                        newWindow.fail_label.destroy()
                        hConn.close()
                    else:
                        newWindow.fail_label.text = "Ensure fields are filled"
                        newWindow.fail_label.place(x=65, y=650)

                submit_img = Image.open("images/submit_icon.png")
                submit_img = ImageTk.PhotoImage(submit_img.resize((50, 50), Image.ANTIALIAS))
                newWindow.submit_btn = customtkinter.CTkButton(newWindow, text='Submit', text_font='Bahnschrift 16 bold',
                                                               bg_color='#2176ff', text_color='black', fg_color='#FFAA21'
                                                               , command=submit_event, image=submit_img)
                newWindow.submit_btn.place(x=170, y=600)
                newWindow.success_label = customtkinter.CTkLabel(newWindow, text='Successfully Submitted',
                                                                 fg_color='green', text_color='black',
                                                                 text_font='Bahnschrift 16 bold')
                newWindow.fail_label = customtkinter.CTkLabel(newWindow, text='Please Check All Fields Are Correct',
                                                              fg_color='red', text_color='black',
                                                              text_font='Bahnschrift 16 bold')
            elif password_hash == db_password:
                file = open("Databases/logs.txt", "w")
                file.write(username + "\n")
                file.close()
                file = open("Databases/logs.txt", "r").read()
                login_username_label.configure(text="Logged in as:\n" + file[:-1])
                login_username_label.tkraise()
                login_username_label.place(x=1000, y=15)
                controller.show_frame('Recs_page')
            else:
                incorrect_password_label_canvas = canvas1.create_window(985, 1000, anchor="center", width=500,
                                                                        window=incorrect_password_label)

        def register_page():
            """
            Requests to show register page

            :return: Displays reguister page to user
            """
            controller.show_frame('Register_page')

        loadimage = Image.open("images/login_icon.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        roundedbutton = customtkinter.CTkButton(self, image=loadimage, command=check_login, bg_color=widget_bg, text="Login",
                                                fg_color="#0d9c8c",text_font=('trebuchet MS bold', 20), width=200, text_color=textColour,
                                                height=40)
        loadimage = Image.open("images/sign_up_icon.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        signup_button = customtkinter.CTkButton(self, text='Sign Up', bg_color=widget_bg,command=register_page,
                                                text_font='arial 15 underline', width=10, fg_color=widget_bg,
                                                hover_color="light blue", text_color=textColour)

        incorrect_password_label = customtkinter.CTkLabel(self, text='Incorrect Password', text_font=('Arial', 20),
                                                          fg_color='red', text_color='black')

        # Display Widgets
        bg_canvas = canvas1.create_window(980, 540, anchor="center", window=bg_label)
        imageLabel_canvas = canvas1.create_window(780, 170, anchor="nw",window=label_img)
        username_label_canvas = canvas1.create_window(985, 570, anchor="center", window=username_label)
        username_box_canvas = canvas1.create_window(990, 620, anchor="center", window=username_box)
        password_label_canvas = canvas1.create_window(985, 670, anchor="center", window=password_label)
        password_box_canvas = canvas1.create_window(990, 720, anchor="center", window=password_box)
        login_btn_canvas = canvas1.create_window(990, 800, anchor="center", window=roundedbutton)
        signup_btn_canvas = canvas1.create_window(990, 870, anchor="center", window=signup_button)

        def handleFocusIn(_):
            """
            Changes text entered in password box to '*'

            :param _: text
            :return: returns *
            """
            password_box.configure(show='*')

        password_box.bind('<FocusIn>', handleFocusIn)

if __name__ == "__main__":
    app = BinaryApp()
    app.mainloop()