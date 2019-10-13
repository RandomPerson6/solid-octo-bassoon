from django import forms 
#from .views import placehold

class PlaceHoldForm(forms.Form):
    user=forms.CharField()
    book=forms.CharField()
    activity_choices=['Checked Out', 'Returned']
    activity=forms.ChoiceField(widget=forms.Select(activity_choices))
