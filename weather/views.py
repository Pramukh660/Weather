from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json

def index1(request):
    return render(request, 'index.html')

def index2(request):
    return HttpResponse("<h1>hello</h1>")


def index(request):
    if request.method != 'POST':
       return render(request, "index.html")
    if request.method == 'POST':
        city = request.POST['city']
        if city == 'banglore' or city == 'Banglore' or city == 'bangalore' or city == 'Bangalore':
            city = 'bengaluru'
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                    city + '&units=metric&appid=33e29300b01a9e8984fd89c44a5b99ad').read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
    else:
        data = {}
    return render(request, "index.html", data)
