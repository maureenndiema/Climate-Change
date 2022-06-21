from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    appid ='ffef4e2d3fc816c6a280afaf80fe6d74'
    URL ='https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'Nairobi','appid':appid, 'lat':'lat', 'lon':'lon', 'units':'metric' }
    r=requests.get()


    return render(request, 'weather/index.html',{'num': num})