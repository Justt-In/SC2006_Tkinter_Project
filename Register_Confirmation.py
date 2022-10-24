import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import sqlite3

class Register_confirmation_page(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        if customtkinter.get_appearance_mode() == "light" or customtkinter.get_appearance_mode() == "Light":
            main_bg = "#ffe5d9"
            accentColour = "#48CAE4"
            accentColour2 = "#E46248"
            textColour = "black"
        else:
            main_bg = "#464646"
            accentColour = "#0077b6"
            accentColour2 = "#B63F00"
            textColour = "black"
        customtkinter.CTkFrame.__init__(self, parent, fg_color=main_bg)
        self.controller = controller
        #Create elements & widgets
        self.space_label1 = customtkinter.CTkLabel(self, height=100, width=1280, bg_color=accentColour,
                                                   text="Let's Setup Your Profile",
                                                   text_color=textColour, text_font=['trebuchet MS bold', 42])
        self.load_title_img = tk.PhotoImage(file="images/profile_icon.png")
        self.title_img_label1 = tk.Label(self, image=self.load_title_img, bg=accentColour)
        self.title_img_label2 = tk.Label(self, image=self.load_title_img, bg=accentColour)
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

        self.label_block = tk.Label(self, bg=main_bg, width=500, height=500)
        self.edit_btn = customtkinter.CTkButton(self, text='Click To Start Editing', text_font=['trebuchet MS bold', 30],
                                                bg_color=main_bg, text_color=textColour, fg_color='#0d9c8c',
                                                width=50, command=open_connection)

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

        self.load_profile_img = tk.PhotoImage(file="images/default_profile_img.png")
        self.profile_img_label = tk.Label(self, image=self.load_profile_img, bg=main_bg)
        self.load_upload_img = (Image.open("images/upload_img.png"))
        self.resized_image = self.load_upload_img.resize((30, 30), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.upload_img_button = customtkinter.CTkButton(self, text="Upload Image",image=self.new_image, text_color=textColour,
                                                         command=uploadImage, width=100, bg_color=main_bg,
                                                         fg_color=accentColour, text_font=['trebuchet MS bold', 20])
        self.username_label = tk.Label(self, font='roboto 30 bold', bg=main_bg, fg=textColour, text='Text Username')
        self.title_label2 = customtkinter.CTkLabel(self, text="Who would you like to see on your recommended?",
                                                   text_font=['trebuchet MS bold', 16], bg_color=main_bg, text_color=textColour)
        self.load_backdrop1_img = Image.open("images/backdrop_v2_1.png")
        self.backdrop1 = ImageTk.PhotoImage(self.load_backdrop1_img.resize((450, 600), Image.ANTIALIAS))
        self.backdrop1_label = tk.Label(self, image=self.backdrop1, bg='#2176FF')
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

        self.experience1 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience1.set("Experience")
        self.experience1.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)
        self.switch1 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var1, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel1 = customtkinter.CTkLabel(self, text='Python', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience2 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience2.set("Experience")
        self.experience2.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch2 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var2, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel2 = customtkinter.CTkLabel(self, text='C++', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience3 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience3.set("Experience")
        self.experience3.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch3 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var3, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel3 = customtkinter.CTkLabel(self, text='C#', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience4 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience4.set("Experience")
        self.experience4.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch4 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var4, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel4 = customtkinter.CTkLabel(self, text='C', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience5 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience5.set("Experience")
        self.experience5.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch5 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var5, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel5 = customtkinter.CTkLabel(self, text='Java', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience6 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience6.set("Experience")
        self.experience6.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch6 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var6, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel6 = customtkinter.CTkLabel(self, text='Javascript', text_font='Bahnschrift 12 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience7 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience7.set("Experience")
        self.experience7.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch7 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var7, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel7 = customtkinter.CTkLabel(self, text='PHP', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience8 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience8.set("Experience")
        self.experience8.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch8 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var8, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel8 = customtkinter.CTkLabel(self, text='SQL', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience9 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience9.set("Experience")
        self.experience9.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                   text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                   dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                   width=100)

        self.switch9 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var9, fg_color='red',
                                               progress_color='#2BD447')
        self.switchLabel9 = customtkinter.CTkLabel(self, text='HTML', text_font='Bahnschrift 14 bold',
                                                   bg_color=main_bg, text_color=textColour)
        self.experience10 = customtkinter.CTkOptionMenu(self, values=["<1Y", "1Y", "2Y", "3Y", ">3Y"])
        self.experience10.set("Experience")
        self.experience10.configure(text_font='Bahnschrift 12 bold', bg_color=main_bg, fg_color=accentColour2,
                                    text_color=textColour, button_color=accentColour2, dropdown_color=accentColour,
                                    dropdown_text_color=textColour, dropdown_text_font='Bahnschrift 12 bold',
                                    width=100)

        self.switch10 = customtkinter.CTkSwitch(self, bg_color=main_bg, text='', variable=var10, fg_color='red',
                                                progress_color='#2BD447')
        self.switchLabel10 = customtkinter.CTkLabel(self, text='CSS', text_font='Bahnschrift 14 bold',
                                                    bg_color=main_bg, text_color=textColour)

        self.title_label3 = customtkinter.CTkLabel(self, text='Short Description of Yourself:', bg_color=main_bg,
                                                   text_font='Bahnschrift 25 bold', text_color=textColour)
        self.check_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=35, height=3, font='Bahnschrift 16 bold')

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

        submit_img = Image.open("images/submit_icon.png")
        submit_img = ImageTk.PhotoImage(submit_img.resize((75, 75), Image.ANTIALIAS))
        self.submit_button = customtkinter.CTkButton(self, text='Create Account', text_font='Bahnschrift 42 bold', text_color=textColour,
                                                     bg_color=main_bg, fg_color="#0d9c8c", width=20, command=goto_recs_page
                                                     ,image=submit_img, height=100)

        #Place elements & widgets
        self.space_label1.place(x=0, y=0)
        self.title_img_label1.place(x=350, y=5)
        self.title_img_label2.place(x=1430, y=5)
        self.edit_btn.place(x=430, y=120)
        self.profile_img_label.place(x=460, y=330)
        self.upload_img_button.place(x=285, y=400)
        self.username_label.place(x=1050, y=320)
        self.title_label2.place(x=590, y=270)

        self.experience1.place(x=850, y=310)
        self.experience1.tkraise()
        self.switchLabel1.place(x=730, y=310)
        self.switch1.place(x=710, y=315)
        self.switch1.tkraise()
        self.experience2.place(x=850, y=350)
        self.experience2.tkraise()
        self.switchLabel2.place(x=730, y=350)
        self.switch2.place(x=710, y=355)
        self.switch2.tkraise()
        self.experience3.place(x=850, y=390)
        self.experience3.tkraise()
        self.switchLabel3.place(x=735, y=390)
        self.switch3.place(x=710, y=395)
        self.switch3.tkraise()
        self.experience4.place(x=850, y=430)
        self.experience4.tkraise()
        self.switchLabel4.place(x=730, y=430)
        self.switch4.place(x=710, y=435)
        self.switch4.tkraise()
        self.experience5.place(x=850, y=470)
        self.experience5.tkraise()
        self.switchLabel5.place(x=730, y=470)
        self.switch5.place(x=710, y=475)
        self.switch5.tkraise()
        self.experience6.place(x=850, y=510)
        self.experience6.tkraise()
        self.switchLabel6.place(x=730, y=510)
        self.switch6.place(x=710, y=515)
        self.switch6.tkraise()
        self.experience7.place(x=850, y=550)
        self.experience7.tkraise()
        self.switchLabel7.place(x=730, y=550)
        self.switch7.place(x=710, y=555)
        self.switch7.tkraise()
        self.experience8.place(x=850, y=590)
        self.experience8.tkraise()
        self.switchLabel8.place(x=730, y=590)
        self.switch8.place(x=710, y=595)
        self.switch8.tkraise()
        self.experience9.place(x=850, y=630)
        self.experience9.tkraise()
        self.switchLabel9.place(x=730, y=630)
        self.switch9.place(x=710, y=635)
        self.switch9.tkraise()
        self.experience10.place(x=850, y=670)
        self.experience10.tkraise()
        self.switchLabel10.place(x=730, y=670)
        self.switch10.place(x=710, y=675)
        self.switch10.tkraise()
        self.title_label3.place(x=180, y=450)
        self.check_area.place(x=270, y=740)
        self.submit_button.place(x=170, y=590)
        self.label_block.place(x=0,y=300)
        self.label_block.tkraise()