from tkinter import *
from time import *
from tkinter.ttk import *
from datetime import datetime
root = Tk()
root.geometry("600x300")
root.title("Smart App")

root.config(bg="#c9c9c9")
def time():
    string = strftime("%B %d %Y %I:%M %p")
    label.config(text = string)
    label.after(1000, time)


label = Label(root, font=("Arial", 45))


ExitButton = Button(root, text="Exit", command=SystemExit, state=ACTIVE)

label.pack()

ExitButton.pack();
time()
root.mainloop()