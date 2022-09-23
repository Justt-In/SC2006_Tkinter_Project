import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image

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

