from django.urls import path
from . import views
urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('AtoZ', views.atoz.as_view(), name='a2z'),
    path('ContactUs', views.contact.as_view(), name='contact'),
    path('fr', views.french.as_view(), name='french'),
    path('AtoZfr', views.atozfr.as_view(), name='a2zfr'),
    path('fr/contact', views.contactfr.as_view(), name='contactfr'),
    path('libsearch', views.libsearch.as_view(), name='libsearch'),
    path('bookacomputer', views.bookacomp.as_view(), name='bookcomp'),
    path('hoursandlocations', views.hoursandloca.as_view(), name='hours&loca'),
    path('getalibrarycard', views.getalibcard.as_view(), name='getalibcard'),
    path('howdoi', views.howdoi.as_view(), name='howdoi'),
    path('jobopportunities', views.jobopps.as_view(), name='jobopps'),
    path('recent_arrivals', views.recent_arrivals.as_view(), name='recent_arrivals'),
    path('placehold', views.user_is_authenticated, name='placehold'),
    path('edit/<int:pk>', views.edit.as_view(), name='edit'),
    path('delete/<int:pk>', views.delete.as_view(), name='delete'),
    path('book/<int:pk>', views.book.as_view(), name='detail'),
    path('form', views.form, name='form'),

]
