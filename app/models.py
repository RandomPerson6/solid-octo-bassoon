from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

class Book(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField(max_length=2000, blank=True)
    author = models.CharField(max_length=100, default=True)
    Type_choice = (
    ('Book', 'Book'),
    ('eBook', 'eBook'),
    ('DVD Movie', 'DVD Movie'),
    ('CD Music', 'CD Music'),
    ('Audio Book', 'Audio Book'),
    )
    type= models.CharField(max_length=20, choices=Type_choice, default=True)
    genre_choice = (
    ('Mystery Fiction', 'Mystery Fiction'),
    ('Detective and Mystery Stories', 'Detective and Mystery Stories'),
    ('Suspense Fiction', 'Suspense Fiction'),
    ('Historical Fiction', 'Historical Fiction'),
    ('Adventure Fiction', 'Adventure Fiction'),
    ('Fantasy Fiction', 'Fantasy Fiction'),
    ('Christian Fiction', 'Christian Fiction'),
    ('Juvenile Fiction', 'Juvenile Fiction'),
    ('Psycological Fiction', 'Psycological Fiction'),
    ('Horror Fiction', 'Horror Fiction'),
    ('Juvenile Sound Recordings', 'Juvenile Sound Recordings'),
    )
    genre= models.CharField(max_length=30, choices=genre_choice, default=True)
#    = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=genre_choice)
    year = models.IntegerField(max_length=2019, default=True)
    picture = models.TextField()
    entered_lib = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
       db_table = 'books'

class BookActivitie(models.Model):
    book=models.CharField(max_length=100, default=True)
    location_choices= (
    ('New Sudbury Branch', 'New Sudbury Branch'),
    ('Garson Branch', 'Garson Branch'),
    ('Main', 'Main'),
    )
    location=models.CharField(max_length=100, choices=location_choices, default=True)
    user=models.CharField(max_length=100, default=True)
    activity_choices= (
    ('Checked Out', 'Checked Out'),
    ('Returned', 'Returned'),
    )
    activity= models.CharField(max_length=20, choices=activity_choices, default=True)
    date = models.DateTimeField(auto_now_add=True)
