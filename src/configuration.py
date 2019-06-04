import configparser
import os.path
import getpass

class Configuration(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file = "config.ini"
        self.fontsize = 'FONTSIZES'
        self.color = 'COLORS'
        self.first_run = 'FIRSTRUN'
        self.titletext = 'TITLETEXT'
        self.api_key = 'APIKEY'
        self.timezone = 'TIMEZONE'
        self.weatherlocation = 'WEATHER'
        self.user = getpass.getuser()
        self.path_to_config = str("/home/" + self.user + "/.config/northwest-clock/")

    def __str__(self):
        return str(self.path_to_config + self.config)

    def SetDefaultConfigFile(self):
        if os.path.isdir(self.path_to_config) == False:
            os.mkdir(self.path_to_config)
        if os.path.isfile(self.path_to_config + self.config_file) == False:
            f = open(self.path_to_config + self.config_file, "w+")
            f.close
        self.config[self.fontsize] = {'date': '60',
                               'clock': '100',
                               'weather': '50',
                               'title': '60'}
        self.config[self.color] = {'titlebackground': '#00541c',
                                 'titleforeground': '#141414',
                                 'datebackground': '#212121',
                                 'dateforeground': '#cecece',
                                 'clockbackground': '#212121',
                                 'clockforeground': '#cecece',
                                 'weatherbackground': '#212121',
                                 'weatherforeground': '#cecece'}
        self.config[self.first_run] = {'firstrun': 'true'}
        self.config[self.titletext] = {'titletext': 'Northwest Clock'}
        self.config[self.api_key] = {'openWeather api key': 'Get an API key at OWM, see README.'}
        self.config[self.timezone] = {'timezone': 'UTC'}
        self.config[self.weatherlocation] = {'weather location': 'Seattle, US'}
        self.SetConfigFile()

    def ReadConfigFile(self):
        self.config.read(self.path_to_config + self.config_file)

    def SetConfigFile(self):
        with open(self.path_to_config + self.config_file, 'w') as config_file:
            self.config.write(config_file)
        config_file.close()

    def SetFontSize(self, label, size):
        self.config.set('FONTSIZES', label, size)
        self.SetConfigFile()

    def setColor(self, label, color):
        self.config.set('COLORS', label, color)
        self.SetConfigFile()

    def setFirstRun(self, option):
        self.config.set('FIRSTRUN', 'firstrun', option)
        self.SetConfigFile()

    def setTitleText(self, option):
        self.config.set(self.titletext, 'titletext', option)
        self.SetConfigFile()

    def setApiKey(self, option):
        self.config.set(self.api_key, 'openWeather api key', option)
        self.SetConfigFile()

    def setTimezone(self, option):
        self.config.set(self.timezone, 'timezone', option)
        self.SetConfigFile()
    
    def setWeatherLocation(self, option):
        self.config.set(self.weatherlocation, 'weather location', option)
        self.SetConfigFile()

    def getFontsize(self, label):
        return self.config.get('FONTSIZES', label)

    def getColor(self, label):
        return self.config.get('COLORS', label)

    def getFirstRun(self):
        return self.config.getboolean(self.first_run, 'firstrun')

    def getTitleText(self):
        title_text = self.config.get(self.titletext, 'titletext')
        return title_text
    
    def getApiKey(self):
        api_key = self.config.get(self.api_key, 'openweather api key')
        return api_key

    def getTimezone(self):
        timezone = self.config.get(self.timezone, 'timezone')
        return timezone
    
    def getWeatherLocation(self, option):
        weatherlocation = self.config.get(self.weatherlocation, 'weather location')
        return weatherlocation