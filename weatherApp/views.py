from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth import logout, login
from .forms import *
import requests
import json

def parser(city_name):
    API_KEY = '96b2ca52ca8ab6039c9e6b09a292e412'
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    response = json.loads(requests.get(URL, headers=headers).text)
    return (response['name'], response['main']['temp'],
            response['main']['feels_like'], response['main']['temp_min'],
            response['main']['temp_max'], response['weather'][0]['icon'],
            response['weather'][0]['description'].title()) if response['cod'] == 200 else False


def index(request):
    context = {'title': 'Main page'}
    return render(request, 'weatherApp/index.html', context=context)

def make_context(cities):
    weather_info = []
    for x in cities:
        res = parser(x)
        city_info = {
            'name': res[0],
            'temp': round(res[1] - 272.15),
            'feels_like': round(res[2] - 272.15),
            'temp_min': round(res[3] - 272.15),
            'temp_max': round(res[4] - 272.15),
            'icon': f'http://openweathermap.org/img/w/{res[5]}.png',
            'description': res[6]
        }
        weather_info.append(city_info)
    return {'title': 'Weather page', 'weathers': weather_info}

def weather_page(request):
    city = request.GET.get('city', False)
    cities = CardCityWeather.objects.filter(user=request.user)
    if city:
        if parser(city):
            if parser(city)[0] not in [x.city_name for x in cities]:
                CardCityWeather.objects.create(city_name=parser(city)[0], user=request.user)
            cities = CardCityWeather.objects.filter(user=request.user)
            return render(request, 'weatherApp/weather.html', context=make_context(cities))
        else:
            context = make_context(cities)
            context['message'] = 'Error! Invalid city name'
            return render(request, 'weatherApp/weather.html', context=context)
    else:
        return render(request, 'weatherApp/weather.html', context=make_context(cities))

def delete_card(request):
    res = request.GET.get('city_name', None)
    if res:
        c = CardCityWeather.objects.get(city_name=res, user=request.user)
        c.delete()
        return redirect('cards')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'weatherApp/login.html'

    def get_success_url(self):
        return reverse_lazy('cards')

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'weatherApp/sign_up.html'
    success_url = reverse_lazy('cards')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('cards')

def logout_method(request):
    logout(request)
    return redirect('home')