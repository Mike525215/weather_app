from django.shortcuts import render, HttpResponse, redirect, Http404
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
import requests
import json
def city_handler(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f0e74799577e63a71b8ca26906ad4b4f'
    r = requests.get(url.format(city)).text
    r = json.loads(r)
    try:
        city_data = {
            'city': r['name'],
            'temprature':  round((float(r['main']['temp']) - 32) / 1.8),
            'weather': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
    except KeyError:
        city_data = False
    return city_data
def start_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            obj = City.objects.filter(user=request.user)
            cities = [city_handler(x.name) for x in obj]
            context_data = {'title': 'Start page', 'form': AddCityForm(), 'cities': cities}
            return render(request, 'weather/index.html', context=context_data)
        else:
            context_data = {'title': 'Start page'}
            return render(request, 'weather/index.html', context=context_data)
    else:
        if city_handler(request.POST['name']):
            form = AddCityForm(request.POST)
            city = form.save(commit=False)
            city.user = request.user
            city.name = city_handler(request.POST['name'])['city']
            city.save()
            return redirect('start_page')
        else:
            obj = City.objects.filter(user=request.user)
            names = [x.name for x in obj]
            cities = [city_handler(x) for x in names]
            context_data = {'title': 'Start page', 'form': AddCityForm(), 'cities': cities, 'error': 'Invalid name city'}
            return render(request, 'weather/index.html', context=context_data)

def delete_city(request, city_name):
    city = City.objects.get(user=request.user, name=city_name)
    city.delete()
    return redirect('start_page')



def sign_up_user(request):
    if request.method == 'GET':
        context_data = {'title': 'Sign up', 'form': SignUpForm()}
        return render(request, 'weather/sign_up_user.html', context=context_data)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('start_page')
            except IntegrityError:
                return redirect('login_user')
        else:
            context_data = {'title': 'Sign up', 'form': SignUpForm(), 'error': 'Password are not match!'}
            return render(request, 'weather/sign_up_user.html', context=context_data)
def logout_user(request):
    logout(request)
    return redirect('start_page')
def login_user(request):
    if request.method == 'GET':
        context_data = {'title': 'Login', 'form': LoginForm()}
        return render(request, 'weather/login_user.html', context=context_data)
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context_data = {'title': 'Login', 'form': LoginForm(), 'error': 'Username or password is not correct!'}
            return render(request, 'weather/login_user.html', context=context_data)
        else:
            login(request, user)
            return redirect('start_page')

