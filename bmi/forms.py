from django import forms
from django.forms import ModelForm
from bmi.models import BmiMeasurement, Contact
from django.conf import settings
from django.core.mail import send_mail


class BmiForm(forms.Form):
    """
    height is in meters
    weight is in kg
    """
    #name = forms.CharField(required=False)
    height = forms.FloatField(label="Height in cm:", required=True, min_value=0, )
    weight = forms.FloatField(label="Weight in kg:", required=True, min_value=0)
    #dupa = forms.FloatField(label="dupa in kg:", required=True, min_value=0)

#class BmiMeasurementForm(forms.ModelForm):
    #class Meta:
        #model = BmiMeasurement
      #  fields = [ "height_in_meters", "weight_in_kg", ]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30,required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=30,required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)
 