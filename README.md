# NWClock
### Copyright 2017 Bret Cadle

This is a simple clock that displays UTC and current temp. It currently has a settings menu for changing the fontsize for the clock, date, and weather.

## Prerequisites

What you need on your system in order to install:

- Preferably Ubuntu 12.04 or later
- At least a Core i3 processor
- 256mb RAM
- Python 3.5 or later
- Various packages that the build step with show as an error
- cx_freeze

## Installing

1. Extract the .zip file to any location that you have read-write access
2. Navigate to the newly extracted directory
3. Open a terminal inside directory
4. Type:
    ```python3 setup.py build```
    or (if you have python 3.5 or later as your only installation):
    ```python setup.py build```
    *If there are any errors for missing packages then install those packages, alternatively update your setup and install cx_freeze*
5. Upon succesful completion of the build navigate to /build/exe.linux-***-3.5/ and type:
    ```./clock.py```
    and the clock should be up and running.
6. Repeat steps 4 and 5 until you no longer error and the clock comes up

#Built with

- [VSCode](https://code.visualstudio.com)
- [TKinter](https://wiki.python.org/moin/TkInter)
- [Open Weather Map](https://openweathermap.org)
- [Python3.5](https://www.python.org)
- [CX_Freeze](https://anthony-tuininga.github.io/cx_Freeze/)
- [Ubuntu](https://www.ubuntu.com)

#Contributing

I have not yet come up with a code of conduct for contributing, though if you would like to please send a pull request as usual.

#Versioning

Versioning is done within Git using the tag system

Authors

- Bret Cadle - _Initial work_ - [Bretcadle.com](https://www.bretcadle.com)

#License

This project is licensed under the MIT License - see the LICENSE.md file for details.

#Acknowledgments

I'll update this section in the coming weeks as I have gotten an immense amount of help from stackoverflow, reddit, and a few other places and would like to ackowledge anyone's whose solutions help get this clock ticking.

#Known bugs
- app tends to hang when changing font sizes

#Future Changes

###Soon
- Ability to change background and foreground colors
- Ability to change font
- More items for weather display (wind, direction, humidity, etc.)
- Ability to change location for weather information
- Ability to change timezone

###Further Out
- Dynamic resizing of font when resizing window (maybe)
- Ability to hide file menu when in fullscreen
- Fullscreen button (maybe)
- Ability to use an image as the background

#Workarounds

###Location
To modify the location you must change:
```observation = owm.weather_at_place('Seattle, US')```
to read your current location, i.e. 'London, UK' or 'Toronto, CA'

###GMT
Location names used in OWM can be found at https://openweathermap.org.
The time zone can be changed by simply removing "gmtime()" from the source code.
