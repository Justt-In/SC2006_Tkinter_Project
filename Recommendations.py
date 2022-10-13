import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import Contacts
from PIL import ImageTk, Image
import sqlite3



class Recs_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#2176FF')
        self.controller = controller
        #Toolbar
        #Top Toolbar
        self.space_label1 = tk.Label(self, width=1000, height=9, bg="#FDCA40", borderwidth=2, relief='solid')
        def goto_recs():
            controller.show_frame('Recs_page')
        self.load_recs_image = tk.PhotoImage(file="images/recs_icon.png")
        self.recs_btn = tk.Button(self, image=self.load_recs_image, bg="#FDCA40", bd="3", height=130, relief="raised", command=lambda: controller.show_frame("Recs_page"))
        def goto_search():
            controller.show_frame('Search_page')
        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="#FDCA40", bd="3", height=130, relief="raised", command=lambda: controller.show_frame("Search_page"))
        def goto_events():
            controller.show_frame('Events_page')
        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="#FDCA40", bd="3", height=130, relief="raised", command=lambda: controller.show_frame("Events_page"))
        def goto_contacts():
            controller.show_frame('Contacts_page')
        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="#FDCA40", bd="3", height=130, relief="raised", command=lambda: controller.show_frame("Contacts_page"))
        def goto_profile():
            controller.show_frame('Profile_page')
        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="#FDCA40", bd="3", height=130, relief="raised", command=lambda: controller.show_frame("Profile_page"))
        self.load_logout_img = Image.open("images/logout_icon.png")
        self.logout_img = ImageTk.PhotoImage(self.load_logout_img.resize((128, 128), Image.ANTIALIAS))
        self.logout_btn = tk.Button(self, image=self.logout_img, bg="#FDCA40", bd="3", relief="raised", command=lambda: controller.show_frame("Login"))
        #End of Toolbar

        #create elements/widgets
        self.space_label1_1 = tk.Label(self, height=8, width=50, bg='black')
        self.space_label2 = tk.Label(self, height=1, bg='black')
        #self.space_label3 = tk.Label(self, height=1, bg='black')
        self.line_label1 = tk.Label(self,  width=1000, bg='#33A1FD')
        self.title_label = tk.Label(self, text='Upcoming Events You May Be Interested', font='Impact 16 underline', background='#33A1FD')
        self.user_label = tk.Label(self, text='Username', font='Impact 16 underline', background='#33A1FD')

        image = Image.open("images/round_rect.png")
        photo = ImageTk.PhotoImage(image.resize((710, 300), Image.ANTIALIAS))
        self.rect_label = tk.Label(self, image=photo, bg='#33A1FD', fg='black', relief='solid')



        self.event_left = tk.PhotoImage(file="images/img_login_left.png")
        self.event_left_btn = tk.Button(self, image=self.event_left, bg="white", bd="3", relief="raised")
        self.event_right = tk.PhotoImage(file="images/img_login.png")
        self.event_right_btn = tk.Button(self, image=self.event_right, bg="white", bd="3", relief="raised")

        self.event_focus = tk.PhotoImage(file="images/blank_image_icon.png")
        self.event_focus_btn = tk.Button(self, image=self.event_focus)

        '''
        connection = sqlite3.connect("Databases/Event_database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Events")
        profilepic1 = cursor.fetchall()[0][1]
        load_profile_pic = Image.open(profilepic1)
        default_pic = ImageTk.PhotoImage(load_profile_pic.resize((130, 130), Image.ANTIALIAS))
        self.event_focus_btn.configure(image=default_pic)
        '''
        image1 = Image.open("images/round_rect.png")
        photo1 = ImageTk.PhotoImage(image1.resize((710, 300), Image.ANTIALIAS))
        self.rect_label_2 = tk.Label(self, image=photo1, bg='#33A1FD', fg='black', relief='solid')
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
                connection = sqlite3.connect("Databases/User_database.db")
                cursor = connection.cursor()
                proficiency = window.proficient
                cursor.execute("SELECT * FROM User WHERE code_lang = ?", [proficiency])

                user_returned = cursor.fetchall()

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

        self.user_desc_label = tk.Label(self, text='description...', bg='#33A1FD', fg='black')

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
        self.logout_btn.place(x=100, y=3)
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

if __name__ == "__main__":
    app = Recs_page()
    app.mainloop()

