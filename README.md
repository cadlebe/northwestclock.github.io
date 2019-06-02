# NWClock v 0.2.9

This is a simple clock that displays UTC and current temp. It currently has a settings menu for changing the fontsize for the clock, date, and weather.

## Prerequisites

What you need on your system in order to install:

- Linux or Windows
- Python 3.7+ (Python 3.5+ will probably work)
- x86 or ARM processor (see Starting Clock: From Source)

## Starting Clock

### Run Binary:
1. Download the [binary file](https://github.com/cadlebe/northwestclock.github.io/releases) for your os/processor. 
2. Extract the .zip file or file to any location that you have read-write access.
3. Navigate to the newly extracted directory.
4. Double-Click on clock application.

### From Source:

##### BASH (Linux)

```` bash
git clone git@github.com:cadlebe/northwestclock.github.io.git nwclock
cd nwclock
virtualenv --python="/path/to/python3.7.x" env
source env/bin/activate
pip install pipreqs
pipreqs /path/to/nwclock
python build.py
````

##### PowerShell (windows)

```` Powershell
git clone git@github.com:cadlebe/northwestclock.github.io.git nwclock
cd nwclock
virtualenv --python="/path/to/python3.7.x" env
./env/Scripts/activate.ps1
pip install pipreqs
pipreqs /path/to/nwclock
python build.py
````

- Run the binary from dist/northwest-clock-X_X_x

#### Running in Fullscreen

To run northwest-clock in fullscreen:

```` bash
northwest-clock --fullscreen
````

Otherwise pressing F11 once clock is running will suffice.

## Configuration

Configuration is done via both the in-app settings menu and the config file. The file is located in ~/.config/northwest-clock/config.ini

Default configuration settings:

````
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

[WEATHER]
weatherlocation = Seattle, US
````

## Weather information

### Open Weather Map API Key

Weather information will only be available if you obtain a free API-Key from Open Weather Map.

[Sign up at OWM](https://home.openweathermap.org/users/sign_up)

Once you have your key:
1. Click 'edit' -> settings
2. Enter API key
3. Press configure
4. Cose then reopen clock.
5. The temperature should be displayed at the bottom of the clock.

WARNING: If you reset the configuration to default then the API key will need to be reentered. Please backup your config!

### Weather Location

If you have gotten an API key from openweather you can go into the config, or the settings and changed the weather location. Just put in your city as so "Cityname, US". You can also use your zip code i.e. "98584, US" and it will default to the nearest city available in openweather.


## Full List of Timezones

Timezones follow the 'county'/'city' format and are limited to a handful of cities in each timezone.

[Timezones](http://worldtimeapi.org/timezones)

# Built with

- [VSCode](https://code.visualstudio.com)
- [TKinter](https://wiki.python.org/moin/TkInter)
- [Open Weather Map](https://openweathermap.org)
- [Python3.5](https://www.python.org)
- [pyinstaller](http://pyinstaller.readthedocs.io/en/stable/index.html#)
- [Ubuntu](https://www.ubuntu.com)
- [Manjaro](https://www.majaro.org)

# Contributing

I have not yet come up with a code of conduct for contributing, though if you would like to please send a pull request as usual or email me directly with any ideas.

# Authors

- Bret Cadle - _Initial work_ - [Bretcadle.com](https://www.bretcadle.com)

# License

This project is licensed under the GPL-3.0+ License - see the LICENSE.md file for details.

# Future Changes

### Soon
- Ability to change font
- More items for weather display (wind, direction, humidity, etc.)

<p style="text-align: center;">Copyright &copy2017 Bret Cadle</p>
