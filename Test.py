from time import *
from tkinter import *
from feedparser import *
from pyowm import OWM
from math import *
from datetime import *

print(" > Start Init")
bkgrndcolor = "#b1bb78"
# Weather Handling Code
size = "900x400"
APIKEY = '233a80f0949773a2a747fda592388231'

owm = OWM(APIKEY)
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=45.357132, lon=-122.84750)
feelslike = one_call.forecast_daily[0].temperature('fahrenheit').get('feels_like_morn', None)
observation = mgr.weather_at_zip_code('97140', 'us')
weathervar = observation.weather.status
feelslikevar = str(trunc(feelslike)) + " F"

print(" > Done Weather Load")

# News Handling Code
NewsFeed = parse("http://feeds.foxnews.com/foxnews/national")
entry = NewsFeed.entries[1]
newsvar = "Fox News (National): " + entry.title

NewsFeed1 = parse("http://feeds.foxnews.com/foxnews/politics")
entry1 = NewsFeed1.entries[1]
news1var = "Fox News (Politics): " + entry1.title

NewsFeed2 = parse("http://feeds.foxnews.com/foxnews/scitech")
entry2 = NewsFeed2.entries[1]
news2var = "Fox News (Sci & Tech): " + entry2.title
print(" > Done News Load")

NewsFeed3 = parse("http://feeds.feedburner.com/breitbart")
entry3 = NewsFeed3.entries[1]
news3var = "Breitbart: " + entry3.title

NewsFeed4 = parse("http://www.sherwoodfire.com/RSSFeeds/rss_whats_new.cfm")
entry4 = NewsFeed4.entries[1]
news4var = "Sherwood Fire: " + entry4.title

NewsFeed5 = parse("https://www.sherwoodconservatives.com/news/feed")
entry5 = NewsFeed5.entries[1]
news5var = "Sherwood Conservatives: " + entry5.title

print(" > Done News Load")
# Init root
root = Tk()

# To be implemented into main from settings
finalzip = StringVar()
finaltz = StringVar()
# photo = PhotoImage(file="gibby.png")

text = Text(root)
text.insert(INSERT, "FUCK YOU")
text.pack()
def time():
    # Gets time for the timeLabel on main screen (root)
    string = strftime("%B %d %Y \n %I:%M %p")
    timeLabel.config(text=string)
    timeLabel.after(1000, time)
    return


def settings():
    # Settings screen (sett)
    def getentry():
        finalzip.set(entry0.get())
        finaltz.set(entry1.get())

        return
    sett = Tk()

    zipcode = Label(sett, text="Zip Code: ", bg=bkgrndcolor)
    entry0 = Entry(sett)

    timezone = Label(sett, text="Timezone (Pacific, Mountain, Central): ", bg=bkgrndcolor)
    entry1 = Entry(sett)

    submit = Button(sett, text="Submit", command=lambda: getentry(), bg=bkgrndcolor)
    zipcode.pack()
    entry0.pack()
    timezone.pack()
    entry1.pack()
    submit.pack()
    sett.title("Smart Screen    Settings")
    sett.geometry("400x200")
    sett.configure(bg=bkgrndcolor)
    sett.grid_rowconfigure(0, weight=1)
    sett.grid_columnconfigure(0, weight=1)
    sett.mainloop()
    return


# Buttons on Main Screen
exitbutton = Button(root, text="Exit", command=lambda: quit(), bg=bkgrndcolor)
settingsButton = Button(root, text="Settings", command=lambda: settings(), bg=bkgrndcolor, fg="#212121")

# Grid Arrangements
timeLabel = Label(root, font=("Times", 25), bg=bkgrndcolor)
weatherLabel = Label(root, font=("Arial", 25), text=weathervar, bg=bkgrndcolor)
feelsLikeLabel = Label(root, font=("Arial", 20), text=feelslikevar, bg=bkgrndcolor)
newsLabel = Label(root, font=("Arial", 12), text=newsvar, bg=bkgrndcolor)
news1Label = Label(root, font=("Arial", 12), text=news1var, bg=bkgrndcolor)
news2Label = Label(root, font=("Arial", 12), text=news2var, bg=bkgrndcolor)
news3Label = Label(root, font=("Arial", 12), text=news3var, bg=bkgrndcolor)
news4Label = Label(root, font=("Arial", 12), text=news4var, bg=bkgrndcolor)
news5Label = Label(root, font=("Arial", 12), text=news5var, bg=bkgrndcolor)

timeLabel.pack()

weatherLabel.pack()
feelsLikeLabel.pack()

newsLabel.pack()
news1Label.pack()
news2Label.pack()
news3Label.pack()
news4Label.pack()
news5Label.pack()
settingsButton.pack(fill=X)
exitbutton.pack(fill=X)

root.geometry(size)
root.title("Smart Screen")
root.configure(bg=bkgrndcolor)
time()
print(" > Loaded in at " + size + " at " + datetime.now().strftime("%H:%M:%S"))
root.mainloop()
