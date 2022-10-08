import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
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

connection = sqlite3.connect('Databases/User_database.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS User(userid INTEGER PRIMARY KEY AUTOINCREMENT, profile_pic TEXT, creation_date TEXT, data_protect BOOLEAN, fullname TEXT, password TEXT, age INT, nationality TEXT, username TEXT, email TEXT, github TEXT, linkedIn TEXT, code_lang TEXT, events TEXT, meeting_mode TEXT, meeting_region TEXT, field_study TEXT, years_in_field INT, short_Desc TEXT)''')
connection.commit()
connection.close()
connection = sqlite3.connect('Databases/Event_database.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Events(eventid INTEGER PRIMARY KEY AUTOINCREMENT, event_pic TEXT, creation_date TEXT, event_date TEXT, eventname TEXT, location TEXT, event_type TEXT, short_Desc TEXT)''')
connection.commit()
connection.close()

class BinaryApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
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
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#2176FF')
        self.controller = controller
        self.controller.title("Binary")
        self.controller.state("zoomed")

        space_label1 = tk.Label(self, height=8, bg='#2176FF')
        space_label1.pack()

        image = Image.open("images/binary_home.png")
        photo = ImageTk.PhotoImage(image.resize((278, 235), Image.ANTIALIAS))

        label_img = tk.Label(self, image=photo, bd=-2)
        label_img.image = photo
        label_img.pack()

        space_label2 = tk.Label(self, height=3, bg='#2176FF')
        space_label2.pack()

        username_label = tk.Label(self, text="Username", font=('arial', 20, 'bold'), foreground='black', bg='#2176FF')
        username_label.pack(pady=5)
        username = tk.StringVar()
        username_box = tk.Entry(self, textvariable=username, font=('arial', 12), width=30)
        username_box.pack(ipady=7)
        username_box.focus_set()

        password_label = tk.Label(self, text="Password", font=('arial', 20, 'bold'), foreground='black',background='#2176FF')
        password_label.pack(pady=5)
        password = tk.StringVar()
        password_box = tk.Entry(self, textvariable=password, font=('arial', 12), width=30)
        password_box.pack(ipady=7)

        #ALL
        login_username_label = tk.Label(font='Bahnschrift 20 underline bold', bg="#FDCA40")
        #self.login_block_label = tk.Label(font='Bahnschrift 20 underline bold', bg="#2176FF", width=20, height=10)

        def handleFocusIn(_):
            password_box.configure(fg='black', show='*')

        password_box.bind('<FocusIn>', handleFocusIn)

        space_label3 = tk.Label(self, height=1, bg='#2176FF')
        space_label3.pack()

        def check_login():
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            username = username_box.get()
            password = password_box.get()
            password_hash = password.encode()
            h = blake2b()
            h.update(password_hash)
            password_hash = "[('" + h.hexdigest() + "',)]"
            cursor.execute("SELECT password FROM User WHERE username = ?", [username])
            db_password = str(cursor.fetchall())
            if username == "abc" and password == '123':
                file = open("Databases/logs.txt", "w")
                file.write(username + "\n")
                file.close()
                file = open("Databases/logs.txt", "r").read()
                login_username_label['text'] = "Logged in as:\n" + file[:-1]
                login_username_label.tkraise()
                login_username_label.place(x=1175, y=50)
                controller.show_frame('Recs_page')
            #Admin Login
            elif username == "admin" and password == "admin":
                # Toplevel object which will
                # be treated as a new window
                newWindow = tk.Toplevel(parent)
                # sets the title of the
                # Toplevel widget
                newWindow.title("New Window")
                # sets the geometry of toplevel
                newWindow.geometry("500x570")
                tk.Label(newWindow,text="Add new event", font='Bahnschrift 20 underline bold').pack()
                newWindow.load_event_pic = Image.open('images/default_profile_img.png')
                newWindow.default_pic = ImageTk.PhotoImage(newWindow.load_event_pic.resize((150, 150), Image.ANTIALIAS))
                newWindow.event_pic_label = tk.Label(newWindow, image=newWindow.default_pic)
                newWindow.event_pic_label.place(x=30, y=50)
                def change_pic():
                    file = open("Databases/event.txt", "w")
                    filename = filedialog.askopenfilename(initialdir="C:\\", filetypes=(
                    ("PNG file", "*.png"), ("JPEG File", "*.jpeg"), ("JPG File", "*.jpg"), ("All File Types", "*.*")))
                    file.write(filename)
                    file.close()
                    stgImg = ImageTk.PhotoImage(file=filename)
                    newWindow.event_pic_label.configure(image=stgImg)
                    newWindow.event_pic_label.image = stgImg
                change_pic_btn = tk.Button(newWindow, text="Upload Image", width=20, font='Bahnschrift 12 bold', relief='solid', command=change_pic)
                change_pic_btn.place(x=10, y=210)
                event_name_label = tk.Label(newWindow,text='Event name', font='Bahnschrift 14')
                event_name_label.place(x=275, y=50)
                event_name_entry = tk.Entry(newWindow, width=45, relief='solid')
                event_name_entry.place(x=200,y=85)
                cal = Calendar(newWindow, selectmode='day',year=2022, month=9,day=29)
                cal.place(x=210, y=115)
                newWindow.location = tk.StringVar(newWindow)
                newWindow.location.set("Location")
                newWindow.location_dd = tk.OptionMenu(newWindow, newWindow.location, "Singapore", "Malaysia", "Indonesia", "China", "Vietnam")
                newWindow.location_dd.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
                location1_menu = newWindow.nametowidget(newWindow.location_dd.menuname)
                location1_menu.configure(font='Bahnschrift 12 bold')
                newWindow.location_dd.place(x=220, y=310)
                newWindow.eventType = tk.StringVar(newWindow)
                newWindow.eventType.set("Event Type")
                newWindow.evenType_dd = tk.OptionMenu(newWindow, newWindow.eventType, "Hackathon", "Codathon", "Bug Hunt", "Seminars & Olympiads")
                newWindow.evenType_dd.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
                eventType_menu = newWindow.nametowidget(newWindow.evenType_dd.menuname)
                eventType_menu.configure(font='Bahnschrift 12 bold')
                newWindow.evenType_dd.place(x=330, y=310)
                newWindow.short_desc_label = tk.Label(newWindow, text="Event Description", font='Bahnschrift 16 bold')
                newWindow.short_desc_label.place(x=150, y=350)
                newWindow.short_desc = scrolledtext.ScrolledText(newWindow, wrap=tk.WORD, width=35, height=3,
                                                            font='Bahnschrift 16 bold', relief='solid')
                newWindow.short_desc.place(x=20, y=380)
                def submit_event():
                    connection = sqlite3.connect('Databases/Event_database.db')
                    cursor = connection.cursor()
                    file = open("Databases/event.txt", "r")
                    filename = file.read()
                    file.close()
                    date_time = str(datetime.now())
                    event_date = str(cal.get_date())
                    event_name = event_name_entry.get()
                    location = newWindow.location.get()
                    eventType = newWindow.eventType.get()
                    shortDesc = newWindow.short_desc.get("1.0","end-1c")
                    count = 0
                    if event_name == '':
                        count+=1
                    if location == "Location":
                        count+=1
                    if event_name == "Event Type":
                        count+=1
                    if count == 0:
                        cursor.execute('INSERT INTO Events(event_pic, creation_date, event_date, eventname, location, event_type, short_Desc) VALUES(?,?,?,?,?,?,?)',
                            (filename, date_time, event_date, event_name, location, eventType, shortDesc))
                        connection.commit()
                        newWindow.success_label['text'] = "Successfully submitted"
                        newWindow.success_label.tkraise()
                        connection.close()
                    else:
                        newWindow.fail_label['text'] = "Ensure fields are filled"
                        newWindow.fail_label.tkraise()

                newWindow.submit_btn = tk.Button(newWindow, text='Submit', font='Bahnschrift 16 bold', bg='#FDCA40', relief='solid', command=submit_event)
                newWindow.submit_btn.place(x=200, y=480)
                newWindow.success_label = tk.Label(newWindow, text='', fg='green', relief='flat', font='Bahnschrift 16 bold')
                newWindow.success_label.place(x=140, y=530)
                newWindow.fail_label = tk.Label(newWindow, text='', fg='red', relief='flat',font='Bahnschrift 16 bold')
                newWindow.fail_label.place(x=140, y=530)

            elif password_hash == db_password:
                file = open("Databases/logs.txt", "w")
                file.write(username + "\n")
                file.close()
                file = open("Databases/logs.txt", "r").read()
                login_username_label['text'] = "Logged in as:\n" + file[:-1]
                login_username_label.tkraise()
                login_username_label.place(x=1175, y=50)
                controller.show_frame('Recs_page')
            else:
                incorrect_password_label['text'] = 'Incorrect Password'

        def register_page():
            login_username_label.place(x=1175, y=50)
            login_username_label.lower()
            controller.show_frame('Register_page')

        self.loadimage = tk.PhotoImage(file="images/img_login.png")
        self.roundedbutton = tk.Button(self, image=self.loadimage, command=check_login)
        self.roundedbutton["bg"] = "#FDCA40"
        self.roundedbutton["border"] = "3"
        self.roundedbutton.pack(side="top")
        signup_button = tk.Button(self, text='Sign Up', fg='black', bg='#FDCA40', command=register_page, font=('Arial', 15), width=10, relief='raised', borderwidth=5)
        signup_button.pack(pady=10)
        incorrect_password_label = tk.Label(self, text='', font=('Arial', 20), fg='red', bg='#2176FF')
        incorrect_password_label.pack(fill='both', expand=True)
