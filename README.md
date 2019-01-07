# NWClock v 0.2.6
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

### Using Debian Package

1. Download the .deb file.
2. Make the package executable:
  ```Bash
  sudo chmod +x <package name>
  ```
3. Then:
  ```Bash
  sudo apt-get install ./<package name>
  ```
5. ```northwest-clock --version``` in terminal to verify installation.
6. ```northwest-clock``` to open clock.

### Using pyinstaller

1. Download source
2. Run pyinstaller using prefered method
  * Prefered method
  ```python
  pyinstaller -F -n NAME /src/clock.py
  ```
3. Move the binary created from this process to desired location

### If using pc as a dedicated clock display

1. Copy /usr/bin/northwest-clock/northwest-clock.service to /etc/systemd/system/
2. Open northwest-clock.service:
  ```bash
  vim /etc/systemd/northwest-clock.service
  ```
3. Change <username> to username that will be running clock as a service
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

### Further Out
- Dynamic resizing of font when resizing window (maybe)
- Ability to hide file menu when in fullscreen
- Fullscreen button (maybe)
- Ability to use an image as the background

# Workarounds
## (NOTE: These workarounds only work if you download and build the source code using pyinstaller)

### Location
To modify the location you must change:
```observation = owm.weather_at_place('Seattle, US')```
to read your current location, i.e. 'London, UK' or 'Toronto, CA'

### GMT
Location names used in OWM can be found at https://openweathermap.org.
The time zone can be changed by simply removing "gmtime()" from the source code.
