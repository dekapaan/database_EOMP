import mysql.connector
from tkinter import *
from tkinter import PhotoImage

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='lifechoices_online', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()


class HomeScreen:
    def __init__(self, master):
        # window setup
        self.master = master
        self.master.title("Lifechoices Online")
        self.master.geometry("800x600")

        # label for bg image
        image_bg = PhotoImage(file='images/background/george-pagan-iii-WwCTFNpZx8g-unsplash.png')
        image_bg = image_bg.subsample(5)
        self.lbl_bg = Label(self.master, image=image_bg)
        self.lbl_bg.place(x=-10, y=-10)

        # lifechoices logo
        image_logo = PhotoImage(file='images/LIFE-CHOICES-ACADEMY-LOGO-ON-BLUE-removebg-preview.png')
        image_logo = image_logo.subsample(2)
        self.lbl_logo = Label(self.master, image=image_logo, bg="black", width="600", height="150")
        self.lbl_logo.place(x=98, y=50)

        # sign-in/sign-up frame
        self.frame_log = Frame(self.master, width="602", height="350", bg="white")
        self.frame_log.place(x=98, y=200)

        self.frame_left = Frame(self.frame_log, width="300", height="350", bg="#00769e")
        self.frame_left.place(x=0, y=0)
        image_welcome = PhotoImage(file="images/NicePng_welcome-sign-png_2216066.png")
        image_welcome = image_welcome.subsample(2)
        self.lbl_welcome = Label(self.frame_left, image=image_welcome, bg="#00769e")
        self.lbl_welcome.place(x=30, y=30)

        self.master.mainloop()


root = Tk()
HomeScreen(root)
