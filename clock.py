''' tk_clock101.py
use Tkinter to show a digital clock
tested with Python27 and Python33
'''
import time
from time import gmtime
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

root = tk.Tk()
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
tick()
root.mainloop()