import tkinter as ui
from turtle import color
import time

#Creates a GUI window.
window = ui.Tk()
window.title('Clock')
window.config(bg='red')

def update_time():
    hours = time.strftime('%I')
    minutes = time.strftime('%M')
    seconds = time.strftime('%S')
    am_pm = time.strftime('%p')
    set_time = hours + ':' + minutes + ':' + seconds + ' ' + am_pm
    clock_lbl.config(text=set_time)

#Clock label and call. 
clock_lbl = ui.Label(window, text='00:00:00', font='Arial 90 bold', fg='lime')
clock_lbl.pack()

#Calls the Window.
window.mainloop()


