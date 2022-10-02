import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import sqlite3

class Events_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='yellow')
        self.controller = controller

        # Toolbar
        # Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg="#ff8c1a", borderwidth=2, relief='solid')

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

        #Create elements and widgets
        #Top Left backdrop
        self.load_round_rect = Image.open("images/backdrop2.png")
        self.load_main_img1 = Image.open("images/hackathon.png")
        self.hack_main_img = ImageTk.PhotoImage(self.load_main_img1.resize((250, 150), Image.ANTIALIAS))
        self.next_img = tk.PhotoImage(file="images/img_login.png")

        self.backdrop_top_left = ImageTk.PhotoImage(self.load_round_rect.resize((500, 340), Image.ANTIALIAS))
        self.hack_backdrop = tk.Label(self, image=self.backdrop_top_left, bg='yellow')
        self.hack_label = tk.Label(self, text='Hackathon', font='Bahnschrift 32 bold underline', bg='#119975')
        self.hack_img = tk.Label(self, image=self.hack_main_img)
        def hackathon_view():
            connection = sqlite3.connect('Databases/Event_database.db')
            cursor = connection.cursor()
            #get data from database
            cursor.execute('select (select count() from Events WHERE event_type = ?) as count', ['Hackathon'])
            count = cursor.fetchall()
            count = count[0][0]
            cursor.execute('SELECT * FROM Events WHERE event_type = ?', ['Hackathon'])
            query_data = cursor.fetchall()
            def populate(newWindow):
                '''Put in some fake data'''
                for row in range(count):
                    print(query_data[row][1])
                    print(query_data[row][4])
                    print(query_data[row][3])
                    print(query_data[row][5])
                    print(query_data[row][7])

                    self.open_image = Image.open(query_data[row][1])
                    self.resized_image = ImageTk.PhotoImage(self.open_image.resize((200, 150), Image.ANTIALIAS))
                    tk.Label(newWindow, image=self.resized_image, bg='yellow', relief='solid').grid(row=row, column=0)
                    info_text = query_data[row][4]+ '\n' + query_data[row][3] + '\n' + query_data[row][5]
                    tk.Label(newWindow, text=info_text, font='Bahnschrift 24 bold', bg='yellow').grid(row=row, column=1)
                    tk.Label(newWindow, text=query_data[row][7], font='Bahnschrift 16 bold', bg='yellow').grid(row=row, column=2)

            def onFrameConfigure(canvas):
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("600x500")
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
        self.hack_btn = tk.Button(self, image=self.next_img, width=400, command=hackathon_view)
        # Top Right backdrop
        self.load_main_img2 = Image.open("images/codathon.png")
        self.code_main_img = ImageTk.PhotoImage(self.load_main_img2.resize((250, 150), Image.ANTIALIAS))
        self.backdrop_top_right = ImageTk.PhotoImage(self.load_round_rect.resize((500, 340), Image.ANTIALIAS))
        self.code_backdrop = tk.Label(self, image=self.backdrop_top_left, bg='yellow')
        self.code_label = tk.Label(self, text='Codathon', font='Bahnschrift 32 bold underline', bg='#119975')
        self.code_img = tk.Label(self, image=self.code_main_img)
        def codathon_view():
            connection = sqlite3.connect('Databases/Event_database.db')
            cursor = connection.cursor()
            #get data from database
            cursor.execute('select (select count() from Events WHERE event_type = ?) as count', ['Codathon'])
            count = cursor.fetchall()
            count = count[0][0]
            cursor.execute('SELECT * FROM Events WHERE event_type = ?', ['Codathon'])
            query_data = cursor.fetchall()
            def populate(newWindow):
                '''Put in some fake data'''
                self.picture = {}
                self.resized_image = {}
                self.open_image = {}
                for row in range(count):
                    print(query_data[row][1])
                    print(query_data[row][4])
                    print(query_data[row][3])
                    print(query_data[row][5])
                    print(query_data[row][7])

                    self.open_image[row] = Image.open(query_data[row][1])
                    self.resized_image[row] = ImageTk.PhotoImage(self.open_image[row].resize((200, 150), Image.ANTIALIAS))
                    self.picture[row] = tk.Label(newWindow, image=self.resized_image[row], bg='yellow', relief='solid').grid(row=row, column=0)
                    info_text = query_data[row][4]+ '\n' + query_data[row][3] + '\n' + query_data[row][5]
                    tk.Label(newWindow, text=info_text, font='Bahnschrift 24 bold', bg='yellow').grid(row=row, column=1)
                    tk.Label(newWindow, text=query_data[row][7], font='Bahnschrift 16 bold', bg='yellow').grid(row=row, column=2)

            def onFrameConfigure(canvas):
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("600x500")
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
        self.code_btn = tk.Button(self, image=self.next_img, width=400, command=codathon_view)
        # Bottom Left backdrop
        self.load_main_img3 = Image.open("images/bug_hunt.jpg")
        self.bug_main_img = ImageTk.PhotoImage(self.load_main_img3.resize((250, 150), Image.ANTIALIAS))
        self.backdrop_bottom_left = ImageTk.PhotoImage(self.load_round_rect.resize((500, 340), Image.ANTIALIAS))
        self.bug_backdrop = tk.Label(self, image=self.backdrop_top_left, bg='yellow')
        self.bug_label = tk.Label(self, text='Bug Hunts', font='Bahnschrift 32 bold underline', bg='#119975')
        self.bug_img = tk.Label(self, image=self.bug_main_img)
        def bug_view():
            connection = sqlite3.connect('Databases/Event_database.db')
            cursor = connection.cursor()
            #get data from database
            cursor.execute('select (select count() from Events WHERE event_type = ?) as count', ['Bug Hunt'])
            count = cursor.fetchall()
            count = count[0][0]
            cursor.execute('SELECT * FROM Events WHERE event_type = ?', ['Bug Hunt'])
            query_data = cursor.fetchall()
            def populate(newWindow):
                '''Put in some fake data'''
                for row in range(count):
                    print(query_data[row][1])
                    print(query_data[row][4])
                    print(query_data[row][3])
                    print(query_data[row][5])
                    print(query_data[row][7])

                    self.open_image = Image.open(query_data[row][1])
                    self.resized_image = ImageTk.PhotoImage(self.open_image.resize((200, 150), Image.ANTIALIAS))
                    tk.Label(newWindow, image=self.resized_image, bg='yellow', relief='solid').grid(row=row, column=0)
                    info_text = query_data[row][4]+ '\n' + query_data[row][3] + '\n' + query_data[row][5]
                    tk.Label(newWindow, text=info_text, font='Bahnschrift 24 bold', bg='yellow').grid(row=row, column=1)
                    tk.Label(newWindow, text=query_data[row][7], font='Bahnschrift 16 bold', bg='yellow').grid(row=row, column=2)

            def onFrameConfigure(canvas):
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("600x500")
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
        self.bug_btn = tk.Button(self, image=self.next_img, width=400, command=bug_view)
        # Bottom Right backdrop
        self.load_main_img4 = Image.open("images/seminars.jpg")
        self.seminar_main_img = ImageTk.PhotoImage(self.load_main_img4.resize((250, 150), Image.ANTIALIAS))
        self.backdrop_bottom_right = ImageTk.PhotoImage(self.load_round_rect.resize((500, 340), Image.ANTIALIAS))
        self.seminar_backdrop = tk.Label(self, image=self.backdrop_top_left, bg='yellow')
        self.seminar_label = tk.Label(self, text='Seminar & Events', font='Bahnschrift 32 bold underline', bg='#119975')
        self.seminar_img = tk.Label(self, image=self.seminar_main_img)
        def SnO_view():
            connection = sqlite3.connect('Databases/Event_database.db')
            cursor = connection.cursor()
            #get data from database
            cursor.execute('select (select count() from Events WHERE event_type = ?) as count', ['Seminars & Olympiads'])
            count = cursor.fetchall()
            count = count[0][0]
            cursor.execute('SELECT * FROM Events WHERE event_type = ?', ['Seminars & Olympiads'])
            query_data = cursor.fetchall()
            def populate(newWindow):
                '''Put in some fake data'''
                for row in range(count):
                    print(query_data[row][1])
                    print(query_data[row][4])
                    print(query_data[row][3])
                    print(query_data[row][5])
                    print(query_data[row][7])

                    self.open_image = Image.open(query_data[row][1])
                    self.resized_image = ImageTk.PhotoImage(self.open_image.resize((200, 150), Image.ANTIALIAS))
                    tk.Label(newWindow, image=self.resized_image, bg='yellow', relief='solid').grid(row=row, column=0)
                    info_text = query_data[row][4]+ '\n' + query_data[row][3] + '\n' + query_data[row][5]
                    tk.Label(newWindow, text=info_text, font='Bahnschrift 24 bold', bg='yellow').grid(row=row, column=1)
                    tk.Label(newWindow, text=query_data[row][7], font='Bahnschrift 16 bold', bg='yellow').grid(row=row, column=2)

            def onFrameConfigure(canvas):
                '''Reset the scroll region to encompass the inner frame'''
                canvas.configure(scrollregion=canvas.bbox("all"))

            root = tk.Toplevel()
            root.geometry("600x500")
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
        self.seminar_btn = tk.Button(self, image=self.next_img, width=400, command=SnO_view)

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
        # Top-left backdrop
        self.hack_backdrop.place(x=100, y=150)
        self.hack_label.place(x=250, y=170)
        self.hack_img.place(x=230, y=230)
        self.hack_btn.place(x=150, y=400)
        # Top-Right backdrop
        self.code_backdrop.place(x=820, y=150)
        self.code_label.place(x=980, y=170)
        self.code_img.place(x=950, y=230)
        self.code_btn.place(x=870, y=400)
        # Bottom-left backdrop
        self.bug_backdrop.place(x=100, y=550)
        self.bug_label.place(x=250, y=570)
        self.bug_img.place(x=230, y=630)
        self.bug_btn.place(x=150, y=800)
        # Bottom-Right backdrop
        self.seminar_backdrop.place(x=820, y=550)
        self.seminar_label.place(x=900, y=570)
        self.seminar_img.place(x=950, y=630)
        self.seminar_btn.place(x=870, y=800)


