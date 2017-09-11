import socket
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

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
''' MIT License

Copyright (c) 2017 Bret Cadle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

datefontsize = 50
clockfontsize = 50
weatherfontsize = 50


def tick(time1=''):
    try:
        # get UTC time
        time2 = time.strftime('%H:%M:%S UTC', gmtime())
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
    except:
        time2 = "no"
        clock.config(Text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)


def UTCdate(date1=''):
    # get Date at UTC
    date2 = time.strftime('%B %d %Y', gmtime())
    # if date string has changed, update it
    if date2 != date1:
        date1 = date2
        date.config(text=date2)
    # calls itself every n milliseconds
    # to update the date display as needed
    print(date2)
    date.after(200, tick)


def tempcheck(temp1=''):
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
    except:
        error = "network error"
        weather.config(text=error)

    weather.after(10000, tempcheck)


root = tk.Tk()


# Sample button donothing
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


# Settings menu button
def settings():
    win = Toplevel(root)
    win.wm_title('Settings')

    def setclockfont():
        newfontsize = clockfontentry.get()
        clock.config(font=(
            'freesans',
            newfontsize, 'bold'))


    def setdatefont():
        newfontsize = datefontentry.get()
        date.config(font=(
            'freesans',
            newfontsize, 'bold'))


    def setweatherfont():
        newfontsize = weatherfontentry.get()
        weather.config(font=(
            'freesans',
            newfontsize, 'bold'))

    clockfontsizelabel = tk.Label(
        win,
        text='Clock fontsize (default 50)',
        anchor=E)
    clockfontsizelabel.grid(row=0, column=0)

    datefontsizelabel = tk.Label(win,
        text='Date fontsize (default 50)',
        anchor=E)
    datefontsizelabel.grid(row=1, column=0)

    weatherfontsizelabel = tk.Label(win,
        text='Weather fontsize (default 50)',
        anchor=E,)
    weatherfontsizelabel.grid(row=2, column=0)

    clockfontentry = Entry(win)
    datefontentry = Entry(win)
    weatherfontentry = Entry(win)

    clockfontconfirm = tk.Button(win, text='confirm', command=setclockfont)
    datefontconfirm = tk.Button(win, text='confirm', command=setdatefont)
    weatherfontconfirm = tk.Button(win, text='confirm', command=setweatherfont)

    clockfontentry.grid(row=0, column=1)
    clockfontconfirm.grid(row=0, column=2)
    datefontentry.grid(row=1, column=1)
    datefontconfirm.grid(row=1, column=2)
    weatherfontentry.grid(row=2, column=1)
    weatherfontconfirm.grid(row=2, column=2)


# Set the window title bar text
root.wm_title('Northwest Clock')
appname = tk.Label(
    root,
    font=('TakaoPGothic', 50,),
    bg='#00541c',
    fg='#141414',
    anchor='w',)
appname.config(text='Northwest Clock')
# Set clock label text
appname.pack(fill='both', expand=1)
date = tk.Label(
    root,
    font=('freesans', datefontsize, 'bold'),
    bg='#212121',
    fg='#cecece')
date.pack(fill='both', expand=1)
clock = tk.Label(
    root,
    font=('freesans', clockfontsize, 'bold'),
    bg='#212121',
    fg='#cecece')
clock.pack(fill='both', expand=1)
# Set weather label text
weather = tk.Label(
    root,
    font=('freesans', weatherfontsize, 'bold'),
    bg='#212121',
    fg='#cecece'
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

tempcheck()
UTCdate()
tick()
root.mainloop()
