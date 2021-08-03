from django.http.response import HttpResponse
from django.shortcuts import render
import requests, json
import os

# Create your views here.
def home(response):
    r = requests.get('https://data.calgary.ca/resource/ikeb-n5bc.json')
    j = json.loads(r.text)
    dict = {}

    googleAPI = os.environ.get("GOOGLEAPI")

    dir = response.GET.get('dir')
    type = response.GET.get('type')

    if dir is None:
        dir = 'A'
    if type is None:
        type = '@'

    lat = []
    lng = []
    adr = []
    typ = []
    
    for i in range(len(j)):
        if j[i].get('orientation') is not None and j[i].get('location_detail') is not None:
            if dir == 'A' and type == '@':
                lat.append(j[i].get('latitude'))
                lng.append(j[i].get('longitude'))
                adr.append(j[i].get('location_detail'))
                typ.append(j[i].get('type_description'))
            elif dir in j[i].get('orientation'):
                lat.append(j[i].get('latitude'))
                lng.append(j[i].get('longitude'))
                adr.append(j[i].get('location_detail'))
                typ.append(j[i].get('type_description'))
            elif type.upper() in j[i].get('type_description'):
                lat.append(j[i].get('latitude'))
                lng.append(j[i].get('longitude'))
                adr.append(j[i].get('location_detail'))
                typ.append(j[i].get('type_description'))

    lists = zip(lat, lng, adr, typ)

    return render(response, 'main/home.html', {'dict':dict, 'lists':lists, 'googleAPI':googleAPI})