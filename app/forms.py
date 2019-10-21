from django import forms 
#from .views import placehold

class PlaceHoldForm(forms.Form):
    user=forms.CharField()
    book=forms.CharField()
    location_choices=['New Sudbury Branch', 'Main', 'Garson Branch']
    location=forms.ChoiceField(widget=forms.Select(location_choices))
    activity_choices=['Checked Out', 'Returned']
    activity=forms.ChoiceField(widget=forms.Select(activity_choices))
    date=forms.DateField()
