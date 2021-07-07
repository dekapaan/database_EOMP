from tkinter import *
from tkinter import messagebox
import datetime
import mysql.connector
import rsaidnumber


class SignedInWindow:
    def __init__(self, master):
        self.master = master
        self.btn_sign_out = Button(self.master, text="Sign out", command=self.sign_out)
        self.sign_out_id = Entry(self.master)
        self.sign_out_id.pack()
        self.btn_sign_out.pack()

    def sign_out(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        id_no = self.sign_out_id.get()
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


root = Tk()
app = SignedInWindow(root)
root.mainloop()
