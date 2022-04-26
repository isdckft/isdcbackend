from django import forms
from django.core import validators
from .models import PageType, WebPage

def own_validator(value):
    if value[0].upper() =='X':
        raise forms.ValidationError("Do not do that: Name starting with X?")
    if value == 'aaa':
        raise forms.ValidationError("Invalid name")

class PageTypeForm(forms.ModelForm):
    class Meta:
        model = PageType
        fields = '__all__'

class WebPageForm(forms.ModelForm):
  
    name = forms.CharField(max_length=128,validators=[own_validator])
    botcatcher = forms.CharField(required =  False, widget = forms.HiddenInput, 
                                validators=[validators.MaxLengthValidator(0)])
    class Meta:  
        model = WebPage
        fields = '__all__'

        widgets = {
             'about': forms.Textarea,
        }


