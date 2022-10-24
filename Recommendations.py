import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import Contacts
import customtkinter
from PIL import ImageTk, Image
import sqlite3

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
        loadimage = Image.open("images/left_btn.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        self.event_left_btn = customtkinter.CTkButton(self, text="Prev", bg_color=accentColour, fg_color=accentColour2,
                                                      text_font=['trebuchet MS bold', 14], text_color=textColour,
                                                      image=loadimage, compound="top")

        self.event_focus = tk.PhotoImage(file="images/blank_image_icon.png")
        self.event_focus_btn = customtkinter.CTkButton(self, image=self.event_focus, bg_color=accentColour,
                                                       fg_color=accentColour2, text="")
        self.event_name_label = tk.Label(self, text="Event Name", font='Bahnschrift 30 bold', bg=accentColour, fg=textColour)

        loadimage = Image.open("images/right_btn.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        self.event_right_btn = customtkinter.CTkButton(self, text="Next", bg_color=accentColour, fg_color=accentColour2,
                                                       text_font=['trebuchet MS bold', 14], text_color=textColour,
                                                       image=loadimage, compound="top")

        self.rect_label2 = customtkinter.CTkLabel(self, bg_color=main_bg, fg_color=accentColour, height=500, width=500,
                                                 corner_radius=20, text="")
        self.title_label2 = customtkinter.CTkLabel(self, text='Recommended Users',
                                                  text_font=['trebuchet MS bold', 16], bg_color=accentColour,
                                                  fg_color=accentColour, text_color=textColour)
        self.user_label = tk.Label(self, text='Username', font='Bahnschrift 30 bold', bg=accentColour, fg=textColour)
        self.user_image = tk.PhotoImage(file="images/profile_icon.png")
        self.user_image_Button = customtkinter.CTkButton(self, image=self.user_image, bg_color=accentColour,
                                                       fg_color=accentColour2, text="")

        # Popup filter
        def popup_window():
            window = customtkinter.CTkToplevel()
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
            window.meetup_dropdown.set("Experiences")
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
                connection = sqlite3.connect("Databases/User_database.db")
                cursor = connection.cursor()
                proficiency = window.proficiencies.get()
                cursor.execute("SELECT * FROM User WHERE code_lang = ?", [proficiency])

                user_returned = cursor.fetchall()

                window.destroy()

            button_close = customtkinter.CTkButton(window, text="Submit", command=submit_filter, bg_color=main_bg,
                                                       fg_color="#0d9c8c", text_color=textColour, text_font='Bahnschrift 12 bold')
            button_close.pack(fill='x', pady=10)

        self.load_filter_img = Image.open("images/filter_icon.png")
        self.filter_img = ImageTk.PhotoImage(self.load_filter_img.resize((50, 50), Image.ANTIALIAS))
        self.filter_button = customtkinter.CTkButton(self, image=self.filter_img, command=popup_window, text="",
                                                     bg_color=accentColour, fg_color=accentColour2, width=30)
        loadimage = Image.open("images/left_btn.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        self.user_left_btn = customtkinter.CTkButton(self, text="Prev", bg_color=accentColour, fg_color=accentColour2,
                                                      text_font=['trebuchet MS bold', 14], text_color=textColour,
                                                      image=loadimage, compound="top")
        loadimage = Image.open("images/right_btn.png")
        loadimage = ImageTk.PhotoImage(loadimage.resize((50, 50), Image.ANTIALIAS))
        self.user_right_btn = customtkinter.CTkButton(self, text="Next", bg_color=accentColour, fg_color=accentColour2,
                                                       text_font=['trebuchet MS bold', 14], text_color=textColour,
                                                       image=loadimage, compound="top")
        self.user_desc_label = tk.Label(self, text='description...', bg=accentColour, fg='black')

        #arrange elements & widgets in grid
        self.recs_btn.place(x=2, y=2)
        self.search_btn.place(x=158, y=2)
        self.events_btn.place(x=300, y=2)
        self.contacts_btn.place(x=442, y=2)
        self.profile_btn.place(x=584, y=2)

        self.rect_label1.place(x=80, y=205)
        self.title_label.place(x=110, y=215)
        self.event_left_btn.place(x=100, y=620)
        self.event_name_label.place(x=330, y=400)
        self.event_focus_btn.place(x=260, y=400)
        self.event_right_btn.place(x=420, y=620)

        self.rect_label2.place(x=700, y=205)
        self.title_label2.place(x=850, y=215)
        self.user_label.place(x=1290, y=400)
        self.user_image_Button.place(x=870, y=330)
        self.filter_button.place(x=1100, y=215)
        self.user_left_btn.place(x=720, y=620)
        self.user_right_btn.place(x=1040, y=620)
        self.user_desc_label.place(x=1390, y=800)

if __name__ == "__main__":
    app = Recs_page()
    app.mainloop()

