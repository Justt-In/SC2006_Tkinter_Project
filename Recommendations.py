import tkinter as tk
import psycopg2
from tkinter import filedialog
from tkinter import scrolledtext
import Contacts
import customtkinter
from PIL import ImageTk, Image
import sqlite3


row = 0
index = 0
Filterlist = []
RecsList = []
recsOrfilter = 0
class Recs_page(customtkinter.CTkFrame):

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
        #Toolbar
        #Top Toolbar
        # Create Canvas
        canvas1 = tk.Canvas(self, width=400, height=250, bd=0, highlightthickness=0)
        canvas1.pack(fill="x", side='top')

        # Display image

        self.toolbarImg = Image.open(path)
        self.toolbarImg = ImageTk.PhotoImage(self.toolbarImg.resize((1930, 300), Image.ANTIALIAS))
        canvas1.create_image(0, 0, image=self.toolbarImg, anchor="nw")
        self.recs_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Recommendations', text_color=textColour,
                                                text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour2,
                                                command=lambda: controller.show_frame("Recs_page"))
        self.search_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='Search Users', text_color=textColour,
                                                text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                command=lambda: controller.show_frame("Search_page"))
        self.events_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='View Events', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                  command=lambda: controller.show_frame("Events_page"))
        self.contacts_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='My Contacts', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                  command=lambda: controller.show_frame("Contacts_page"))
        self.profile_btn = customtkinter.CTkButton(self, bg_color=toolbar_bg, text='My Profile', text_color=textColour,
                                                  text_font=['trebuchet MS bold', 12], height=30, fg_color=accentColour,
                                                  command=lambda: controller.show_frame("Profile_page"))
        #End of Toolbar

        #create elements/widgets
        self.rect_label1 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, height=500, width=500,
                                                 corner_radius=20, text="")
        self.title_label = customtkinter.CTkLabel(self, text='Upcoming Events You May Be Interested In',
                                                  text_font=['trebuchet MS bold', 16], bg_color=accentColour,
                                                  fg_color=accentColour, text_color=textColour)
        self.event_focus = tk.PhotoImage(file="images/blank_image_icon.png")
        self.event_name_label = tk.Label(self, text="Event Name", font='Bahnschrift 30 bold', bg=accentColour,
                                         fg=textColour)

        def Event_Details():
            """
            Gets event details of chosen event and displays in popup window
            :return: Creates pop up window and displays data
            """
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            hCursor.execute('SELECT * FROM Events ORDER BY eventid ASC')
            query_data = hCursor.fetchall()

            # This function popualtes a grid with all the event details
            def populate(newWindow):
                """
                Populate popup window with gathered data in a grid style manner
                :param newWindow:
                :return:
                """
                self.picture = {}
                self.resized_image = {}
                self.open_image = {}
                filepath = query_data[row][1]
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
                """
                Binds scrollbar to x and y axis and resets scroll to encompass the inner frame
                :param canvas:
                :return:
                """
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("800x300")
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

        hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                 user="wfpsdpcxvibamf",
                                 password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                 port="5432")
        hCursor = hConn.cursor()
        hCursor.execute('SELECT * FROM Events')
        query_data = hCursor.fetchall()
        filepath = query_data[row][1]
        event_name = query_data[row][4]
        load_profile_pic = Image.open(filepath)
        self.event_focus = ImageTk.PhotoImage(load_profile_pic.resize((450, 300), Image.ANTIALIAS))
        self.event_focus_btn = tk.Button(self, image=self.event_focus, bg=accentColour2, fg=textColour,
                                         command=Event_Details)
        self.event_name_label["text"] = str(event_name)


        def Event_right():
            """
            Gets the data of the next event in the list to display, from the database
            Else resets to first event in the list
            :return: Returns next event in the list
            """
            global row
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            hCursor.execute('SELECT * FROM Events')
            query_data = hCursor.fetchall()
            count = hConn.cursor()
            count.execute('SELECT COUNT(*) FROM Events')
            count_data = count.fetchone()[0]
            if row == count_data:
                row = 0
            else:
                row += 1
            filepath = query_data[row][1]
            event_name = query_data[row][4]
            load_profile_pic = Image.open(filepath)
            self.event_focus = ImageTk.PhotoImage(load_profile_pic.resize((450, 300), Image.ANTIALIAS))
            self.event_focus_btn.config(image=self.event_focus)
            if  len(str(event_name)) > 30:
                self.event_name_label.configure(font='Bahnschrift 20 bold')
                self.event_name_label.place(x=150, y=400)
            elif len(str(event_name)) > 25:
                self.event_name_label.configure(font='Bahnschrift 20 bold')
                self.event_name_label.place(x=220, y=400)
            elif len(str(event_name)) > 20:
                self.event_name_label.configure(font='Bahnschrift 25 bold')
                self.event_name_label.place(x=220, y=400)
            else:
                self.event_name_label.configure(font='Bahnschrift 30 bold')
                self.event_name_label.place(x=290, y=400)
            self.event_name_label["text"] = str(event_name)
            hConn.close()

        def Event_left():
            """
            Gets the data of the previous event in the list to display, from the database
            Else resets to last event in the list
            :return: Returns next event in the list
            """
            global row
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            hCursor.execute('SELECT * FROM Events')
            query_data = hCursor.fetchall()
            count = hConn.cursor()
            count.execute('SELECT COUNT(*) FROM Events')
            count_data = count.fetchone()[0]
            if row == 0:
                row = count_data
            else:
                row -= 1
            filepath = query_data[row][1]
            event_name = query_data[row][4]
            load_profile_pic = Image.open(filepath)
            self.event_focus = ImageTk.PhotoImage(load_profile_pic.resize((450, 300), Image.ANTIALIAS))
            self.event_focus_btn.config(image=self.event_focus)
            if len(str(event_name)) > 30:
                self.event_name_label.configure(font='Bahnschrift 20 bold')
                self.event_name_label.place(x=150, y=400)
            elif len(str(event_name)) > 25:
                self.event_name_label.configure(font='Bahnschrift 20 bold')
                self.event_name_label.place(x=220, y=400)
            elif len(str(event_name)) > 20:
                self.event_name_label.configure(font='Bahnschrift 25 bold')
                self.event_name_label.place(x=220, y=400)
            else:
                self.event_name_label.configure(font='Bahnschrift 30 bold')
                self.event_name_label.place(x=290, y=400)
            self.event_name_label["text"] = str(event_name)
            hConn.close()

        loadimage = Image.open("images/left_btn.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        self.event_left_btn = customtkinter.CTkButton(self, text="Prev", bg_color=accentColour, fg_color=accentColour2,
                                                      text_font=['trebuchet MS bold', 14], text_color=textColour,
                                                      image=loadimage, compound="top", command=Event_left)

        loadimage = Image.open("images/right_btn.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        self.event_right_btn = customtkinter.CTkButton(self, text="Next", bg_color=accentColour, fg_color=accentColour2,
                                                       text_font=['trebuchet MS bold', 14], text_color=textColour,
                                                       image=loadimage, compound="top", command=Event_right)

        #User Recommendations
        #pref_text = '\n'.join(pref_languages[1:])

        self.rect_label2 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, height=500, width=500,
                                                 corner_radius=20, text="")
        self.title_label2 = customtkinter.CTkLabel(self, text='Recommended Users',
                                                  text_font=['trebuchet MS bold', 16], bg_color=accentColour,
                                                  fg_color=accentColour, text_color=textColour)
        self.block_label = tk.Label(self, bg=accentColour, width=73, height=26)
        self.user_label = tk.Label(self, text='Username', font='Bahnschrift 30 bold', bg=accentColour, fg=textColour)

        def view_user_prof():
            """
            Gets selected user's data from the database and displays in popup winddow
            :return: Gets user data and displays it in popup window
            """
            username = self.user_label.cget('text')
            if username == "Username":
                return
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com",
                                            database="ddipmu7if1umsi",
                                            user="wfpsdpcxvibamf",
                                            password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                            port="5432")
            hCursor = hConn.cursor()
            hCursor.execute('SELECT * FROM Users WHERE username = %s', [username])
            newWindow = tk.Toplevel(parent)
            newWindow.title(username + "'s Profile")
            newWindow.geometry("650x800")
            newWindow.configure(bg='#33A1FD')
            query_data = hCursor.fetchall()
            newWindow.username = tk.Label(newWindow, text='Username', bg='#33A1FD', fg='black', font='Bahnschrift 24 bold underline')
            newWindow.username.pack(side='top')
            newWindow.username["text"] = str(query_data[0][8])
            try:
                filepath = query_data[0][1]
                if filepath == None or filepath == '':
                    filepath = "images/default_profile_img.png"
                else:
                    filepath = str(query_data[0][1])
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
            newWindow.code_lang["text"] = code_text
            newWindow.short_desc = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 12 bold', bd=3, relief='solid')
            newWindow.short_desc.pack(side='top', fill='x')
            newWindow.short_desc["text"] = str(query_data[0][18])
            newWindow.meetMode = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetMode.pack(side='top')
            newWindow.meetMode["text"] = "Meeting Preference: " + query_data[0][14]
            newWindow.meetLocale = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.meetLocale.pack(side='top')
            newWindow.meetLocale["text"] = "Location Preference: " + query_data[0][15]
            newWindow.nationality = tk.Label(newWindow, text='', bg='#33A1FD', fg='black', font='Bahnschrift 14 bold')
            newWindow.nationality.pack(side='top')
            newWindow.nationality["text"] = "Nationality: " + query_data[0][7]
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
            hConn.close()

        self.user_image = tk.PhotoImage(file="images/profile_icon.png")
        self.user_image_Button = tk.Button(self, image=self.user_image, bg=accentColour2, fg=textColour, command=view_user_prof)
        self.user_desc_label = tk.Label(self, text='description...', bg=accentColour, fg='black')

        def view_recs():
            """
            Gets list of recommended users based on logged-in user's preferences stored in the database
            Displays first user's data on the page
            :return: list of recommended users and first user in the list
            """
            hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                     user="wfpsdpcxvibamf",
                                     password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                     port="5432")
            hCursor = hConn.cursor()
            global RecsList
            # recslist = []  # add recommended USERNAMES here
            file = open("Databases/logs.txt", "r").read()
            username = file[:-1]  # Get current user's username
            hCursor.execute("SELECT users_preference FROM Users WHERE username = '{0}'".format(username))
            pref_data = hCursor.fetchall()
            pref_languages = pref_data[0][0]
            pref_languages = pref_languages.split(',')
            pref_languages.pop(0)
            for lang in pref_languages:
                hCursor.execute("SELECT username FROM Users WHERE code_lang ILIKE '%{0}%'".format(lang[1:]))
                username_data = hCursor.fetchall()
                for x in username_data:
                    if x in RecsList:
                        continue
                    else:
                        RecsList.append(x)
            firstUser = RecsList[0][0]
            self.user_label["text"] = str(firstUser)
            hCursor.execute("SELECT profile_pic, short_Desc FROM Users WHERE username = '{0}'".format(firstUser))
            details = hCursor.fetchall()
            filepath = details[0][0]
            shortDesc = details[0][1]
            self.newImg = Image.open(filepath)
            self.newImg = ImageTk.PhotoImage(self.newImg.resize((256, 256), Image.ANTIALIAS))
            self.user_image_Button.config(image=self.newImg)
            self.user_desc_label["text"] = str(shortDesc)
            self.block_label.lower()

        self.load_recs_img = Image.open("images/default_profile_img.png")
        self.recs_img = ImageTk.PhotoImage(self.load_recs_img.resize((50, 50), Image.ANTIALIAS))
        self.view_recs_btn = customtkinter.CTkButton(self, image=self.recs_img, command=view_recs, text="",
                                                     bg_color=accentColour, fg_color=accentColour2, width=30)

        # Popup filter
        def popup_window():
            """
            Creates popup window for users to select filters, ranked based on best to worst match (meets the
            requirements best to worst)
            :return:
            """
            window = customtkinter.CTkToplevel()
            window.title("User Filtering")
            window.geometry("350x380")
            if customtkinter.get_appearance_mode() == "light" or customtkinter.get_appearance_mode() == "Light":
                path = "images/toolbar_image2.jpg"
                main_bg = "#ffe5d9"
                accentColour = "#48CAE4"
                accentColour2 = "#E46248"
                accentColour3 = "#00b4d8"
                textColour = "black"
            else:
                path = "images/toolbar_image1.png"
                main_bg = "#464646"
                accentColour = "#0077b6"
                accentColour2 = "#B63F00"
                accentColour3 = "#00b4d8"
                textColour = "black"
            window.config(bg=main_bg)
            label = customtkinter.CTkLabel(window, text="Preference For Users", text_font=['trebuchet MS bold', 18],
                                           bg=main_bg, fg_color=accentColour, text_color=textColour)
            label.pack(fill='x', ipady=8)

            window.proficiencies = customtkinter.CTkOptionMenu(window, values=["Python", "C#", "C++", "C", "Java",
                                                                             "Javascript", "PHP", "SQL", "HTML", "CSS"])
            window.proficiencies.set("Coding Language")
            window.proficiencies.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                       text_color=textColour, button_color=accentColour, dropdown_color=accentColour,
                                       dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold')
            window.proficiencies.pack(fill='x', ipady=5, pady=10)

            window.experience_dropdown = customtkinter.CTkOptionMenu(window, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
            window.experience_dropdown.set("Experiences")
            window.experience_dropdown.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour,
                                           text_color=textColour, button_color=accentColour,
                                           dropdown_color=accentColour,
                                           dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold')
            window.experience_dropdown.pack(fill='x', ipady=5, pady=10)

            window.meetup_dropdown = customtkinter.CTkOptionMenu(window, values=["Meet Up", "Virtual Meeting", "No Preference"])
            window.meetup_dropdown.set("Meet Up Preference")
            window.meetup_dropdown.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg,
                                                 fg_color=accentColour,
                                                 text_color=textColour, button_color=accentColour,
                                                 dropdown_color=accentColour,
                                                 dropdown_text_color=textColour,
                                                 dropdown_text_font='Bahnschrift 12 bold')
            window.meetup_dropdown.pack(fill='x', ipady=5, pady=10)

            window.locale_dropdown = customtkinter.CTkOptionMenu(window,values=["Central SG", "North SG",
                                                                                "East SG", "South SG", "West SG"])
            window.locale_dropdown.set("Meeting Location")
            window.locale_dropdown.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg,
                                             fg_color=accentColour,
                                             text_color=textColour, button_color=accentColour,
                                             dropdown_color=accentColour,
                                             dropdown_text_color=textColour,
                                             dropdown_text_font='Bahnschrift 12 bold')
            window.locale_dropdown.pack(fill='x', ipady=5, pady=10)

            def submit_filter():
                """
                Searches the database and returns a list of users, displays the first user's data on screen
                :return: list of users ranked from best to worst
                """
                hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                         user="wfpsdpcxvibamf",
                                         password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                         port="5432")
                hCursor = hConn.cursor()
                proficiency = window.proficiencies.get()
                experience = window.experience_dropdown.get()
                meetup = window.meetup_dropdown.get()
                locale = window.locale_dropdown.get()

                global Filterlist
                #recslist = []  # add recommended USERNAMES here

                file = open("Databases/logs.txt", "r").read()
                username = file[:-1]  # Get current user's username

                hCursor.execute("SELECT username FROM Users WHERE username != %s", [username])
                userlist = hCursor.fetchall()  # Every other user's username

                for user in userlist:
                    matchrank = 0

                    # Match proficiencies, string split() , and space to separate proficiency and experience
                    # Language proficiency should have a higher weighting
                    hCursor.execute("SELECT code_lang FROM Users WHERE username = %s", user)
                    inter1 = hCursor.fetchall()
                    inter2 = inter1[0][0].split(", ")  # Returns list
                    inter2 = [x for x in inter2 if x != '']
                    for i in range(0, len(inter2)):
                        inter2[i] = inter2[i].split(" ")
                    # print(user, inter2)  # Debug function
                    for j in inter2:
                        if proficiency == j[0]:  # Language must match before checking experience
                            if experience == j[1]:
                                # print("Good match, ", proficiency, experience)  # Debug function
                                matchrank += 3  # Higher weighting since both lang and exp are same
                            else:
                                # print("Okay match, ", proficiency, experience)  # Debug function
                                matchrank += 2  # Lower weighting since same language but differing

                    # Match meetup
                    hCursor.execute("SELECT meeting_mode FROM Users WHERE username = %s", user)
                    meetmode = hCursor.fetchall()
                    if meetup == meetmode[0][0]:
                        # print("Meetup match, ", meetup)  # Debug function
                        matchrank += 1  # Arbitrary weightage

                    # Match locale
                    hCursor.execute("SELECT meeting_region FROM Users WHERE username = %s", user)
                    meetregion = hCursor.fetchall()
                    if locale == meetregion[0][0]:
                        # print("Locale match, ", locale)  # Debug function
                        matchrank += 2  # Arbitrary weightage

                    # Append username and rank in 2d list
                    Filterlist.append([user, matchrank])

                # Sort recslist based on highest match ranking
                recslist = sorted(Filterlist, key=lambda l: l[1], reverse=True)
                global recsOrfilter
                recsOrfilter = 1
                self.user_label["text"] = str(Filterlist[0][0][0])
                label_name = self.user_label.cget("text")
                hCursor.execute("SELECT profile_pic, short_Desc FROM Users WHERE username = '{0}'".format(label_name))
                details = hCursor.fetchall()
                filepath = details[0][0]
                shortDesc = details[0][1]
                self.newImg = Image.open(filepath)
                self.newImg = ImageTk.PhotoImage(self.newImg.resize((256,256), Image.ANTIALIAS))
                self.user_image_Button.config(image=self.newImg)
                self.user_desc_label["text"] = str(shortDesc)
                self.block_label.lower()
                window.destroy()

            button_close = customtkinter.CTkButton(window, text="Submit", command=submit_filter, bg_color=main_bg,
                                                       fg_color="#0d9c8c", text_color=textColour, text_font='Bahnschrift 12 bold')
            button_close.pack(fill='x', pady=10)

        self.load_filter_img = Image.open("images/filter_icon.png")
        self.filter_img = ImageTk.PhotoImage(self.load_filter_img.resize((50, 50), Image.ANTIALIAS))
        self.filter_button = customtkinter.CTkButton(self, image=self.filter_img, command=popup_window, text="",
                                                     bg_color=accentColour, fg_color=accentColour2, width=30)

        def filter_left():
            """
            Gets the next user's data in the list from the database, if end of the list, show first user's data.
            :return: Next user's data
            """
            global index
            if recsOrfilter == 0:
                iteratinglist = RecsList
                index -= 1
                try:
                    user_details = iteratinglist[index][0]
                except IndexError:
                    index = 0
                    user_details = iteratinglist[index][0]
                self.user_label["text"] = str(user_details)
                hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                         user="wfpsdpcxvibamf",
                                         password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                         port="5432")
                hCursor = hConn.cursor()
                hCursor.execute(
                    "SELECT profile_pic, short_Desc FROM Users WHERE username = '{0}'".format(str(user_details)))
                details = hCursor.fetchall()
                filepath = details[0][0]
                shortDesc = details[0][1]
                self.newImg = Image.open(filepath)
                self.newImg = ImageTk.PhotoImage(self.newImg.resize((256, 256), Image.ANTIALIAS))
                self.user_image_Button.config(image=self.newImg)
                self.user_desc_label["text"] = str(shortDesc)
            else:
                iteratinglist = Filterlist
                index -= 1
                if index == -1:
                    index = 0
                    return
                user_details = iteratinglist[index][0][0]
                self.user_label["text"] = str(user_details)
                hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                         user="wfpsdpcxvibamf",
                                         password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                         port="5432")
                hCursor = hConn.cursor()
                hCursor.execute("SELECT profile_pic, short_Desc FROM Users WHERE username = '{0}'".format(str(user_details)))
                details = hCursor.fetchall()
                filepath = details[0][0]
                shortDesc = details[0][1]
                self.newImg = Image.open(filepath)
                self.newImg = ImageTk.PhotoImage(self.newImg.resize((256, 256), Image.ANTIALIAS))
                self.user_image_Button.config(image=self.newImg)
                self.user_desc_label["text"] = str(shortDesc)

        loadimage = Image.open("images/left_btn.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        self.user_left_btn = customtkinter.CTkButton(self, text="Prev", bg_color=accentColour, fg_color=accentColour2,
                                                      text_font=['trebuchet MS bold', 14], text_color=textColour,
                                                      image=loadimage, compound="top", command=filter_left)

        def filter_right():
            """
            Gets the previous user's data in the list from the database, if end of the list, show last user's data.
            :return: Previous user's data
            """
            global index
            if recsOrfilter == 0:
                iteratinglist = RecsList
                index += 1
                try:
                    user_details = iteratinglist[index][0]
                except IndexError:
                    index = 0
                    user_details = iteratinglist[index][0]
                self.user_label["text"] = str(user_details)
                hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                         user="wfpsdpcxvibamf",
                                         password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                         port="5432")
                hCursor = hConn.cursor()
                hCursor.execute(
                    "SELECT profile_pic, short_Desc FROM Users WHERE username = '{0}'".format(str(user_details)))
                details = hCursor.fetchall()
                filepath = details[0][0]
                shortDesc = details[0][1]
                self.newImg = Image.open(filepath)
                self.newImg = ImageTk.PhotoImage(self.newImg.resize((256, 256), Image.ANTIALIAS))
                self.user_image_Button.config(image=self.newImg)
                self.user_desc_label["text"] = str(shortDesc)
            else:
                iteratinglist = Filterlist
                index += 1
                try:
                    user_details = iteratinglist[index][0][0]
                except IndexError:
                    index = 0
                    user_details = iteratinglist[index][0][0]
                self.user_label["text"] = str(user_details)
                hConn = psycopg2.connect(host="ec2-3-213-66-35.compute-1.amazonaws.com", database="ddipmu7if1umsi",
                                         user="wfpsdpcxvibamf",
                                         password="e8a06a9d3be5c23efeb96f72b24bcf22a213106090e7556d37ba5894ddfb4432",
                                         port="5432")
                hCursor = hConn.cursor()
                hCursor.execute(
                    "SELECT profile_pic, short_Desc FROM Users WHERE username = '{0}'".format(str(user_details)))
                details = hCursor.fetchall()
                filepath = details[0][0]
                shortDesc = details[0][1]
                self.newImg = Image.open(filepath)
                self.newImg = ImageTk.PhotoImage(self.newImg.resize((256, 256), Image.ANTIALIAS))
                self.user_image_Button.config(image=self.newImg)
                self.user_desc_label["text"] = str(shortDesc)

        loadimage = Image.open("images/right_btn.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        self.user_right_btn = customtkinter.CTkButton(self, text="Next", bg_color=accentColour, fg_color=accentColour2,
                                                       text_font=['trebuchet MS bold', 14], text_color=textColour,
                                                       image=loadimage, compound="top", command=filter_right)


        #arrange elements & widgets in grid
        self.recs_btn.place(x=2, y=2)
        self.search_btn.place(x=158, y=2)
        self.events_btn.place(x=300, y=2)
        self.contacts_btn.place(x=442, y=2)
        self.profile_btn.place(x=584, y=2)

        self.rect_label1.place(x=80, y=205)
        self.title_label.place(x=110, y=215)
        self.event_left_btn.place(x=100, y=620)
        self.event_name_label.place(x=290, y=400)
        self.event_focus_btn.place(x=260, y=510)
        self.event_right_btn.place(x=420, y=620)

        self.rect_label2.place(x=700, y=205)
        self.title_label2.place(x=850, y=215)
        self.block_label.place(x=1060, y=380)
        self.block_label.tkraise()
        self.user_label.place(x=1290, y=400)
        self.user_image_Button.place(x=1300, y=500)
        self.view_recs_btn.place(x=1100, y=215)
        self.filter_button.place(x=1140, y=215)
        self.user_left_btn.place(x=720, y=620)
        self.user_right_btn.place(x=1040, y=620)
        self.user_desc_label.place(x=1390, y=800)

if __name__ == "__main__":
    app = Recs_page()
    app.mainloop()

