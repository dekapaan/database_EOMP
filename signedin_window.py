from tkinter import *
from tkinter import messagebox
import datetime
import mysql.connector
import rsaidnumber


class SignedInWindow:
    def __init__(self, master):
        # window set up
        self.master = master
        self.master.geometry('600x400')

        # background image
        img = PhotoImage(file='images/background/jj-ying-7JX0-bfiuxQ-unsplash.png')
        img = img.subsample(5)
        self.lbl_img = Label(self.master, image=img)
        self.lbl_img.place(relx=0, rely=0, anchor=NW)

        # logo image
        img_logo = PhotoImage(file='images/LIFE-CHOICES-ACADEMY-LOGO-ON-BLUE-removebg-preview.png')
        img_logo = img_logo.subsample(7)
        self.lbl_logo = Label(self.master, width=600, height=50, bg='black', image=img_logo)
        self.lbl_logo.place(relx=0, rely=0, anchor=NW)

        # Sign out frame for widgets
        self.frame_sign_out = Frame(self.master, width=300, height=200, bg='white')
        self.frame_sign_out.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Heading
        self.lbl_signed_in_head = Label(self.frame_sign_out, text="Signed in", font="sans-serif 15", bg='white')
        self.lbl_signed_in_head.place(rely=0.1, relx=0.5, anchor=N)

        self.frame_sign_out_info = Frame(self.frame_sign_out, bg='white')
        self.frame_sign_out_info.place(rely=0.5, relx=0.5, anchor=CENTER)

        self.lbl_id = Label(self.frame_sign_out_info, text='ID No.', width=10, pady=2)
        self.lbl_id.grid(row=1, column=1)

        # ID entry field
        self.sign_out_id = Entry(self.frame_sign_out_info)
        self.sign_out_id.grid(row=1, column=2)

        # Sign out button
        self.btn_sign_out = Button(self.frame_sign_out, text="Sign out", bg="#00769e", fg="white", border="0",
                                   relief="solid", activebackground="#00547c", activeforeground="white", width="40",
                                   command=self.sign_out)
        self.btn_sign_out.place(rely=1, relx=0.5, anchor=S)

        self.master.mainloop()

    # Sign out function
    def sign_out(self):
        try:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                           database='lifechoices_online', auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()
            id_no = self.sign_out_id.get()

            # validity check
            rsaidnumber.parse(id_no)

            now = datetime.datetime.now()
            minute = now.minute
            hour = now.hour
            if minute <= 9:
                minute = '0' + str(minute)
            if hour <= 9:
                hour = '0' + str(hour)
            time = "{}:{}".format(hour, minute)
            query = "update register set time_out='{}' where ID='{}' and time_out='--:--'".format(time, id_no)
            mycursor.execute(query)
            mydb.commit()
            self.master.destroy()

            # back to sign in/ register window
            import main

        except ValueError:
            messagebox.showerror(message='Invalid ID')


# instantiation
root = Tk()
app = SignedInWindow(root)
