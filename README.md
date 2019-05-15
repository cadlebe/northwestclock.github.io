# NWClock v 0.2.9a
### Copyright 2017 Bret Cadle

This is a simple clock that displays UTC and current temp. It currently has a settings menu for changing the fontsize for the clock, date, and weather.

## Prerequisites

What you need on your system in order to install:

- Ubuntu 12.04 or later
- At least a Core i3 processor
- 256mb RAM

## Installing

### Manual Installation
1. Download the dist/clock file for your operating system
2. Extract the .zip file or file to any location that you have read-write access
3. Navigate to the newly extracted directory
4. Double-Click on clock application

### If using pc as a dedicated clock display

1. Copy /usr/bin/northwest-clock/northwest-clock.service to /etc/systemd/system/
2. Open northwest-clock.service:
  ```bash
  vim /etc/systemd/northwest-clock.service
  ```
3. Change <username> to username that will be running clock as a service, (it is not recommend to run as root.)
4. Save and exit file
5. Enable service:
  ```Bash
  sudo systemctl enable northwest-clock.service
  ```
7. Start service:
  ```Bash
  sudo systemctl start northwest-clock.service
  ```
8. Clock will now open full screen and will do so when OS is started and logged in.
9.  A Raspberry Pi is recommended as a dedicated display computer, attach to screen of choice.

### Weather information

In order to have weather information displayed you will need to get an API key from [Open Weather Map](https://openweathermap.org)
The free tier will give you what you need for the current version of the clock.
Once you have your key:
1. Click 'edit' -> settings
2. Enter API key
3. Press configure
4. Cose then reopen clock.
5. The temperature should be displayed at the bottom of the clock.

## Configuration

A big recent change is the configuration. It is installed in ~/.config/northwest-clock/config.ini

By default it will look like so:

[FONTSIZES]
date = 60
clock = 100
weather = 50
title = 60

[COLORS]
titlebackground = #00541c
titleforeground = #141414
datebackground = #212121
dateforeground = #cecece
clockbackground = #212121
clockforeground = #cecece
weatherbackground = #212121
weatherforeground = #cecece

[FIRSTRUN]
firstrun = false

[TITLETEXT]
titletext = Northwest Clock

[APIKEY]
openweather api key = Get an API key at OWM, see README.

[TIMEZONE]
timezone = UTC

# Full List of Timezones

[Timezones](http://worldtimeapi.org/timezones)

# Built with

- [VSCode](https://code.visualstudio.com)
- [TKinter](https://wiki.python.org/moin/TkInter)
- [Open Weather Map](https://openweathermap.org)
- [Python3.5](https://www.python.org)
- [pyinstaller](http://pyinstaller.readthedocs.io/en/stable/index.html#)
- [Ubuntu](https://www.ubuntu.com)

# Contributing

I have not yet come up with a code of conduct for contributing, though if you would like to please send a pull request as usual or email me directly with any ideas.

# Authors

- Bret Cadle - _Initial work_ - [Bretcadle.com](https://www.bretcadle.com)

# License

This project is licensed under the MIT License - see the LICENSE.md file for details.

# Acknowledgments

I'll update this section in the coming weeks as I have gotten an immense amount of help from stackoverflow, reddit, and a few other places and would like to acknowledge anyone's whose solutions help got this clock ticking.

# Known bugs
- app tends to hang when changing font sizes

# Future Changes

### Soon
- Ability to change background and foreground colors
- Ability to change font
- More items for weather display (wind, direction, humidity, etc.)
- Ability to change location for weather information
- Ability to change timezone

# Workarounds
## (NOTE: These workarounds only work if you download and build the source code using pyinstaller)

### Location
To modify the location you must change:
```observation = owm.weather_at_place('Seattle, US')```
to read your current location, i.e. 'London, UK' or 'Toronto, CA'

### GMT
Location names used in OWM can be found at https://openweathermap.org.
The time zone can be changed by simply removing "gmtime()" from the source code.
