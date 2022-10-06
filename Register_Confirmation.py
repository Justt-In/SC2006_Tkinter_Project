import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
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
            if filename == '' or filename == ' ':
                filename = None
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
        self.title_label2 = tk.Label(self, text="Who would you like to see on your recommended?", font='Bahnschrift 20 bold', bg='purple')
        self.load_backdrop1_img = Image.open("images/backdrop1_v.png")
        self.backdrop1 = ImageTk.PhotoImage(self.load_backdrop1_img.resize((450, 600), Image.ANTIALIAS))
        self.backdrop1_label = tk.Label(self, image=self.backdrop1, bg='#5cc9ed')
        var1 = tk.IntVar(self)
        var2 = tk.IntVar(self)
        var3 = tk.IntVar(self)
        var4 = tk.IntVar(self)
        var5 = tk.IntVar(self)
        var6 = tk.IntVar(self)
        var7 = tk.IntVar(self)
        var8 = tk.IntVar(self)
        var9 = tk.IntVar(self)
        var10 = tk.IntVar(self)
        self.proficient1 = tk.StringVar(self)
        self.proficient1.set("Experience")  # default value
        self.proficient2 = tk.StringVar(self)
        self.proficient2.set("Experience")
        self.proficient3 = tk.StringVar(self)
        self.proficient3.set("Experience")
        self.proficient4 = tk.StringVar(self)
        self.proficient4.set("Experience")
        self.proficient5 = tk.StringVar(self)
        self.proficient5.set("Experience")
        self.proficient6 = tk.StringVar(self)
        self.proficient6.set("Experience")
        self.proficient7 = tk.StringVar(self)
        self.proficient7.set("Experience")
        self.proficient8 = tk.StringVar(self)
        self.proficient8.set("Experience")
        self.proficient9 = tk.StringVar(self)
        self.proficient9.set("Experience")
        self.proficient10 = tk.StringVar(self)
        self.proficient10.set("Experience")

        self.experience1 = tk.OptionMenu(self, self.proficient1, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience1.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience1_menu = self.nametowidget(self.experience1.menuname)
        experience1_menu.configure(font='Bahnschrift 12 bold')
        self.check1 = tk.Checkbutton(self, text='Python', font='Bahnschrift 16 bold', bg='purple', bd=-2,
                                     variable=var1)
        self.experience2 = tk.OptionMenu(self, self.proficient2, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience2.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience2_menu = self.nametowidget(self.experience2.menuname)
        experience2_menu.configure(font='Bahnschrift 12 bold')
        self.check2 = tk.Checkbutton(self, text='C++', font='Bahnschrift 16 bold', bg='purple', bd=-2, variable=var2)
        self.experience3 = tk.OptionMenu(self, self.proficient3, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience3.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience3_menu = self.nametowidget(self.experience3.menuname)
        experience3_menu.configure(font='Bahnschrift 12 bold')
        self.check3 = tk.Checkbutton(self, text='C#', font='Bahnschrift 16 bold', bg='purple', bd=-2, variable=var3)
        self.experience4 = tk.OptionMenu(self, self.proficient4, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience4.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience4_menu = self.nametowidget(self.experience4.menuname)
        experience4_menu.configure(font='Bahnschrift 12 bold')
        self.check4 = tk.Checkbutton(self, text='C', font='Bahnschrift 16 bold', bg='purple', bd=-2, variable=var4)
        self.experience5 = tk.OptionMenu(self, self.proficient5, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience5.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience5_menu = self.nametowidget(self.experience5.menuname)
        experience5_menu.configure(font='Bahnschrift 12 bold')
        self.check5 = tk.Checkbutton(self, text='Java', font='Bahnschrift 16 bold', bg='purple', bd=-2, variable=var5)
        self.experience6 = tk.OptionMenu(self, self.proficient6, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience6.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience6_menu = self.nametowidget(self.experience6.menuname)
        experience6_menu.configure(font='Bahnschrift 12 bold')
        self.check6 = tk.Checkbutton(self, text='Javascript', font='Bahnschrift 16 bold', bg='purple', bd=-2,
                                     variable=var6)
        self.experience7 = tk.OptionMenu(self, self.proficient7, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience7.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience7_menu = self.nametowidget(self.experience7.menuname)
        experience7_menu.configure(font='Bahnschrift 12 bold')
        self.check7 = tk.Checkbutton(self, text='PHP', font='Bahnschrift 16 bold', bg='purple', bd=-2, variable=var7)
        self.experience8 = tk.OptionMenu(self, self.proficient8, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience8.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience8_menu = self.nametowidget(self.experience8.menuname)
        experience8_menu.configure(font='Bahnschrift 12 bold')
        self.check8 = tk.Checkbutton(self, text='SQL', font='Bahnschrift 16 bold', bg='purple', bd=-2, variable=var8)
        self.experience9 = tk.OptionMenu(self, self.proficient9, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience9.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience9_menu = self.nametowidget(self.experience9.menuname)
        experience9_menu.configure(font='Bahnschrift 12 bold')
        self.check9 = tk.Checkbutton(self, text='HTML', font='Bahnschrift 16 bold', bg='purple', bd=-2, variable=var9)
        self.experience10 = tk.OptionMenu(self, self.proficient10, "<1Y", "1Y", "2Y", "3Y", ">3Y")
        self.experience10.configure(font='Bahnschrift 12 bold', bg='#4c5270', fg='white', bd=-2)
        experience10_menu = self.nametowidget(self.experience10.menuname)
        experience10_menu.configure(font='Bahnschrift 12 bold')
        self.check10 = tk.Checkbutton(self, text='CSS', font='Bahnschrift 16 bold', bg='purple', bd=-2, variable=var10)

        self.check_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=35, height=3, font='Bahnschrift 16 bold')
        self.title_label3 = tk.Label(self, text='Short Description of Yourself:', font='Bahnschrift 25 bold', bg='purple')

        def goto_recs_page():
            msgBox = tk.messagebox.askyesno("Confirmation","Your user preference cannot be changed After submission. "
                                                           "Are you sure with your choices?")
            if msgBox == 'No':
                return
            connection = sqlite3.connect('Databases/User_database.db')
            cursor = connection.cursor()
            sql = 'SELECT username FROM User ORDER BY creation_date DESC LIMIT 1;'
            cursor.execute(sql)
            username = cursor.fetchall()[0][0]
            connection.close()
            sql = 'Databases/' + username + '_db.db'
            connection = sqlite3.connect(sql)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Personal(userid INTEGER PRIMARY KEY AUTOINCREMENT, invite_received TEXT, invite_sent TEXT, proggies TEXT, chat_logs TEXT)''')
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
            count = 0
            coding_prof = ''
            if var1.get() == 1:
                python = self.proficient1.get()
                if python == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Python ' + python
            if var2.get() == 1:
                c_plus = self.proficient2.get()
                if c_plus == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C++ ' + c_plus
            if var3.get() == 1:
                c_sharp = self.proficient3.get()
                if c_sharp == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C# ' + c_sharp
            if var4.get() == 1:
                c_only = self.proficient4.get()
                if c_only == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', C ' + c_only
            if var5.get() == 1:
                java = self.proficient5.get()
                if java == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Java ' + java
            if var6.get() == 1:
                javascript = self.proficient6.get()
                if javascript == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', Javascript ' + javascript
            if var7.get() == 1:
                php = self.proficient7.get()
                if php == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', PHP ' + php
            if var8.get() == 1:
                s_q_l = self.proficient8.get()
                if s_q_l == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', SQL ' + s_q_l
            if var9.get() == 1:
                html = self.proficient9.get()
                if html == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', HTML ' + html
            if var10.get() == 1:
                css = self.proficient10.get()
                if css == 'Experience':
                    count += 1
                else:
                    coding_prof = coding_prof + ', CSS ' + css
            cursor.execute("UPDATE User SET user_preference = ? WHERE userid = ?", [coding_prof, num])
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

        self.experience1.place(x=970, y=375)#x-330, y+140
        self.check1.place(x=810, y=370)
        self.experience2.place(x=970, y=405)
        self.check2.place(x=810, y=400)
        self.experience3.place(x=970, y=435)
        self.check3.place(x=810, y=430)
        self.experience4.place(x=970, y=465)
        self.check4.place(x=810, y=460)
        self.experience5.place(x=970, y=495)
        self.check5.place(x=810, y=490)
        self.experience6.place(x=970, y=525)
        self.check6.place(x=810, y=520)
        self.experience7.place(x=970, y=555)
        self.check7.place(x=810, y=550)
        self.experience8.place(x=970, y=585)
        self.check8.place(x=810, y=580)
        self.experience9.place(x=970, y=615)
        self.check9.place(x=810, y=610)
        self.experience10.place(x=970, y=645)
        self.check10.place(x=810, y=645)

        self.title_label3.place(x=210, y=575)
        self.check_area.place(x=210, y=625)
        self.submit_button.place(x=500, y=780)
        self.label_block.place(x=50, y=220)
        self.label_block.tkraise()

        #User preference for recommendation