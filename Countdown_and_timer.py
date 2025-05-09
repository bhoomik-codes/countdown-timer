import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier
import winsound

# Creating a window
window = tk.Tk()
window.geometry('600x600')  # Giving size
window.title('PythonGeeks')  # Giving title
Label(window, text="Countdown Clock and Timer", font=('Calibri', 15)).grid(row=1, column=0)

# To print current time
def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

time_label = Label(window, text="", font=('Calibri', 15))
time_label.grid(row=2, column=1)
update_time()

check = tk.BooleanVar()  # Check is of boolean type
hour = tk.IntVar()  # Ensure count is of integer type
minute = tk.IntVar()  # Ensure count is of integer type
second = tk.IntVar()  # Ensure count is of integer type

# Create a label for countdown
countdown_label = Label(window, text="", font=('Calibri', 15))
countdown_label.grid(row=3,column=1)

# Define the countdown function
def countdown():
    h = hour.get()  # Get the value
    m = minute.get()  # Get the value
    s = second.get()  # Get the value
    t = h * 3600 + m * 60 + s

    while t:
        mins, secs = divmod(t, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        countdown_label.config(text=time_format)
        window.update()
        time.sleep(1)
        t -= 1

    if check.get():  # If the value of check is true
        winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)  # Play the .wav file as alarm sound

    global time_up_label
    time_up_label = Label(window, text="Time-Up", font=('bold', 20))
    time_up_label.grid(row=4, column=1)

    # Display notification on desktop
    toast = ToastNotifier()  # Create toast variable
    toast.show_toast("Notification", "Timer is Off", duration=20, icon_path=None, threaded=True)  # Show toast

# Define the reset function
def reset():
    hour.set(0)
    minute.set(0)
    second.set(0)
    countdown_label.config(text="")
    if 'time_up_label' in globals():
        time_up_label.destroy()
    winsound.PlaySound(None, winsound.SND_PURGE)  # Stop the alarm sound

Label(window, text="Enter time in HH:MM:SS", font=('bold')).grid(row=5, column=1)
Spinbox(window, textvariable=hour, width=15, from_=0, to=999).grid(row=7, column=1)
Spinbox(window, textvariable=minute, width=15, from_=0, to=999).grid(row=7, column=2)
Spinbox(window, textvariable=second, width=15, from_=0, to=999).grid(row=7, column=3)


Checkbutton(window, text='Check for Music', onvalue=True, variable=check).grid(row=6, column=1)  # Creating checkbox
Button(window, text="Set Countdown", command=countdown, bg='yellow').grid(pady=5, row=8, column=1)  # Create button
Button(window, text="Reset", command=reset, bg='lightblue').grid(pady=10, row=9, column=1)  # Create reset button

window.mainloop()
