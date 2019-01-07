import time
from time import gmtime
from tkinter import *

import appdirs
import packaging
import packaging.requirements
import packaging.specifiers
import packaging.version
import pyowm
import six
import argparse
import configuration
import os.path

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

config = configuration.Configuration()
config_vars = vars(configuration.Configuration())
path_to_config = config_vars.get('path_to_config')

# Check if this is the first time running the app, if yes then create default ini
if os.path.isfile(path_to_config + 'config.ini'):
    print(path_to_config + "config.ini")
    config.ReadConfigFile()
    if config.getFirstRun() == True:
        print("were Here")
        config.SetDefaultConfigFile()
        config.setFirstRun('false')
else:
    print("We shouldn't be here")
    config.SetDefaultConfigFile()
    config.setFirstRun('false')

# Default label attributes
datefontsize = config.getFontsize('date')
clockfontsize = config.getFontsize('clock')
weatherfontsize = config.getFontsize('weather')

state = False

parser = argparse.ArgumentParser(description='Northwest Clock - UTC')
parser.add_argument('--fullscreen', help='Opens app in full screen, usefull for displays that have no keyboard and mouse.', action='store_true')
args = parser.parse_args()
if args.fullscreen:
    state = True
else:
    state = False

def tick(time1=''):
    """ This module checks for the current UTC time every 200ms """
    # get UTC time
    time2 = time.strftime('%H:%M:%S UTC', gmtime())
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)


def dateutc(date1=''):
    """ Checks current date at UTC every 200ms """
    # get Date at UTC
    date2 = time.strftime('%B %d %Y', gmtime())
    # if date string has changed, update it
    if date2 != date1:
        date1 = date2
        date.config(text=date2)
    # calls itself every n milliseconds
    # to update the date display as needed
    date.after(200, dateutc)


