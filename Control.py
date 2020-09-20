from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from DbConnectClass import DBConnect
from ListReservation import ListTickets

dbConnect = DBConnect()
root = Tk()
root.resizable(False, False)
root.title("Ticket Reservation")
root.configure(background="#e1d8b2")

ttk.Label(root, text="Full name:").grid(row=0, column=0, pady=10, padx=10)
EntryFullName = ttk.Entry(root, width=30, font=('Arial', 16))
EntryFullName.grid(row=0, column=1, columnspan=2, pady=10)

# style
style = ttk.Style()
# print(style.theme_names())
style.theme_use('winnative')
style.configure("TLabel", background="#e1d8b2")
# style.configure("TButton", background="#e1d8b2")
style.configure("TRadiobutton", background="#e1d8b2")

SpanGender = StringVar()
SpanGender.set("Male")
ttk.Label(root, text="Gender").grid(row=1, column=0)
ttk.Radiobutton(root, text="Male", variable=SpanGender, value="Male").grid(row=1, column=1)
ttk.Radiobutton(root, text="Female", variable=SpanGender, value="Female").grid(row=1, column=2)

TextComments = Text(root, width=30, height=10, font=('Arial', 16))
TextComments.grid(row=3, column=1, columnspan=2, ipadx=20, ipady=20)
ttk.Label(root, text="Comments:").grid(row=3, column=0)

buButton = ttk.Button(root, text="Submit")
buButton.grid(row=4, column=1, sticky='snew')
style.configure('custom.TButton', background='green')
buButton.configure(style='custom.TButton')
style.map('custom.TButton', foreground=[('pressed', 'green')])

buList = ttk.Button(root, text="List Records")
buList.grid(row=4, column=2, sticky='snew')

budelete = ttk.Button(root, text="Delete record")
budelete.grid(row=4, column=3, sticky='snew')
style.configure('custom2.TButton', background='red')
budelete.configure(style='custom2.TButton')
style.map('custom2.TButton', foreground=[('pressed', 'red')])

buupdate = ttk.Button(root, text="Update record")
buupdate.grid(row=5, column=3, sticky='snew')


def ButtonClick():
    print("Full name:{}".format(EntryFullName.get()))
    print("Gender:{}".format(SpanGender.get()))
    print("Comments:{}".format(TextComments.get(1.0, 'end')))
    msg = dbConnect.Add(EntryFullName.get(), SpanGender.get(), TextComments.get(1.0, 'end'))
    messagebox.showinfo(title="Add info", message=msg)
    EntryFullName.delete(0, 'end')
    TextComments.delete(1.0, 'end')


def ButtonList():
    listTickets = ListTickets()


def btndelete():
    id = askstring('delete a record', 'Which ID to delete?')
    msg = dbConnect.DeleteRecord(int(id))
    messagebox.showinfo(title="delete message", message=msg)


def btnupdate():
    inpts = askstring('delete a record', 'please type the ID Name Comment separated by one space!').split()
    msg = dbConnect.UpdateRecord(int(inpts[0]), inpts[1], inpts[2])
    messagebox.showinfo(title="delete message", message=msg)


buButton.config(command=ButtonClick)

buList.config(command=ButtonList)

budelete.config(command=btndelete)

buupdate.config(command=btnupdate)

root.mainloop()
