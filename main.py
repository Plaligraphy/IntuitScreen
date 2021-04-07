# Requires package pyowm
from time import *
from tkinter import *
from feedparser import *
from pyowm import OWM

print(" > Start Init < ")

# Weather Handling Code
APIKEY = '233a80f0949773a2a747fda592388231'
owm = OWM(APIKEY)
mgr = owm.weather_manager()
print(" > Done Weather Load < ")
observation = mgr.weather_at_place('Portland')
weathervar = observation.weather.status

# News Handling Code
NewsFeed = parse("http://rss.cnn.com/rss/cnn_topstories.rss")
entry = NewsFeed.entries[1]
newsvar = entry.title

print(" > Done News Load < ")
root = Tk()


def time():
    string = strftime("%B %d %Y \n %I:%M %p")
    timeLabel.config(text=string)
    timeLabel.after(1000, time)
    return


def settings():
    sett = Tk()

    label = Label(sett, text="Settings")
    but0 = Button(sett, text="Change Size")
    label.grid(row=0, column=0, sticky="N")

    sett.title("Smart Screen    Settings")
    sett.geometry("400x200")
    sett.grid_rowconfigure(0, weight=1)
    sett.grid_columnconfigure(0, weight=1)
    sett.mainloop()
    return


exitbutton = Button(root, text="Exit", command=lambda: quit())
settingsButton = Button(root, text="Settings", command=lambda: settings())

timeLabel = Label(root, font=("Times", 25))
weatherLabel = Label(root, font=("Arial", 25), text=weathervar)
newsLabel = Label(root, font=("Arial", 12), text=newsvar)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

exitbutton.grid(row=3, column=3)
settingsButton.grid(row=2, column=2)

timeLabel.grid(row=0, column=0, sticky="N")
weatherLabel.grid(row=2, column=0, sticky="W")
newsLabel.grid(row=0, column=0)

root.geometry("500x500")
root.title("Smart Screen")
time()
print("Done Loading")
root.mainloop()

