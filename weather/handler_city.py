import requests
import json
def city_handler(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f0e74799577e63a71b8ca26906ad4b4f'
    r = requests.get(url.format(city)).text
    r = json.loads(r)
    city_data = {
        'city': r['name'],
        'temprature':  round((float(r['main']['temp']) - 32) / 1.8),
        'weather': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }
    return city_data
print(city_handler('mdksnjsngjsnge'))

