from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
import mysql.connector
import rsaidnumber


class AdminGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin")
        self.master.geometry('1000x1000')
        self.master.config(bg="white")

        self.frame_options = Frame(self.master, bg='white', width=600, height=400)
        self.frame_options.place(rely=0.5, relx=0.5, anchor=CENTER)
        self.btn_modify_screen = Button(self.frame_options, text="Modify / Add / Remove", bg="#00769e", fg="white", border="0",
                                        relief="solid", activebackground="#00547c", activeforeground="white", width="30"
                                        )

        self.btn_modify_screen.place(rely=0.45, relx=0.5, anchor=CENTER)

        self.btn_view_register = Button(self.frame_options, text="View register", bg="#00769e", fg="white", border="0",
                                        relief="solid", activebackground="#00547c", activeforeground="white", width="30"
                                        )

        self.btn_view_register.place(rely=0.55, relx=0.5, anchor=CENTER)

        self.frame_modify = Frame(self.master, bg='grey')
        self.frame_modify.place(rely=0.5, relx=0.5, anchor=CENTER)

        self.tree_modify = ttk.Treeview(self.frame_modify)
        self.tree_modify['columns'] = ('ID No.', 'Name', 'Surname', 'Phone No.')

        self.tree_modify.column('ID No.')
        self.tree_modify.column('Name')
        self.tree_modify.column('Surname')
        self.tree_modify.column('Phone No.')

        self.tree_modify['show'] = 'headings'
        self.tree_modify.heading('ID No.', text='ID no.')
        self.tree_modify.heading('Name', text='Name')
        self.tree_modify.heading('Surname', text='Surname')
        self.tree_modify.heading('Phone No.', text='Phone no.')

        self.pop_treeview()
        self.tree_modify.pack()

        self.entry_frame = Frame(self.frame_modify, width=50)
        self.entry_frame.pack()

        self.lbl_ID = Label(self.entry_frame, text="ID No.")
        self.lbl_ID.pack()

        self.entry_ID = Entry(self.entry_frame)
        self.entry_ID.pack()

        self.lbl_name = Label(self.entry_frame, text="Name")
        self.lbl_name.pack()

        self.entry_name = Entry(self.entry_frame)
        self.entry_name.pack()

        self.lbl_surname = Label(self.entry_frame, text="Surname")
        self.lbl_surname.pack()

        self.entry_surname = Entry(self.entry_frame)
        self.entry_surname.pack()

        self.lbl_phone = Label(self.entry_frame, text="Phone No.")
        self.lbl_phone.pack()

        self.entry_phone = Entry(self.entry_frame)
        self.entry_phone.pack()

        self.lbl_kin = Label(self.entry_frame, text="Next of kin")
        self.lbl_kin.pack()

        self.lbl_kin_name = Label(self.entry_frame, text='Name')
        self.lbl_kin_name.pack()

        self.entry_kin_name = Entry(self.entry_frame)
        self.entry_kin_name.pack()

        self.lbl_kin_phone = Label(self.entry_frame, text="Phone No.")
        self.lbl_kin_phone.pack()

        self.entry_kin_phone = Entry(self.entry_frame)
        self.entry_kin_phone.pack()

        self.tree_modify.bind('<ButtonRelease-1>', self.send_data)

        self.btn_update = Button(self.frame_modify, text="Update user", bg="#00769e", fg="white", border="0",
                                 relief="solid", activebackground="#00547c", activeforeground="white", width="30",
                                 command=self.update)
        self.btn_update.pack()

        self.btn_add = Button(self.frame_modify, text="Add user", bg="#00769e", fg="white", border="0", relief="solid",
                              activebackground="#00547c", activeforeground="white", width="30", command=self.add)
        self.btn_add.pack()

        self.btn_delete = Button(self.frame_modify, text="Delete user", bg="#00769e", fg="white", border="0",
                                 relief="solid", activebackground="#00547c", activeforeground="white", width="30",
                                 command=self.remove)
        self.btn_delete.pack()

        self.current_id = ''

    def pop_treeview(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        query = "select * from Users"
        mycursor.execute(query)
        info = mycursor.fetchall()

        self.tree_modify.delete(*self.tree_modify.get_children())
        for user in info:
            self.tree_modify.insert(parent='', index='end', text='', values=user)

    def send_data(self, event=None):
        current_item = self.tree_modify.focus()
        info = self.tree_modify.item(current_item)
        info = info['values']

        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        mycursor.execute('select * from Users')
        info1 = mycursor.fetchall()
        self.entry_ID.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_surname.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_kin_name.delete(0, END)
        self.entry_kin_phone.delete(0, END)
        for user in info1:
            if info[1] in user:
                self.entry_ID.insert(0, user[0])
                self.current_id = user[0]
                self.entry_phone.insert(0, user[3])

        self.entry_name.insert(0, info[1])
        self.entry_surname.insert(0, info[2])

        mycursor.execute("select * from next_of_kin where ID='{}'".format(self.entry_ID.get()))
        info_nex_of_kin = mycursor.fetchall()
        print(info_nex_of_kin)
        self.entry_kin_name.insert(0, info_nex_of_kin[0][1])
        self.entry_kin_phone.insert(0, info_nex_of_kin[0][2])

    def update(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        query = "update Users set ID='{}', name='{}', surname='{}', phone='{}' " \
                "where ID='{}'".format(self.entry_ID.get(), self.entry_name.get(), self.entry_surname.get(),
                                       self.entry_phone.get(), self.current_id)
        mycursor.execute(query)
        mydb.commit()
        messagebox.showinfo(message='Update successful')
        self.pop_treeview()

    def add(self):
        try:
            id_no = self.entry_ID.get()
            name = self.entry_name.get()
            surname = self.entry_surname.get()
            phone = self.entry_phone.get()

            name_kin = self.entry_kin_name.get()
            phone_kin = self.entry_kin_phone.get()

            # validity check
            rsaidnumber.parse(id_no)
            int(phone)
            int(phone_kin)

            if name == '' or surname == '' or phone == '' or name_kin == '' or phone_kin == '':
                messagebox.showerror(message='Empty entry fields not allowed')

            elif (len(phone) < 10 or len(phone) > 10) or (len(phone_kin) < 10 or len(phone_kin) > 10):
                messagebox.showerror(message='Phone numbers must be 10 digits')

            else:
                query = "insert into Users (ID, name, surname, phone) values ('{}', '{}', '{}', '{}')".format(id_no,
                                                                                                              name,
                                                                                                              surname,
                                                                                                              phone)
                mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='lifechoices_online', auth_plugin='mysql_native_password')

                mycursor = mydb.cursor()
                mycursor.execute(query)
                mydb.commit()

                query_kin = "insert into next_of_kin (ID, name, phone) values ('{}', '{}', '{}')".format(id_no,
                                                                                                     name_kin,
                                                                                                     phone_kin)
                mycursor.execute(query_kin)
                mydb.commit()

                self.pop_treeview()

        except ValueError:
            messagebox.showerror(message="ID number or phone number(s) are invalid")

    def remove(self):
        id_no = self.current_id
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        query_check = "select * from admin_users where ID='{}'".format(id_no)
        mycursor.execute(query_check)
        result = mycursor.fetchall()

        if not result:
            pass
        else:
            query_admin = "delete from admin_users where ID='{}'".format(id_no)

        query_kin = "delete from next_of_kin where ID='{}'".format(id_no)
        mycursor.execute(query_kin)
        mydb.commit()
        query = "delete from Users where ID='{}'".format(id_no)
        mycursor.execute(query)
        mydb.commit()

        self.pop_treeview()


root = Tk()
app = AdminGUI(root)
root.mainloop()

