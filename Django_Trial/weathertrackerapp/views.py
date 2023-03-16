from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.views import View
from .forms import QueryForm, LocationForm


# Create your views here.

class Index(View):
    def get(self, request):
        form = LocationForm()
        return render(request, 'index.html', {'form':form}) 
    def post(self, request):
        form = LocationForm(request.POST)
        if form.is_valid():
            
            submission = form.cleaned_data['location']
            url = "http://api.weatherapi.com/v1/forecast.json?key=25d64afd97824d6bad1185656231503&q=" + submission + "&days=7&aqi=no&alerts=no'"
            response=requests.get(url).json()
            return render(request, 'index.html', {'form':form, 'response':response}) 

""" def APIresponse(request):
    form = QueryForm()
    response=requests.get('http://api.weatherapi.com/v1/forecast.json?key=25d64afd97824d6bad1185656231503&q=77372&days=7&aqi=no&alerts=no').json()
    args = {'form': form, 'response': response}
    if request.method == 'POST':
            form = QueryForm(request.POST)
            if form.is_valid():
                form.save()
    return render(request, 'APIresponse.html', args)
     """