'''
class Register_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5cc9ed')

        #Create elements & widgets
        self.space_label1 = tk.Label(self, height=8, width=50, bg='#5cc9ed')
        self.load_register_icon = tk.PhotoImage(file="images/register_hello.png")
        self.register_icon_label = tk.Label(self, image=self.load_register_icon, bg='#5cc9ed')
        self.register_label = tk.Label(self, text='Registration', font='Bahnschrift 70 bold', bg='#5cc9ed')
        #Backdrop Left
        self.load_backdrop1_img = Image.open("images/backdrop1.png")
        self.backdrop1 = ImageTk.PhotoImage(self.load_backdrop1_img.resize((450, 600), Image.ANTIALIAS))
        self.username_label = tk.Label(self, text='Username', font='Bahnschrift 32 bold', bg='#4C5270')
        self.username_entry = tk.Entry(self,font=('arial', 20), width=24)
        self.password_label = tk.Label(self, text='Password', font='Bahnschrift 32 bold', bg='#4C5270')
        self.password_entry = tk.Entry(self, font=('arial', 20), width=24)
        self.retype_password_label = tk.Label(self, text='Retype Password', font='Bahnschrift 32 bold', bg='#4C5270')
        self.retype_password_entry = tk.Entry(self, font=('arial', 20), width=24)
        self.email_label = tk.Label(self, text='Email', font='Bahnschrift 32 bold', bg='#4C5270')
        self.email_entry = tk.Entry(self, font=('arial', 20), width=24)
        #Backdrop Right
        self.backdrop2 = self.backdrop1
        self.backdrop1_label = tk.Label(self, image=self.backdrop1, bg='#5cc9ed')
        self.backdrop2_label = tk.Label(self, image=self.backdrop2, bg='#5cc9ed')
        self.proficient = tk.StringVar(self)
        self.proficient.set("Experience")  # default value
        self.experience1 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience1.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience1_menu = self.nametowidget(self.experience1.menuname)
        experience1_menu.configure(font='Bahnschrift 12 bold')
        self.check1 = tk.Checkbutton(self, text='Python', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience2 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience2.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience2_menu = self.nametowidget(self.experience2.menuname)
        experience2_menu.configure(font='Bahnschrift 12 bold')
        self.check2 = tk.Checkbutton(self, text='C++', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience3 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience3.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience3_menu = self.nametowidget(self.experience3.menuname)
        experience3_menu.configure(font='Bahnschrift 12 bold')
        self.check3 = tk.Checkbutton(self, text='C#', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience4 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience4.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience4_menu = self.nametowidget(self.experience4.menuname)
        experience4_menu.configure(font='Bahnschrift 12 bold')
        self.check4 = tk.Checkbutton(self, text='C', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience5 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience5.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience5_menu = self.nametowidget(self.experience5.menuname)
        experience5_menu.configure(font='Bahnschrift 12 bold')
        self.check5 = tk.Checkbutton(self, text='Java', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience6 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience6.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience6_menu = self.nametowidget(self.experience6.menuname)
        experience6_menu.configure(font='Bahnschrift 12 bold')
        self.check6 = tk.Checkbutton(self, text='Javascript', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience7 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience7.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience7_menu = self.nametowidget(self.experience7.menuname)
        experience7_menu.configure(font='Bahnschrift 12 bold')
        self.check7 = tk.Checkbutton(self, text='PHP', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience8 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience8.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience8_menu = self.nametowidget(self.experience8.menuname)
        experience8_menu.configure(font='Bahnschrift 12 bold')
        self.check8 = tk.Checkbutton(self, text='SQL', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience9 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience9.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience9_menu = self.nametowidget(self.experience9.menuname)
        experience9_menu.configure(font='Bahnschrift 12 bold')
        self.check9 = tk.Checkbutton(self, text='HTML', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        self.experience10 = tk.OptionMenu(self, self.proficient, "<1Y", "1Y", "2Y", "3Y", ">3Y", "None")
        self.experience10.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience10_menu = self.nametowidget(self.experience10.menuname)
        experience10_menu.configure(font='Bahnschrift 12 bold')
        self.check10 = tk.Checkbutton(self, text='CSS', font='Bahnschrift 16 bold', bg='#4c5270', bd=-2)
        def goto_cfm_page():
            controller.show_frame('Register_confirmation_page')
        self.next_button = tk.Button(self, text='Continue To Next Step', font='Bahnschrift 20 bold', bg='#5cc9ed', bd=3, relief='raised', width=20, height=1, command=goto_cfm_page)

        #Arrange elements & widgets in grid
        self.register_icon_label.place(x=400, y=10)
        self.register_label.place(x=550, y=10)
        #Backdrop1
        self.backdrop1_label.place(x=250, y=175)
        self.username_label.place(x=375, y=200)
        self.username_label.tkraise()
        self.username_entry.place(x=295, y=270)
        self.username_entry.tkraise()
        self.password_label.place(x=375, y=330)
        self.password_label.tkraise()
        self.password_entry.place(x=295, y=400)
        self.password_entry.tkraise()
        self.retype_password_label.place(x=310, y=460)
        self.retype_password_label.tkraise()
        self.retype_password_entry.place(x=295, y=530)
        self.retype_password_entry.tkraise()
        self.email_label.place(x=420, y=580)
        self.email_label.tkraise()
        self.email_entry.place(x=295, y=650)
        self.email_entry.tkraise()
        #Backdrop2
        self.backdrop2_label.place(x=750, y=175)
        self.experience1.place(x=1000, y=230)
        self.check1.place(x=840, y=225)
        self.experience2.place(x=1000, y=270)
        self.check2.place(x=840, y=268)
        self.experience3.place(x=1000, y=310)
        self.check3.place(x=840, y=310)
        self.experience4.place(x=1000, y=350)
        self.check4.place(x=840, y=348)
        self.experience5.place(x=1000, y=390)
        self.check5.place(x=840, y=388)
        self.experience6.place(x=1000, y=430)
        self.check6.place(x=840, y=428)
        self.experience7.place(x=1000, y=470)
        self.check7.place(x=840, y=468)
        self.experience8.place(x=1000, y=510)
        self.check8.place(x=840, y=508)
        self.experience9.place(x=1000, y=550)
        self.check9.place(x=840, y=548)
        self.experience10.place(x=1000, y=590)
        self.check10.place(x=840, y=588)

        self.next_button.place(x=570, y=800)

class Register_confirmation_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='purple')

        #Create elements & widgets
        self.load_title_img = tk.PhotoImage(file="images/profile_icon.png")
        self.page_label = tk.Label(self, text="Let's Setup Your Profile", font='Bahnschrift 60 bold', bg='purple')
        self.title_img_label1 = tk.Label(self, image=self.load_title_img, bg='purple')
        self.title_img_label2 = tk.Label(self, image=self.load_title_img, bg='purple')

        self.load_profile_img = tk.PhotoImage(file="images/default_profile_img.png")
        self.profile_img_label = tk.Label(self, image=self.load_profile_img, bg='purple')
        def UploadAction(event=None):
            filename = filedialog.askopenfilename()
            #do something with filename

        self.load_upload_img = (Image.open("images/upload_img.png"))
        self.resized_image = self.load_upload_img.resize((30, 30), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.upload_img_button = tk.Button(self,text="Upload Image",image=self.new_image, command=UploadAction, width=100, relief='raised', bg='#2860ed')
        self.username_label = tk.Label(self,text='Test Username', font='Bahnschrift 40 underline', bg='purple')
        self.title_label2 = tk.Label(self, text="What Are Your Interests?", font='Bahnschrift 30 bold', bg='purple')
        self.check1 = tk.Checkbutton(self, text='Cyber Security', font='Bahnschrift 25 bold', bg='purple', bd=-2)
        self.check2 = tk.Checkbutton(self, text='Coding Competitions', font='Bahnschrift 25 bold', bg='purple', bd=-2)
        self.check3 = tk.Checkbutton(self, text='Artificial Intelligence', font='Bahnschrift 25 bold', bg='purple', bd=-2)
        self.check4 = tk.Checkbutton(self, text='Data Analytics', font='Bahnschrift 25 bold', bg='purple', bd=-2)
        self.check5 = tk.Checkbutton(self, text='Web Application & Design', font='Bahnschrift 25 bold', bg='purple', bd=-2)
        self.check_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=25, height=3, font='Bahnschrift 16 bold')
        self.title_label3 = tk.Label(self, text='Others:', font='Bahnschrift 25 bold', bg='purple')

        def goto_recs_page():
            controller.show_frame('Recs_page')
        self.submit_button = tk.Button(self, text='Submit', font='Bahnschrift 25 bold', bg='#2860ed', relief='raised', width=20, command=goto_recs_page)

        #Place elements & widgets
        self.title_img_label1.place(x=150, y=10)
        self.page_label.place(x=300, y=10)
        self.title_img_label2.place(x=1150, y=10)
        self.profile_img_label.place(x=300, y=250)
        self.upload_img_button.place(x=377, y=525)
        self.username_label.place(x=700, y=250)
        self.title_label2.place(x=670, y=320)
        self.check1.place(x=700, y=380)
        self.check2.place(x=700, y=430)
        self.check3.place(x=700, y=480)
        self.check4.place(x=700, y=530)
        self.check5.place(x=700, y=580)
        self.title_label3.place(x=700, y=635)
        self.check_area.place(x=700, y=685)
        self.submit_button.place(x=500, y=780)

class Recs_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='brown')
        #Toolbar
        #Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg='orange', borderwidth=2, relief='solid')
        def goto_recs():
            controller.show_frame('Recs_page')
        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="orange", bd="3", height=130, relief="raised", command=goto_recs)
        def goto_search():
            controller.show_frame('Search_page')
        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="orange", bd="3", height=130, relief="raised", command=goto_search)
        def goto_events():
            controller.show_frame('Events_page')
        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="orange", bd="3", height=130, relief="raised", command=goto_events)
        def goto_contacts():
            controller.show_frame('Contacts_page')
        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="orange", bd="3", height=130, relief="raised", command=goto_contacts)
        def goto_profile():
            controller.show_frame('Profile_page')
        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="orange", bd="3", height=130, relief="raised", command=goto_profile)
        #End of Toolbar

        #create elements/widgets
        self.space_label1_1 = tk.Label(self, height=8, width=50, bg='black')
        self.space_label2 = tk.Label(self, height=1, bg='black')
        #self.space_label3 = tk.Label(self, height=1, bg='black')
        self.line_label1 = tk.Label(self,  width=1000, bg='green')
        self.title_label = tk.Label(self, text='Upcoming Events You May Be Interested', font='Impact 16 underline', background='green')
        self.user_label = tk.Label(self, text='Username', font='Impact 16 underline', background='green')

        image = Image.open("images/round_rect.png")
        photo = ImageTk.PhotoImage(image.resize((710, 300), Image.ANTIALIAS))
        self.rect_label = tk.Label(self, image=photo, bg='green', fg='black', relief='solid')

        self.event_left = tk.PhotoImage(file="images/img_login_left.png")
        self.event_left_btn = tk.Button(self, image=self.event_left, bg="white", bd="3", relief="raised")
        self.event_right = tk.PhotoImage(file="images/img_login.png")
        self.event_right_btn = tk.Button(self, image=self.event_right, bg="white", bd="3", relief="raised")

        self.event_focus = tk.PhotoImage(file="images/blank_image_icon.png")
        self.event_focus_btn = tk.Button(self, image=self.event_focus)

        image1 = Image.open("images/round_rect.png")
        photo1 = ImageTk.PhotoImage(image1.resize((710, 300), Image.ANTIALIAS))
        self.rect_label_2 = tk.Label(self, image=photo1, bg='green', fg='black', relief='solid')
        #Popup filter
        def popup_window():
            window = tk.Toplevel()
            window.geometry("350x380")
            window.config(bg='orange')
            label = tk.Label(window, text="Preference For Users", font='Bahnschrift 18 underline bold', bg='orange', relief='solid', bd=2, pady=10)
            label.pack(fill='x', ipady=8)
            window.proficient = tk.StringVar(window)
            window.proficient.set("Proficiencies")  # default value
            window.proficiencies = tk.OptionMenu(window, window.proficient, "Python", "C#", "C++", "C", "Java")
            window.proficiencies.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
            proficient_menu = window.nametowidget(window.proficiencies.menuname)
            proficient_menu.configure(font='Bahnschrift 12 bold')
            window.proficiencies.pack(fill='x', ipady=5, pady=10)

            window.experiences = tk.StringVar(window)
            window.experiences.set("Experiences")  # default value
            window.experience_dropdown = tk.OptionMenu(window, window.experiences, "<1Y", "1Y", "2Y", "3Y", ">3Y")
            window.experience_dropdown.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
            experience_menu = window.nametowidget(window.experience_dropdown.menuname)
            experience_menu.configure(font='Bahnschrift 12 bold')
            window.experience_dropdown.pack(fill='x', ipady=5, pady=10)

            window.meetup = tk.StringVar(window)
            window.meetup.set("Meet Up Preferences")  # default value
            window.meetup_dropdown = tk.OptionMenu(window, window.meetup, "Meet Up", "Virtual Meeting", "No Preference")
            window.meetup_dropdown.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
            meetup_menu = window.nametowidget(window.meetup_dropdown.menuname)
            meetup_menu.configure(font='Bahnschrift 12 bold')
            window.meetup_dropdown.pack(fill='x', ipady=5, pady=10)

            window.locale = tk.StringVar(window)
            window.locale.set("Country/Location")  # default value
            window.locale_dropdown = tk.OptionMenu(window, window.locale, "Singapore", "Malaysia", "Indonesia")
            window.locale_dropdown.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
            locale_menu = window.nametowidget(window.locale_dropdown.menuname)
            locale_menu.configure(font='Bahnschrift 12 bold')
            window.locale_dropdown.pack(fill='x', ipady=5, pady=10)
            def submit_filter():
                window.destroy()
            button_close = tk.Button(window, text="Submit", command=submit_filter)
            button_close.pack(fill='x', pady=10)

        self.load_filter_img = Image.open("images/filter_icon.png")
        self.filter_img = ImageTk.PhotoImage(self.load_filter_img.resize((50, 50), Image.ANTIALIAS))
        self.filter_button = tk.Button(self, image=self.filter_img, command=popup_window)
        self.user_left = tk.PhotoImage(file="images/img_login_left.png")
        self.user_left_btn = tk.Button(self, image=self.user_left, bg="white", bd="3", relief="raised")
        self.user_right = tk.PhotoImage(file="images/img_login.png")
        self.user_right_btn = tk.Button(self, image=self.user_right, bg="white", bd="3", relief="raised")

        self.user_image = tk.PhotoImage(file="images/profile_icon.png")
        self.user_image_Button = tk.Button(self, image=self.user_image)

        self.user_desc_label = tk.Label(self, text='description...', bg='green', fg='black')

        #arrange elements & widgets in grid
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
        self.rect_label.place(x=350, y=180)
        self.title_label.tkraise()
        self.title_label.place(x=530, y=190)
        self.event_left_btn.place(x=400, y=300)
        self.event_focus_btn.place(x=640, y=270)
        self.event_right_btn.place(x=960, y=300)
        #self.line_label1.place(x=0, y=500)
        self.rect_label_2.place(x=350, y=540)
        self.user_label.tkraise()
        self.user_label.place(x=660, y=560)
        self.filter_button.place(x=960, y=560)
        self.user_left_btn.place(x=400, y=670)
        self.user_image_Button.place(x=640, y=630)
        self.user_right_btn.place(x=960, y=670)
        self.user_desc_label.place(x=670, y=800)

class Search_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='red')
        self.controller = controller

        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg='orange', borderwidth=2, relief='solid')

        def goto_recs():
            controller.show_frame('Recs_page')

        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="orange", bd="3", height=130, relief="raised",
                                  command=goto_recs)

        def goto_search():
            controller.show_frame('Search_page')

        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=goto_search)

        def goto_events():
            controller.show_frame('Events_page')

        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=goto_events)

        def goto_contacts():
            controller.show_frame('Contacts_page')

        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="orange", bd="3", height=130,
                                      relief="raised", command=goto_contacts)

        def goto_profile():
            controller.show_frame('Profile_page')

        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="orange", bd="3", height=130,
                                     relief="raised", command=goto_profile)
        # End of Toolbar

        #add elemets & widgets
        self.user_label = tk.Label(self, text='Looking for someone...?', font='Bahnschrift 40 bold underline', bg='red')
        self.search_user = tk.Entry(self, font=('arial', 18), width=30, relief='solid', bd=2)
        self.search_user.pack(ipady=18)
        self.usersearch_button = tk.Button(self, text='Search', font='Bahnschrift 16 bold', bg='red', relief='solid')
        self.rect_label_1 = tk.Label(self, bg='orange', fg='black', relief='solid', height='10', width='80')
        self.load_randomuser1_img = tk.PhotoImage(file='images/profile_icon.png')
        self.randomuser1_img = tk.Label(self, image=self.load_randomuser1_img, bg='orange')
        self.randomuser1_username = tk.Label(self, text='Username', font='Bahnschrift 20 underline bold', bg='orange')
        self.randomuser1_desc = tk.Label(self, text='Experience Description...', font='Bahnschrift 14 bold', bg='orange')
        self.load_add_img = tk.PhotoImage(file='images/add_user_img.png')
        self.add_img_btn1 = tk.Button(self, image=self.load_add_img, bg='orange')
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
        self.randomuser1_username.place(x=630, y=330)
        self.randomuser1_desc.place(x=630, y=400)
        self.add_img_btn1.place(x=900, y=360)
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

class Events_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='yellow')
        self.controller = controller

        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg='orange', borderwidth=2, relief='solid')

        def goto_recs():
            controller.show_frame('Recs_page')

        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="orange", bd="3", height=130, relief="raised",
                                  command=goto_recs)

        def goto_search():
            controller.show_frame('Search_page')

        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=goto_search)

        def goto_events():
            controller.show_frame('Events_page')

        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=goto_events)

        def goto_contacts():
            controller.show_frame('Contacts_page')

        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="orange", bd="3", height=130,
                                      relief="raised", command=goto_contacts)

        def goto_profile():
            controller.show_frame('Profile_page')

        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="orange", bd="3", height=130,
                                     relief="raised", command=goto_profile)
        # End of Toolbar

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

class Contacts_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller
        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg='orange', borderwidth=2, relief='solid')

        def goto_recs():
            controller.show_frame('Recs_page')

        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="orange", bd="3", height=130, relief="raised",
                                  command=goto_recs)

        def goto_search():
            controller.show_frame('Search_page')

        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=goto_search)

        def goto_events():
            controller.show_frame('Events_page')

        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=goto_events)

        def goto_contacts():
            controller.show_frame('Contacts_page')

        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="orange", bd="3", height=130,
                                      relief="raised", command=goto_contacts)

        def goto_profile():
            controller.show_frame('Profile_page')

        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="orange", bd="3", height=130,
                                     relief="raised", command=goto_profile)
        # End of Toolbar

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

class Profile_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='green')
        self.controller = controller
        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg='orange', borderwidth=2, relief='solid')

        def goto_recs():
            controller.show_frame('Recs_page')

        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="orange", bd="3", height=130, relief="raised",
                                  command=goto_recs)

        def goto_search():
            controller.show_frame('Search_page')

        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=goto_search)

        def goto_events():
            controller.show_frame('Events_page')

        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=goto_events)

        def goto_contacts():
            controller.show_frame('Contacts_page')

        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="orange", bd="3", height=130,
                                      relief="raised", command=goto_contacts)

        def goto_profile():
            controller.show_frame('Profile_page')

        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="orange", bd="3", height=130,
                                     relief="raised", command=goto_profile)
        # End of Toolbar

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
'''
if __name__ == "__main__":
    app = BinaryApp()
    app.mainloop()