from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Book,BookActivitie 

class MyUserCreationForm(UserCreationForm):
    username = forms.RegexField(
        label='Username',
        max_length=14,
        regex=r'^[0-9]+$',
        help_text = 'Required. 14 digits or fewer.',
#        error_message = 'This value must contain only digits'
    )

class MyUserChangeForm(UserChangeForm):
    username = forms.RegexField(
        label='Username',
        max_length=14,
        regex=r'^[0-9]+$',
        help_text = 'Required. 14 digits or fewer.',
#        error_message = 'This value must contain only digits'
    )

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'entered_lib', 'modified', 'type')
    list_filter = ['entered_lib']
    search_fields = ['title', 'author']
admin.site.register(Book, BooksAdmin)
admin.site.unregister(User)
admin.site.register(BookActivitie)
admin.site.register(User, MyUserAdmin)
