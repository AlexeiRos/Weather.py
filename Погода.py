import pyowm
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
city = input('Какой город Вас интересует?: ')

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temp = w.temperature('celsius')["temp"]
hym = w.humidity #Влажность
wind = w.wind() #Скорость ветра
clouds = w.clouds #Состояние облаков %
print("В указаном городе : " + city + ' ' + str(temp) + ' ' + 'По цельсию' + ',' + w.detailed_status)
print('Влажность : ' + ' ' + str(int(hym)) + ' ' + '%' + ';' + 'Облака: ' + ' ' + str(clouds) + ' %')
print('Скорость ветра {Скорость, Угол ветра} : ' + ' ' + str(wind))