# importing libraries ...
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from datetime import datetime
import os

# global variable time
in_time = ''


def count_hours():
    sec = in_time * 3600 # convert hours into seconds
    start_counting_sec = time.time() # get the start work time in seconds
    start_counting_full = datetime.fromtimestamp(start_counting_sec).strftime("%A, %B %d, %Y %I:%M:%S")
    print("start work: ", start_counting_full)

    time_after_hrs_sec = start_counting_sec + sec # calculate break time in seconds
    time_after_hrs_full = datetime.fromtimestamp(time_after_hrs_sec).strftime("%A, %B %d, %Y %I:%M:%S")
    print("break time: ", time_after_hrs_full)

    while time.time() < time_after_hrs_sec:
        time.sleep(1) # sleep the program " cpu does not work on this program untill the loop is finished "
    option = messagebox.askquestion(title="Info message", message="Time to take a break?!")
    if option == "yes":
        os.system(r"rundll32.exe user32.dll,LockWorkStation") # lock the computer
    else:
        messagebox.showinfo(title="invalid input",message="continue work!")


# GUI part ...
root = Tk()  # root view
style = ttk.Style()  # style used for every object
root.resizable(False, False)  # fixed size
root.title("Break Time")  # root view title
root.configure(background="#C0C0C0")  # root view background color

# first label informative label...
ttk.Label(root, text="Sleep after ", font=('Arial', 10)).grid(row=0, column=1, pady=10, padx=10)

# input field...
EntrySleepTime = ttk.Entry(root, width=20, font=('Arial', 16))
EntrySleepTime.grid(row=1, column=1, pady=10)

# setting time button...
settingTime_btn = ttk.Button(root, text="Set Time")
settingTime_btn.grid(row=3, column=1, pady=10, padx=10)
style.configure("TButton", background="green")
settingTime_btn.configure(style='TButton')

# exit button...
exit_btn = ttk.Button(root, text="Exit ")
exit_btn.grid(row=4, column=1, pady=10, padx=10)


# when the set time button clicked...
def ButtonClick():
    try:
        global in_time
        in_time = int(EntrySleepTime.get())
        count_hours()
    except Exception as ex:  # exception clause if there are any errors with the input...
        messagebox.showinfo(title="invalid input",
                            message="Enter the time in hours !\ni.e. try 2 for 2 hours etc.")
        EntrySleepTime.delete(0, 'end')


# when the exit button clicked...
def exitClick():
    exit(0)  # close the program...


settingTime_btn.config(command=ButtonClick)
exit_btn.config(command=exitClick)

root.mainloop()
# end of GUI part...
