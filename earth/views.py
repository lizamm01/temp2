from django.shortcuts import render
from .models import *

def index(request):
    s = "<h1> Mamlakatlar </h1> \n"
    ma = Country.objects.all()
    sh = City.objects.all()
    context = {
        'ma': ma,
        'title': "Mamlakatlar nomi",
        'sh': sh,
    }
    return render(request, 'mamlakat.html',context=context)

def country(request,pk):
    s = "<h1> Mamlakatlar </h1> \n"
    ma = Country.objects.all()
    sh = City.objects.filter(country=pk)
    context = {
        'ma': ma,
        'title': "Mamlakatlar nomi",
        'sh': sh,
    }
    return render(request, 'country.html', context=context)

