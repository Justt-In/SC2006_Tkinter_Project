import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image

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
                                  command=lambda: controller.show_frame("Recs_page"))

        def goto_search():
            controller.show_frame('Search_page')

        self.load_search_image = tk.PhotoImage(file="images/search_icon.png")
        self.search_btn = tk.Button(self, image=self.load_search_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=lambda: controller.show_frame("Search_page"))

        def goto_events():
            controller.show_frame('Events_page')

        self.load_events_image = tk.PhotoImage(file="images/events_icon.png")
        self.events_btn = tk.Button(self, image=self.load_events_image, bg="orange", bd="3", height=130,
                                    relief="raised", command=lambda: controller.show_frame("Events_page"))

        def goto_contacts():
            controller.show_frame('Contacts_page')

        self.load_contacts_image = tk.PhotoImage(file="images/contacts_icon.png")
        self.contacts_btn = tk.Button(self, image=self.load_contacts_image, bg="orange", bd="3", height=130,
                                      relief="raised", command=lambda: controller.show_frame("Contacts_page"))

        def goto_profile():
            controller.show_frame('Profile_page')

        self.load_profile_image = tk.PhotoImage(file="images/profile_icon.png")
        self.profile_btn = tk.Button(self, image=self.load_profile_image, bg="orange", bd="3", height=130,
                                     relief="raised", command=lambda: controller.show_frame("Profile_page"))
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