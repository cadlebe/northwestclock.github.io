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

import six
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements
import appdirs
import time
from time import gmtime
import pyowm
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

from tkinter import *

def tick(time1=''):
    # get UTC time
    time2 = time.strftime('%B %d %Y \n%H:%M:%S UTC', gmtime())
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)


def tempcheck(temp1=''):
    # API key for Open Weather Map
    owm = pyowm.OWM(API_key='8a3f8610bb7985541149717900f43011')
    # Get weather for seattle, all of it
    observation = owm.weather_at_place('Seattle, US')
    w = observation.get_weather()
    currenttemp = w.get_temperature('fahrenheit')
    temp2 = currenttemp['temp']

    if temp2 != temp1:
        temp1 = temp2
        outtemp.config(text=str(int(temp1)) + ' F')


    outtemp.after(300000, tempcheck)


root = tk.Tk()

# Sample button donothing
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
# Settings menu button
def settings():
    filewin = Toplevel(root)
    button = Button(filewin, Text="Settings")
    button.pack()

# Set the window title bar text
root.wm_title('Northwest Clock')
appname = tk.Label(
    root,
    font=('TakaoPGothic', 125,),
    bg='#00541c',
    fg='#141414',
    anchor='w',)
appname.config(text='Northwest Clock')
# Set clock label text
appname.pack(fill='both', expand=1)
clock = tk.Label(
    root,
    font=('freesans', 200, 'bold'),
    bg='#212121',
    fg='#cecece')
clock.pack(fill='both', expand=1)
# Set weather label text
outtemp = tk.Label(
    root,
    font=('freesans', 100, 'bold'),
    bg='#212121',
    fg='#cecece'
)
outtemp.pack(fill='both', expand=1)
# create top menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
editmenu.add_command(label="Settings", command=settings)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

tempcheck()
tick()
root.mainloop()