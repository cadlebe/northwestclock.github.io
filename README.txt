NWClock
Copyright 2017 Bret Cadle

This is a simple clock that displays UTC and current temp.

To modify the location you must change:

    32      observation = owm.weather_at_place('Seattle, US')

to read your current location, i.e. 'London, UK' or 'Toronto, CA'

Location names used in OWM can be found at https://openweathermap.org.

The time zone can be changed by simply removing "gmtime()" from the source code.