def tempcheck(temp1=''):
    """ Using OWM, checks for temperature every 10000ms """
    try:
        # API key for Open Weather Map
        owm = pyowm.OWM(API_key='8a3f8610bb7985541149717900f43011')
        # Get weather for seattle, all of it
        observation = owm.weather_at_place('Seattle, US')
        w = observation.get_weather()
        currenttemp = w.get_temperature('fahrenheit')
        temp2 = currenttemp['temp']

        if temp2 != temp1:
            temp1 = temp2
            weather.config(text=str(int(temp1)) + ' F')
    # TODO: At some point handle this error correctly
    except:
        error = "network error"
        weather.config(text=error)

    weather.after(10000, tempcheck)


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
    win.wm_title('Settings')

    def settitletext():
        """ Assigns title text """
        newtitletext = titletextentry.get()
        nwclockapp.config(text=newtitletext)
        config.setTitleText(newtitletext)

    def settitlebgcolor():
        """ Assigns new bgcolor size to title label """
        newbgcolor = titlebgcolorentry.get()
        nwclockapp.config(bg=newbgcolor)
        config.setColor('titlebackground', newbgcolor)

    """def settitlefont():
        """" Assigns new font size to title label """"
        newfontsize = titlefontentry.get()
        title.config(font=('freesans', newfontsize, 'bold')) """

    # Define how each button behaves, maybe refactor this later
    def setclockfont():
        """ Assigns new font size to clock label """
        newfontsize = clockfontentry.get()
        clock.config(font=(
            'freesans',
            newfontsize, 'bold'))
        config.SetFontSize('clock', newfontsize)

    def setdatefont():
        """ Assigns new font size to date label """
        newfontsize = datefontentry.get()
        date.config(font=(
            'freesans',
            newfontsize, 'bold'))
        config.SetFontSize('date', newfontsize)

    def setweatherfont():
        """ Assigns new font size to weather label """
        newfontsize = weatherfontentry.get()
        weather.config(font=('freesans', newfontsize, 'bold'))
        config.SetFontSize('weather', newfontsize)

    def setdatebgcolor():
        """ Assigns new background color to date label """
        newbgcolor = datebgcolorentry.get()
        date.config(bg=newbgcolor)
        config.setColor('date', newbgcolor)

    def setclockbgcolor():
        """ Assigns new background color to clock label """
        newbgcolor = clockbgcolorentry.get()
        clock.config(bg=newbgcolor)
        config.setColor('clock', newbgcolor)

    def setweatherbgcolor():
        """ Assigns new background color to weather label """
        newbgcolor = weatherbgcolorentry.get()
        weather.config(bg=newbgcolor)
        config.setColor('weather', newbgcolor)

    def setdefaults():
        config.SetDefaultConfigFile()

        """ Assigns title text """
        newtitletext = config.getTitleText()
        nwclockapp.config(text=newtitletext)
        config.setTitleText(newtitletext)

        """ Assigns new bgcolor size to title label """
        newbgcolor = config.getColor('titlebackground')
        nwclockapp.config(bg=newbgcolor)

        """ Assigns new font size to clock label """
        newfontsize = config.getFontsize('clock')
        clock.config(font=(
            'freesans',
            newfontsize, 'bold'))

        """ Assigns new font size to date label """
        newfontsize = config.getFontsize('date')
        date.config(font=(
            'freesans',
            newfontsize, 'bold'))

        """ Assigns new font size to weather label """
        newfontsize = config.getFontsize('weather')
        weather.config(font=('freesans', newfontsize, 'bold'))

        """ Assigns new background color to date label """
        newbgcolor = config.getColor('datebackground')
        date.config(bg=newbgcolor)

        """ Assigns new background color to clock label """
        newbgcolor = config.getColor('clockbackground')
        clock.config(bg=newbgcolor)

        """ Assigns new background color to weather label """
        newbgcolor = config.getColor('weatherbackground')
        weather.config(bg=newbgcolor)


    titletextlabel = tk.Label(
        win,
        text='Title Text',
        anchor=E)
    titletextlabel.grid(row=0, column=0)

    titlebgcolorlabel = tk.Label(
        win,
        text='Title Background Color',
        anchor=E)
    titlebgcolorlabel.grid(row=1, column=0)

    datefontsizelabel = tk.Label(
        win,
        text='Date Fontsize',
        anchor=E)
    datefontsizelabel.grid(row=2, column=0)

    clockfontsizelabel = tk.Label(
        win,
        text='Clock Fontsize',
        anchor=E)
    clockfontsizelabel.grid(row=3, column=0)

    weatherfontsizelabel = tk.Label(
        win,
        text='Weather Fontsize',
        anchor=E,)
    weatherfontsizelabel.grid(row=4, column=0)

    datebgcolorlabel = tk.Label(
        win,
        text='Date bgcolor',
        anchor=E,)
    datebgcolorlabel.grid(row=5, column=0)

    clockbgcolorlabel = tk.Label(
        win,
        text='Clock bgcolor',
        anchor=E,)
    clockbgcolorlabel.grid(row=6, column=0)

    weatherbgcolorlabel = tk.Label(
        win,
        text='Weather bgcolor',
        anchor=E,)
    weatherbgcolorlabel.grid(row=7, column=0)

    loaddefaultslabel = tk.Label(
        win,
        text='Load Defaults',
        anchor=E,)
    loaddefaultslabel.grid(row=8, column=0)

    titletextconfirm = tk.Button(
        win,
        text='confirm',
        command=settitletext)

    titlebgcolorconfirm = tk.Button(
        win,
        text='confirm',
        command=settitlebgcolor)

    datefontconfirm = tk.Button(
        win,
        text='confirm',
        command=setdatefont)

    clockfontconfirm = tk.Button(
        win,
        text='confirm',
        command=setclockfont)

    weatherfontconfirm = tk.Button(
        win,
        text='confirm',
        command=setweatherfont)

    datebgcolorconfirm = tk.Button(
        win,
        text='confirm',
        command=setdatebgcolor)

    clockbgcolorconfirm = tk.Button(
        win,
        text='confirm',
        command=setclockbgcolor)

    weatherbgcolorconfirm = tk.Button(
        win,
        text='confirm',
        command=setweatherbgcolor)

    loaddefaultsconfirm = tk.Button(
        win,
        text='confirm',
        command=setdefaults)

    titletextentry = Entry(win)
    titlebgcolorentry = Entry(win)

    datefontentry = Entry(win)
    clockfontentry = Entry(win)
    weatherfontentry = Entry(win)

    datebgcolorentry = Entry(win)
    clockbgcolorentry = Entry(win)
    weatherbgcolorentry = Entry(win)

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
    loaddefaultsconfirm.grid(row=8, column=1)

    # TODO: consider using a tabbed notebook here when settings page
    # gets a little too full


# Set the window title bar text
root.wm_title(config.getTitleText())
nwclockapp = tk.Label(
    root,
    font=('TakaoPGothic', 50,),
    bg=config.getColor('titlebackground'),
    fg=config.getColor('titleforeground'),
    anchor='w',)
nwclockapp.config(text=config.getTitleText())
# Set clock label text
nwclockapp.pack(fill='both', expand=1)
date = tk.Label(
    root,
    font=('freesans', datefontsize, 'bold'),
    bg=config.getColor('datebackground'),
    fg=config.getColor('dateforeground'))
date.pack(fill='both', expand=1)
clock = tk.Label(
    root,
    font=('freesans', clockfontsize, 'bold'),
    bg=config.getColor('clockbackground'),
    fg=config.getColor('clockforeground'))
clock.pack(fill='both', expand=1)
# Set weather label text
weather = tk.Label(
    root,
    font=('freesans', weatherfontsize, 'bold'),
    bg=config.getColor('weatherbackground'),
    fg=config.getColor('weatherforeground')
)
weather.pack(fill='both', expand=1)
# create top menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Settings", command=settings)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Code for handling fullscreen
root.attributes("-fullscreen", state)

tempcheck()
dateutc()
tick()
root.mainloop()
