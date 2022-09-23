import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image

class Register_confirmation_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='purple')
        self.controller = controller

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
        self.submit_button = tk.Button(self, text='Submit', font='Bahnschrift 25 bold', bg='#2860ed', relief='raised', width=20, command=lambda: controller.show_frame("Recs_page"))

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