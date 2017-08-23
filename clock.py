''' tk_clock101.py
use Tkinter to show a digital clock
tested with Python27 and Python33
'''
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
    # get the current local time from the PC
    # utc_time = time.gmtime()
    time2 = time.strftime('%B %d %Y \n%H:%M:%S UTC', gmtime())
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)


def tempcheck(temp1=''):
    owm = pyowm.OWM(API_key='8a3f8610bb7985541149717900f43011')
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
tick()
root.mainloop()