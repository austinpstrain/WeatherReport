from django import forms
from django.forms import ModelForm
from .models import Query

class LocationForm(forms.Form):
    location = forms.CharField(max_length=50)


class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = ('location',)
        labels = {
            'location':'Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name.'
        }
    
   