from django import forms
from django.forms import ModelForm
from .models import Venue

#create a venue form
class VenueForm(ModelForm):
    class Meta:
        model=Venue
        # field = '__all__'
        fields = ('name','address','postcode','phone','web','email')
        labels={
            'name': 'entry your venue here',
            'address': '',
            'postcode': '',
            'phone': '',
            'web': 'wwweb',
            'email': 'eeemail',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'address'}),
            'postcode':forms.TextInput(attrs={'class':'form-control','placeholder':'postcode'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),
            'web':forms.URLInput(attrs={'class':'form-control','placeholder':'web'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
        }
