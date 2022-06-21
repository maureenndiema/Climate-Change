from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    appid ='ffef4e2d3fc816c6a280afaf80fe6d74'
    URL ='https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'Nairobi','appid':appid, 'lat':'lat', 'lon':'lon', 'units':'metric' }
    r=requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main'][0]['temp']
    


    return render(request, 'weather/index.html',{'num': num})