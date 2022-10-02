import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import sqlite3

class Register_confirmation_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='purple')
        self.controller = controller
        #Create elements & widgets
        self.space_label1 = tk.Label(self, width=1000, height=9, bg="#ff8c1a", borderwidth=2, relief='solid')
        self.load_title_img = tk.PhotoImage(file="images/profile_icon.png")
        self.page_label = tk.Label(self, text="Let's Setup Your Profile", font='Bahnschrift 60 bold', bg="#ff8c1a")
        self.title_img_label1 = tk.Label(self, image=self.load_title_img, bg="#ff8c1a")
        self.title_img_label2 = tk.Label(self, image=self.load_title_img, bg="#ff8c1a")
        def open_connection():
            global username
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            data = cursor.execute('SELECT * FROM User')
            for row in data:
                print(row)
            sql = 'SELECT username FROM User ORDER BY creation_date DESC LIMIT 1;'
            cursor.execute(sql)
            username = cursor.fetchall()
            self.username_label['text'] = username
            self.label_block.lower()

        self.label_block = tk.Label(self, bg='purple', width=500, height=500)
        self.edit_btn = tk.Button(self, text='Click To Start Editing', font='Bahnschrift 20 bold', bg='Grey', relief='solid', width=50, command=open_connection)

        def uploadImage():
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            sql = 'SELECT userid FROM User ORDER BY creation_date DESC LIMIT 1;'
            cursor.execute(sql)
            userid = str(cursor.fetchall())
            num = ''
            for char in userid:
                if char.isdigit():
                    num += char
            filename = filedialog.askopenfilename(initialdir="C:\\", filetypes=(("PNG file", "*.png"), ("JPEG File", "*.jpeg"), ("JPG File", "*.jpg"), ("All File Types", "*.*")))
            cursor.execute("UPDATE User SET profile_pic = ? WHERE userid = ?", [filename, num])
            connection.commit()
            connection.close()
            stgImg = ImageTk.PhotoImage(file=filename)
            self.profile_img_label.configure(image=stgImg)
            self.profile_img_label.image = stgImg

        photo = tk.PhotoImage(file="images/default_profile_img.png")
        self.load_profile_img = tk.PhotoImage(file="images/default_profile_img.png")
        self.profile_img_label = tk.Label(self, image=self.load_profile_img, bg='purple')
        self.load_upload_img = (Image.open("images/upload_img.png"))
        self.resized_image = self.load_upload_img.resize((30, 30), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.upload_img_button = tk.Button(self,text="Upload Image",image=self.new_image, command=uploadImage, width=100, relief='raised', bg='#2860ed')
        self.username_label = tk.Label(self,text='Test Username', font='Bahnschrift 40 underline', bg='purple')
        self.title_label2 = tk.Label(self, text="What Events Are You Interested In?", font='Bahnschrift 30 bold', bg='purple')
        var1 = tk.IntVar(self)
        var2 = tk.IntVar(self)
        var3 = tk.IntVar(self)
        var4 = tk.IntVar(self)
        var5 = tk.IntVar(self)
        self.check1 = tk.Checkbutton(self, text='Hackathons', font='Bahnschrift 25 bold', bg='purple', bd=-2, variable=var1)
        self.check2 = tk.Checkbutton(self, text='Codathons', font='Bahnschrift 25 bold', bg='purple', bd=-2, variable=var2)
        self.check3 = tk.Checkbutton(self, text='Bug Hunts', font='Bahnschrift 25 bold', bg='purple', bd=-2, variable=var3)
        self.check4 = tk.Checkbutton(self, text='Seminars & Exhibitions', font='Bahnschrift 25 bold', bg='purple', bd=-2, variable=var4)
        self.check5 = tk.Checkbutton(self, text='Olympiads', font='Bahnschrift 25 bold', bg='purple', bd=-2, variable=var5)
        self.check_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=35, height=3, font='Bahnschrift 16 bold')
        self.title_label3 = tk.Label(self, text='Short Description of Yourself:', font='Bahnschrift 25 bold', bg='purple')

        def goto_recs_page():
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            sql = 'SELECT username FROM User ORDER BY creation_date DESC LIMIT 1;'
            cursor.execute(sql)
            username = cursor.fetchall()[0][0]
            connection.close()
            sql = 'Databases/' + username + '_db.db'
            connection = sqlite3.connect(sql)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Personal(userid INTEGER PRIMARY KEY AUTOINCREMENT, invite_received TEXT, invite_sent TEXT, proggies TEXT, chat_log TEXT)''')
            connection.commit()
            connection.close()
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            sql = 'SELECT userid FROM User ORDER BY creation_date DESC LIMIT 1;'
            cursor.execute(sql)
            userid = str(cursor.fetchall())
            num = ''
            for char in userid:
                if char.isdigit():
                    num += char
            print(num)
            interests = ''
            if var1.get() == 1:
                interests = interests + ', Hackathons'
            if var2.get() == 1:
                interests = interests + ', Codathons'
            if var3.get() == 1:
                interests = interests + ', Bug Hunts'
            if var4.get() == 1:
                interests = interests + ', Seminars & Exhibitions'
            if var5.get() == 1:
                interests = interests + ', Olympiads'
            print(interests)
            cursor.execute("UPDATE User SET events = ? WHERE userid = ?", [interests, num])
            connection.commit()
            shortDesc = self.check_area.get("1.0","end-1c")
            print(shortDesc)
            cursor.execute("UPDATE User SET short_Desc = ? WHERE userid = ?", [shortDesc, num])
            #cursor.execute(sql)
            connection.commit()
            connection.close()
            controller.show_frame('Login')
        self.submit_button = tk.Button(self, text='Submit', font='Bahnschrift 25 bold', bg='#2860ed', relief='raised', width=20, command=goto_recs_page)

        #Place elements & widgets
        self.space_label1.place(x=0, y=0)
        self.title_img_label1.place(x=150, y=5)
        self.page_label.place(x=300, y=10)
        self.title_img_label2.place(x=1150, y=5)
        self.profile_img_label.place(x=300, y=250)
        self.upload_img_button.place(x=377, y=525)
        self.username_label.place(x=700, y=250)
        self.title_label2.place(x=670, y=320)
        self.edit_btn.place(x=360, y=150)
        self.check1.place(x=700, y=380)
        self.check2.place(x=700, y=430)
        self.check3.place(x=700, y=480)
        self.check4.place(x=700, y=530)
        self.check5.place(x=700, y=580)
        self.title_label3.place(x=700, y=635)
        self.check_area.place(x=700, y=685)
        self.submit_button.place(x=500, y=780)
        self.label_block.place(x=50, y=220)
        self.label_block.tkraise()