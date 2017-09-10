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


def tick(time1=''):
    # get UTC time
    time2 = time.strftime('%H:%M:%S UTC', gmtime())
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
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

# Set the window title bar text
root.wm_title('Northwest Clock')
appname = tk.Label(
    root,
    font=('TakaoPGothic', 125,),
    bg='#00541c',
    fg='#141414',
    anchor='w',)
appname.config(text='Northwest Clock')
appname.pack(fill='both', expand=1)
date = tk.Label(
    root,
    font=('freesans', 85, 'bold'),
    bg='#212121',
    fg='#cecece')
date.pack(fill='both', expand=1)
clock = tk.Label(
    root,
    font=('freesans', 200, 'bold'),
    bg='#212121',
    fg='#cecece')
clock.pack(fill='both', expand=1)
outtemp = tk.Label(
    root,
    font=('freesans', 100, 'bold'),
    bg='#212121',
    fg='#cecece'
)
outtemp.pack(fill='both', expand=1)
tempcheck()
UTCdate()
tick()
root.mainloop()
