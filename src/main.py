# Development uncomment:
# from tkinter import *
# Release uncomment:
import pytz
import webbrowser
import pyowm
import argparse
import configuration
import os.path
import sys

from tkinter import (
    Button,
    Label,
    Canvas,
    Toplevel,
    E,
    W,
    N,
    S,
    Entry,
    StringVar,
    Message,
    LEFT,
    Menu,
)
from datetime import datetime, timedelta
from pytz import timezone

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


def main():
    config = configuration.Configuration()
    config_vars = vars(configuration.Configuration())
    path_to_config = config_vars.get("path_to_config")
    timefmt = "%H:%M:%S %Z"
    datefmt = "%Y-%m-%d"
    version = "0215"

    # Check if this is the first time running the app, if yes then create default ini
    if os.path.isfile(path_to_config + "config.ini"):
        config.ReadConfigFile()
        if config.getFirstRun() == True:
            config.SetDefaultConfigFile()
            config.setFirstRun("false")
    else:
        config.SetDefaultConfigFile()
        config.setFirstRun("false")

    # Default label attributes
    datefontsize = config.getFontsize("date")
    clockfontsize = config.getFontsize("clock")
    weatherfontsize = config.getFontsize("weather")
    timezones_common = pytz.common_timezones

    state = False

    parser = argparse.ArgumentParser(description="Northwest Clock - UTC")
    parser.add_argument(
        "--fullscreen",
        help="Opens app in full screen, usefull for displays that have no keyboard and mouse.",
        action="store_true",
    )
    args = parser.parse_args()
    if args.fullscreen:
        state = True
    else:
        state = False

    def close_window(window):
        window.destroy()

    def currenttime():
        utc = pytz.utc
        timezone_str = config.getTimezone()
        timezone = pytz.timezone(timezone_str)
        timeUTC = datetime(2002, 10, 27, 12, 0, 0, tzinfo=utc).now()
        currenttime = timeUTC.astimezone(timezone)
        return currenttime

    def tick(time1=""):
        """ This module checks for the current UTC time every 200ms """
        time2 = currenttime()
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            time_string = time2.strftime(timefmt)
            clock.config(text=time_string)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        clock.after(200, tick)

    def dateutc(date1=""):
        """ Checks current date at UTC every 200ms """
        # get Date at UTC
        date2 = currenttime()
        # if date string has changed, update it
        if date2 != date1:
            date1 = date2
            date_string = date2.strftime(datefmt)
            date.config(text=date_string)
        # calls itself every n milliseconds
        # to update the date display as needed
        date.after(200, dateutc)

    def tempcheck(temp1=""):
        """ Using OWM, checks for temperature every 10000ms """
        apikey = str(config.getApiKey())
        weather_location = str(config.getWeatherLocation("weather location"))
        try:
            # API key for Open Weather Map
            owm = pyowm.OWM(API_key=apikey)
            # Get weather for seattle, all of it
            observation = owm.weather_at_place(weather_location)
            # observation = owm.weather_at_place('Seattle, US')
            w = observation.get_weather()
            currenttemp = w.get_temperature("fahrenheit")
            temp2 = currenttemp["temp"]

            if temp2 != temp1:
                temp1 = temp2
                weather.config(text=str(int(temp1)) + " F")
            weather.after(10000, tempcheck)
            return temp2
        except:
            error = "network error"
            weather.config(text=error)
            return error

    root = tk.Tk()

    # Sample button donothing
    def donothing():
        """ Placeholder for buttons that currently "do nothing" """
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()

    # Settings menu button
    def settings():
        """ Opens settings window """
        win = Toplevel(root)
        win.wm_title("Settings")

        def close_settings():
            win.destroy()

        def settitletext():
            """ Assigns title text """
            newtitletext = titletextentry.get()
            nwclockapp.config(text=newtitletext)
            config.setTitleText(newtitletext)

        def settitlebgcolor():
            """ Assigns new bgcolor size to title label """
            newbgcolor = titlebgcolorentry.get()
            nwclockapp.config(bg=newbgcolor)
            config.setColor("titlebackground", newbgcolor)

        """def settitlefont():
            """ " Assigns new font size to title label " """
            newfontsize = titlefontentry.get()
            title.config(font=('freesans', newfontsize, 'bold')) """

        # Define how each button behaves, maybe refactor this later
        def setclockfont():
            """ Assigns new font size to clock label """
            newfontsize = clockfontentry.get()
            clock.config(font=("freesans", newfontsize, "bold"))
            config.SetFontSize("clock", newfontsize)

        def setdatefont():
            """ Assigns new font size to date label """
            newfontsize = datefontentry.get()
            date.config(font=("freesans", newfontsize, "bold"))
            config.SetFontSize("date", newfontsize)

        def setweatherfont():
            """ Assigns new font size to weather label """
            newfontsize = weatherfontentry.get()
            weather.config(font=("freesans", newfontsize, "bold"))
            config.SetFontSize("weather", newfontsize)

        def setdatebgcolor():
            """ Assigns new background color to date label """
            newbgcolor = datebgcolorentry.get()
            date.config(bg=newbgcolor)
            config.setColor("date", newbgcolor)

        def setclockbgcolor():
            """ Assigns new background color to clock label """
            newbgcolor = clockbgcolorentry.get()
            clock.config(bg=newbgcolor)
            config.setColor("clock", newbgcolor)

        def setweatherbgcolor():
            """ Assigns new background color to weather label """
            newbgcolor = weatherbgcolorentry.get()
            weather.config(bg=newbgcolor)
            config.setColor("weather", newbgcolor)

        def setapikey():
            """ Allows user to set api for openweather if desired """
            apikey = apikeyentry.get()
            config.setApiKey(apikey)

        def settimezone():
            timezone = timezoneentry.get()
            timezones = pytz.all_timezones
            if timezone in timezones:
                config.setTimezone(timezone)
                timezoneerror.config(text="")
            else:
                error = "Invalid Timezone!"
                timezoneerror.config(text=error)

        def setweatherlocation():
            weatherlocation = weatherlocationentry.get()
            config.setWeatherLocation(weatherlocation)

        def setdefaults():
            config.SetDefaultConfigFile()

            """ Assigns title text """
            newtitletext = config.getTitleText()
            nwclockapp.config(text=newtitletext)
            config.setTitleText(newtitletext)

            """ Assigns new bgcolor size to title label """
            newbgcolor = config.getColor("titlebackground")
            nwclockapp.config(bg=newbgcolor)

            """ Assigns new font size to clock label """
            newfontsize = config.getFontsize("clock")
            clock.config(font=("freesans", newfontsize, "bold"))

            """ Assigns new font size to date label """
            newfontsize = config.getFontsize("date")
            date.config(font=("freesans", newfontsize, "bold"))

            """ Assigns new font size to weather label """
            newfontsize = config.getFontsize("weather")
            weather.config(font=("freesans", newfontsize, "bold"))

            """ Assigns new background color to date label """
            newbgcolor = config.getColor("datebackground")
            date.config(bg=newbgcolor)

            """ Assigns new background color to clock label """
            newbgcolor = config.getColor("clockbackground")
            clock.config(bg=newbgcolor)

            """ Assigns new background color to weather label """
            newbgcolor = config.getColor("weatherbackground")
            weather.config(bg=newbgcolor)

        # Create and position Labels in Grid
        titletextlabel = tk.Label(win, text="Title Text", anchor=E)
        titletextlabel.grid(row=0, column=0)

        titlebgcolorlabel = tk.Label(win, text="Title Background Color", anchor=E)
        titlebgcolorlabel.grid(row=1, column=0)

        datefontsizelabel = tk.Label(win, text="Date Fontsize", anchor=E)
        datefontsizelabel.grid(row=2, column=0)

        clockfontsizelabel = tk.Label(win, text="Clock Fontsize", anchor=E)
        clockfontsizelabel.grid(row=3, column=0)

        weatherfontsizelabel = tk.Label(
            win,
            text="Weather Fontsize",
            anchor=E,
        )
        weatherfontsizelabel.grid(row=4, column=0)

        datebgcolorlabel = tk.Label(
            win,
            text="Date bgcolor",
            anchor=E,
        )
        datebgcolorlabel.grid(row=5, column=0)

        clockbgcolorlabel = tk.Label(
            win,
            text="Clock bgcolor",
            anchor=E,
        )
        clockbgcolorlabel.grid(row=6, column=0)

        weatherbgcolorlabel = tk.Label(
            win,
            text="Weather bgcolor",
            anchor=E,
        )
        weatherbgcolorlabel.grid(row=7, column=0)

        apikeylabel = tk.Label(
            win,
            text="Openweather API Key",
            anchor=E,
        )
        apikeylabel.grid(row=8, column=0)

        timezonelabel = tk.Label(
            win,
            text="Timezone",
            anchor=E,
        )
        timezonelabel.grid(row=9, column=0)

        timezoneerror = tk.Label(
            win,
            anchor=E,
        )
        timezoneerror.grid(row=9, column=3)

        weatherlocationlabel = tk.Label(
            win,
            text="Weather Location",
            anchor=E,
        )
        weatherlocationlabel.grid(row=10, column=0)

        loaddefaultslabel = tk.Label(
            win,
            text="Load Defaults",
            anchor=E,
        )
        loaddefaultslabel.grid(row=11, column=0)

        # Create Buttons
        titletextconfirm = tk.Button(win, text="confirm", command=settitletext)

        titlebgcolorconfirm = tk.Button(win, text="confirm", command=settitlebgcolor)

        datefontconfirm = tk.Button(win, text="confirm", command=setdatefont)

        clockfontconfirm = tk.Button(win, text="confirm", command=setclockfont)

        weatherfontconfirm = tk.Button(win, text="confirm", command=setweatherfont)

        datebgcolorconfirm = tk.Button(win, text="confirm", command=setdatebgcolor)

        clockbgcolorconfirm = tk.Button(win, text="confirm", command=setclockbgcolor)

        weatherbgcolorconfirm = tk.Button(
            win, text="confirm", command=setweatherbgcolor
        )

        apikeyconfirm = tk.Button(win, text="confirm", command=setapikey)

        timezoneconfirm = tk.Button(win, text="confirm", command=settimezone)

        weatherlocationconfirm = tk.Button(
            win, text="confirm", command=setweatherlocation
        )

        loaddefaultsconfirm = tk.Button(win, text="confirm", command=setdefaults)

        # create Entry Spaces
        titletextentry = Entry(win)
        titlebgcolorentry = Entry(win)

        datefontentry = Entry(win)
        clockfontentry = Entry(win)
        weatherfontentry = Entry(win)

        datebgcolorentry = Entry(win)
        clockbgcolorentry = Entry(win)
        weatherbgcolorentry = Entry(win)

        apikeyentry = Entry(win)

        timezoneentry = Entry(win)

        weatherlocationentry = Entry(win)

        # Position entry spaces and buttons in grid
        titletextentry.grid(row=0, column=1)
        titletextconfirm.grid(row=0, column=2)
        titlebgcolorentry.grid(row=1, column=1)
        titlebgcolorconfirm.grid(row=1, column=2)
        datefontentry.grid(row=2, column=1)
        datefontconfirm.grid(row=2, column=2)
        clockfontentry.grid(row=3, column=1)
        clockfontconfirm.grid(row=3, column=2)
        weatherfontentry.grid(row=4, column=1)
        weatherfontconfirm.grid(row=4, column=2)
        datebgcolorentry.grid(row=5, column=1)
        datebgcolorconfirm.grid(row=5, column=2)
        clockbgcolorentry.grid(row=6, column=1)
        clockbgcolorconfirm.grid(row=6, column=2)
        weatherbgcolorentry.grid(row=7, column=1)
        weatherbgcolorconfirm.grid(row=7, column=2)
        apikeyentry.grid(row=8, column=1)
        apikeyconfirm.grid(row=8, column=2)
        timezoneentry.grid(row=9, column=1)
        timezoneconfirm.grid(row=9, column=2)
        weatherlocationentry.grid(row=10, column=1)
        weatherlocationconfirm.grid(row=10, column=2)
        loaddefaultsconfirm.grid(row=11, column=1)

        close_about_button = tk.Button(
            win, text="Exit without save", command=close_settings
        )
        close_about_button.grid(row=12, column=0)

        # TODO: consider using a tabbed notebook here when settings page
        # gets a little too full

    def about_page():
        win = Toplevel(root)
        win.wm_title("About")
        row = 0

        if hasattr(sys, "_MEIPASS"):
            """Ignore sys._MEIPASS error, pyinstaller compiles just fine and about
            page functions once binary is build and run.
            TODO: fix sys._MEIPASS error before compiling. For now this works
            despite error"""
            description_data = os.path.join(sys._MEIPASS, "description")
        else:
            description_data = "description"
        description_file = open(description_data, "rt")
        desc_text = description_file.read()
        description_file.close()

        about_var = StringVar()
        about_var.set(desc_text)

        def callback():
            webbrowser.open_new_tab(
                r"https://github.com/cadlebe/northwestclock.github.io/wiki"
            )

        def close_about():
            win.destroy()

        abouttitlelabel = tk.Label(
            win,
            font=(
                "freesans",
                24,
                "bold",
            ),
            text="About",
            justify=LEFT,
            anchor=E,
        )
        abouttitlelabel.grid(row=row, column=0)

        row += 1

        about_text = Message(
            win,
            font=(
                "freesans",
                16,
            ),
            textvariable=about_var,
            justify=LEFT,
            anchor=E,
        )
        about_text.grid(row=row, column=0)

        row += 1

        github_link_button = tk.Button(
            win, text="See Wiki for more information", command=callback
        )
        github_link_button.grid(row=row, column=0)

        row += 1

        versionlabel = tk.Label(
            win,
            font=("freesans", 12, "bold"),
            text="Version: " + version,
            justify=LEFT,
            anchor=E,
        )
        versionlabel.grid(row=row, column=0)

        row += 1

        copyrightlabel = tk.Label(
            win,
            font=("freesans", 12, "bold"),
            text="Copyright 2019 Bret Cadle",
            justify=LEFT,
            anchor=E,
        )
        copyrightlabel.grid(row=row, column=0)

        row += 1

        close_about_button = tk.Button(win, text="Close Window", command=close_about)
        close_about_button.grid(row=row, column=0)

    # Set the window title bar text
    root.wm_title(config.getTitleText())
    nwclockapp = tk.Label(
        root,
        font=(
            "TakaoPGothic",
            50,
        ),
        bg=config.getColor("titlebackground"),
        fg=config.getColor("titleforeground"),
        anchor="w",
    )
    nwclockapp.config(text=config.getTitleText())
    # Set clock label text
    nwclockapp.pack(fill="both", expand=1)
    date = tk.Label(
        root,
        font=("freesans", datefontsize, "bold"),
        bg=config.getColor("datebackground"),
        fg=config.getColor("dateforeground"),
    )
    date.pack(fill="both", expand=1)
    clock = tk.Label(
        root,
        font=("freesans", clockfontsize, "bold"),
        bg=config.getColor("clockbackground"),
        fg=config.getColor("clockforeground"),
    )
    clock.pack(fill="both", expand=1)
    # Set weather label text
    weather = tk.Label(
        root,
        font=("freesans", weatherfontsize, "bold"),
        bg=config.getColor("weatherbackground"),
        fg=config.getColor("weatherforeground"),
    )
    temperature = tempcheck()
    if temperature != "network error":
        weather.pack(fill="both", expand=1)
    else:
        print(temperature)

    # create top menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)

    editmenu.add_command(label="Settings", command=settings)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)

    helpmenu.add_command(label="About...", command=about_page)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    # Code for handling fullscreen
    root.attributes("-fullscreen", state)

    tempcheck()
    dateutc()
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
