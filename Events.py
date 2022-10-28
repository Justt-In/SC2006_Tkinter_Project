import tkinter as tk
import psycopg2
import customtkinter
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import sqlite3

class Events_page(customtkinter.CTkFrame):

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
        self.recs_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Recommendations',
                                                text_color=textColour,
                                                text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                command=lambda: controller.show_frame("Recs_page"))
        self.search_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Search Users', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                  command=lambda: controller.show_frame("Search_page"))
        self.events_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='View Events', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour2,
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

        #Create elements and widgets
        #Top Left backdrop
        self.load_main_img1 = Image.open("images/hackathon.png")
        self.hack_main_img = ImageTk.PhotoImage(self.load_main_img1.resize((450, 230), Image.ANTIALIAS))
        self.hack_backdrop = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, corner_radius=20,
                                                    text="", width=500, height=250)
        self.hack_label = customtkinter.CTkLabel(self, text='Hackathon', text_font=['Bahnschrift bold', 32],
                                                 bg_color=accentColour, text_color=textColour)
        #This function opens up a new window and displays all hackathons uploaded into the system by the admin
        def hackathon_view():
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            #get data from database
            hCursor.execute("SELECT (SELECT count(*) FROM Events WHERE event_type = '{0}') as count".format('Hackathon'))
            count = hCursor.fetchall()
            count = count[0][0]
            hCursor.execute("SELECT * FROM Events WHERE event_type = '{0}'".format('Hackathon'))
            query_data = hCursor.fetchall()
            #This function populates a grid with all the events related to the event type
            def populate(newWindow):
                self.picture = {}
                self.resized_image = {}
                self.open_image = {}
                for row in range(count):
                    '''
                    print(query_data[row][1])
                    print(query_data[row][4])
                    print(query_data[row][3])
                    print(query_data[row][5])
                    print(query_data[row][7])
                    '''
                    #filepath = "images/" + query_data[row][1][25:]
                    filepath = str(query_data[row][1])
                    print(filepath)
                    self.open_image = Image.open(filepath)
                    self.resized_image[row] = ImageTk.PhotoImage(self.open_image.resize((200, 150), Image.ANTIALIAS))
                    self.picture[row] = tk.Label(newWindow, image=self.resized_image[row], bg='#33A1FD', relief='solid').grid(row=row, column=0)
                    info_text = query_data[row][4]+ '\n' + query_data[row][3] + '\n' + query_data[row][5]
                    tk.Label(newWindow, text=info_text, font='Bahnschrift 24 bold', bg='#33A1FD').grid(row=row, column=1)
                    tk.Label(newWindow, text=query_data[row][7], font='Bahnschrift 16 bold', bg='#33A1FD').grid(row=row, column=2)

            def onFrameConfigure(canvas):
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("1000x500")
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
            hConn.close()
        self.hack_btn = customtkinter.CTkButton(self, image=self.hack_main_img, text="Click For More!",
                                                text_color=textColour, text_font=['trebuchet MS bold', 14],
                                                compound='top', bg_color=accentColour, fg_color=accentColour,
                                                command=hackathon_view)

        # Top Right backdrop
        self.load_main_img2 = Image.open("images/codathon.png")
        self.code_main_img = ImageTk.PhotoImage(self.load_main_img2.resize((450, 230), Image.ANTIALIAS))
        self.code_backdrop = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, corner_radius=20,
                                                    text="", width=500, height=250)
        self.code_label = customtkinter.CTkLabel(self, text='Codathon', text_font=['Bahnschrift bold', 32],
                                                 bg_color=accentColour, text_color=textColour)
        # This function opens up a new window and displays all codathons uploaded into the system by the admin
        def codathon_view():
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            # get data from database
            hCursor.execute("SELECT (SELECT count(*) FROM Events WHERE event_type = '{0}') as count".format('Codathon'))
            count = hCursor.fetchall()
            count = count[0][0]
            hCursor.execute("SELECT * FROM Events WHERE event_type = '{0}'".format('Codathon'))
            query_data = hCursor.fetchall()

            # This function popualtes a grid with all the events related to the event type
            def populate(newWindow):
                self.picture = {}
                self.resized_image = {}
                self.open_image = {}
                for row in range(count):
                    '''
                    print(query_data[row][1])
                    print(query_data[row][4])
                    print(query_data[row][3])
                    print(query_data[row][5])
                    print(query_data[row][7])
                    '''
                    '''
                    fileLocale = str(query_data[row][1])
                    fileLocale = fileLocale.split("/")
                    fileLocale = fileLocale[-1]
                    filepath = "images/" + fileLocale
                    '''
                    filepath = str(query_data[row][1])
                    self.open_image = Image.open(filepath)
                    self.resized_image[row] = ImageTk.PhotoImage(self.open_image.resize((200, 150), Image.ANTIALIAS))
                    self.picture[row] = tk.Label(newWindow, image=self.resized_image[row], bg='#33A1FD',
                                                 relief='solid').grid(row=row, column=0)
                    info_text = query_data[row][4] + '\n' + query_data[row][3] + '\n' + query_data[row][5]
                    tk.Label(newWindow, text=info_text, font='Bahnschrift 24 bold', bg='#33A1FD').grid(row=row,
                                                                                                       column=1)
                    tk.Label(newWindow, text=query_data[row][7], font='Bahnschrift 16 bold', bg='#33A1FD').grid(row=row,
                                                                                                                column=2)

            def onFrameConfigure(canvas):
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("1000x500")
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
            hConn.close()
        self.code_btn = customtkinter.CTkButton(self, image=self.code_main_img, text="Click For More!",
                                                text_color=textColour, text_font=['trebuchet MS bold', 14],
                                                compound='top', bg_color=accentColour, fg_color=accentColour,
                                                command=codathon_view)

        # Bottom Left backdrop
        self.load_main_img3 = Image.open("images/bug_hunt.jpg")
        self.bug_main_img = ImageTk.PhotoImage(self.load_main_img3.resize((450, 230), Image.ANTIALIAS))
        self.bug_backdrop = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, corner_radius=20,
                                                    text="", width=500, height=250)
        self.bug_label = customtkinter.CTkLabel(self, text='Bug Hunts', text_font=['Bahnschrift bold', 32],
                                                 bg_color=accentColour, text_color=textColour)

        def bug_view():
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            #get data from database
            hCursor.execute("SELECT (SELECT count(*) FROM Events WHERE event_type = '{0}') as count".format('Bug Hunt'))
            count = hCursor.fetchall()
            count = count[0][0]
            hCursor.execute("SELECT * FROM Events WHERE event_type = '{0}'".format('Bug Hunt'))
            query_data = hCursor.fetchall()
            #This function populates a grid with all the events related to the event type
            def populate(newWindow):
                for row in range(count):
                    '''
                    print(query_data[row][1])
                    print(query_data[row][4])
                    print(query_data[row][3])
                    print(query_data[row][5])
                    print(query_data[row][7])
                    '''
                    #filepath = "images/" + query_data[row][1][25:]
                    filepath = str(query_data[row][1])
                    self.open_image = Image.open(filepath)
                    self.resized_image = ImageTk.PhotoImage(self.open_image.resize((200, 150), Image.ANTIALIAS))
                    tk.Label(newWindow, image=self.resized_image, bg='#33A1FD', relief='solid').grid(row=row, column=0)
                    info_text = query_data[row][4]+ '\n' + query_data[row][3] + '\n' + query_data[row][5]
                    tk.Label(newWindow, text=info_text, font='Bahnschrift 24 bold', bg='#33A1FD').grid(row=row, column=1)
                    tk.Label(newWindow, text=query_data[row][7], font='Bahnschrift 16 bold', bg='#33A1FD').grid(row=row, column=2)

            def onFrameConfigure(canvas):
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("1000x500")
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
            hConn.close()
        self.bug_btn = customtkinter.CTkButton(self, image=self.bug_main_img, text="Click For More!",
                                                text_color=textColour, text_font=['trebuchet MS bold', 14],
                                                compound='top', bg_color=accentColour, fg_color=accentColour,
                                                command=bug_view)

        # Bottom Right backdrop
        self.load_main_img4 = Image.open("images/seminars.jpg")
        self.seminar_main_img = ImageTk.PhotoImage(self.load_main_img4.resize((450, 230), Image.ANTIALIAS))
        self.seminar_backdrop = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, corner_radius=20,
                                                   text="", width=500, height=250)
        self.seminar_label = customtkinter.CTkLabel(self, text='Seminars and Olympiads', text_font=['Bahnschrift bold', 30],
                                                bg_color=accentColour, text_color=textColour)
        def SnO_view():
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            #get data from database
            hCursor.execute("SELECT (SELECT count(*) FROM Events WHERE event_type = '{0}') as count".format('Seminars & Olympiads'))
            count = hCursor.fetchall()
            count = count[0][0]
            hCursor.execute("SELECT * FROM Events WHERE event_type = '{0}'".format('Seminars & Olympiads'))
            query_data = hCursor.fetchall()
            #This function populates a grid with all the events related to the event type
            def populate(newWindow):
                for row in range(count):
                    '''
                    print(query_data[row][1])
                    print(query_data[row][4])
                    print(query_data[row][3])
                    print(query_data[row][5])
                    print(query_data[row][7])
                    '''
                    #filepath = "images/" + query_data[row][1][25:]
                    filepath = str(query_data[row][1])
                    self.open_image = Image.open(filepath)
                    self.resized_image = ImageTk.PhotoImage(self.open_image.resize((200, 150), Image.ANTIALIAS))
                    tk.Label(newWindow, image=self.resized_image, bg='#33A1FD', relief='solid').grid(row=row, column=0)
                    info_text = query_data[row][4]+ '\n' + query_data[row][3] + '\n' + query_data[row][5]
                    tk.Label(newWindow, text=info_text, font='Bahnschrift 24 bold', bg='#33A1FD').grid(row=row, column=1)
                    tk.Label(newWindow, text=query_data[row][7], font='Bahnschrift 16 bold', bg='#33A1FD').grid(row=row, column=2)

            def onFrameConfigure(canvas):
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("1000x500")
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
            hConn.close()
        self.seminar_btn = customtkinter.CTkButton(self, image=self.seminar_main_img, text="Click For More!",
                                               text_color=textColour, text_font=['trebuchet MS bold', 14],
                                               compound='top', bg_color=accentColour, fg_color=accentColour,
                                               command=SnO_view)

        # arrange elements & widgets in grid
        self.recs_btn.place(x=2, y=2)
        self.search_btn.place(x=158, y=2)
        self.events_btn.place(x=300, y=2)
        self.contacts_btn.place(x=442, y=2)
        self.profile_btn.place(x=584, y=2)

        # Top-left backdrop
        self.hack_backdrop.place(x=100, y=190)
        self.hack_label.place(x=250, y=190)
        self.hack_btn.place(x=190, y=245)
        # Top-Right backdrop
        self.code_backdrop.place(x=680, y=190)
        self.code_label.place(x=830, y=190)
        self.code_btn.place(x=770, y=245)
        # Bottom-left backdrop
        self.bug_backdrop.place(x=100, y=450)
        self.bug_label.place(x=250, y=450)
        self.bug_btn.place(x=190, y=505)
        # Bottom-Right backdrop
        self.seminar_backdrop.place(x=680, y=450)
        self.seminar_label.place(x=700, y=450)
        self.seminar_btn.place(x=770, y=505)