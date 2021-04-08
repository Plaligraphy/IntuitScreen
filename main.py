# Requires package pyowm
from time import *
from tkinter import *
from feedparser import *
from pyowm import OWM
from math import *
from datetime import *
print(" > Start Init")

# Weather Handling Code
size = "700x300"
APIKEY = '233a80f0949773a2a747fda592388231'

owm = OWM(APIKEY)
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=45.357132, lon=-122.84750)
feelslike = one_call.forecast_daily[0].temperature('fahrenheit').get('feels_like_morn', None)
print(" > Done Weather Load")

observation = mgr.weather_at_zip_code('97140', 'us')
weathervar = observation.weather.status
feelslikevar = str(trunc(feelslike)) + " F"
# News Handling Code
NewsFeed = parse("http://rss.cnn.com/rss/cnn_topstories.rss")
entry = NewsFeed.entries[1]
newsvar = entry.title

print(" > Done News Load")


root = Tk()
finalzip = StringVar()
finaltz = StringVar()


def time():
    string = strftime("%B %d %Y \n %I:%M %p")
    timeLabel.config(text=string)
    timeLabel.after(1000, time)
    return


def settings():
    def getEntry():
        finalzip.set(entry0.get())
        finaltz.set(entry1.get())

        return
    sett = Tk()

    zipcode = Label(sett, text="Zip Code: ")
    entry0 = Entry(sett)

    timezone = Label(sett, text="Timezone (Pacific, Mountain, Central): ")
    entry1 = Entry(sett)

    submit = Button(sett, text="Submit", command=lambda: getEntry())
    zipcode.pack()
    entry0.pack()
    timezone.pack()
    entry1.pack()
    submit.pack()
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
feelsLikeLabel = Label(root, font=("Arial", 20), text=feelslikevar)
newsLabel = Label(root, font=("Arial", 12), text=newsvar)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

exitbutton.grid(row=3, column=3)
settingsButton.grid(row=2, column=2)

timeLabel.grid(row=0, column=0, sticky="N")
weatherLabel.grid(row=2, column=0, sticky="W")
feelsLikeLabel.grid(row=3, column=0, sticky="W")
newsLabel.grid(row=0, column=0)

root.geometry(size)
root.title("Smart Screen")
time()
print(" > Loaded in at " + size + " at " + datetime.now().strftime("%H:%M:%S"))
root.mainloop()

