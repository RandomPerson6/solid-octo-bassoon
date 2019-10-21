from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Book, BookActivitie
from django.db.models import Q
from django.core.paginator import Paginator
import datetime
from . forms import PlaceHoldForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

#def placehold(request):
#    if request.method == 'POST':
#        if request.POST.get('book') and request.POST.get('user'):
#        placehold = PlaceHoldForm(request.POST)
#        user= request.POST.get('user')
#        book= request.POST.get('book')
#        activity= request.POST.get('activity','')
#        data = BookActivitie(activity = activity, user = user, book = book)
#        data.save()
#        return HttpResponseRedirect(reverse('placehold'))
#    else:
#        placehold = PlaceHoldForm()
#    return render(request, 'app/enterdata.html', {'placehold':placehold,})
   #     else:
    #        return render(request, 'app/loggedin.html')

class home(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/home.html'
class atoz(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/a2z.html'
class contact(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/contact.html'
class french(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/french.html'
class atozfr(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/atozfr.html'
class contactfr(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/contactfr.html'
class libsearch(ListView):
    model = Book
    context_object_name = 'article'
    template_name = 'app/libsearch.html'
  
    #this is where the search starts:
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(Q(title__icontains=query) | Q(description=query))

        return object_list 
###    def get_queryset(self):
###        query = self.request.GET.get('q')
###        object_list = Book.objects.filter(Q(title__icontains=query) | Q(description=query))

###        return object_list 
       # paginator(object_list)
class recent_arrivals(ListView):
    template_name = 'app/recent_arrival.html'
    model = Book
    def get_queryset(self):
        now = datetime.date.today()
        start_week = now - datetime.timedelta(days=7)
        object_list = Book.objects.filter(entered_lib__range=[start_week, now])
        return object_list 

class bookacomp(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/bookacomp.html'
class hoursandloca(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/hoursandloca.html'
class getalibcard(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/getalibcard.html'
class howdoi(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/howdoi.html'
class jobopps(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/jobopps.html'
class user_is_authenticated(ListView):
    model = Book 
    context_object_name = 'article'
    template_name = 'app/login.html'

class edit(UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'type', 'genre', 'year', 'picture']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')

class delete(DeleteView):
    model = Book
    success_url = reverse_lazy('home')

class book(DetailView):
    model = Book
    context_object_name = 'book'
    template = "app/book_detail.html"

def form(request):
    if request.method == 'POST':
        form = PlaceHoldForm(request.POST)
        user = request.POST.get('user', '')
        book = request.POST.get('book', '')
        location = request.POST.get('location', '')
        activity = request.POST.get('activity', '')
        date = request.POST.get('date', '')
        data = BookActivitie(user = user, book = book, location = location, activity = activity, date = date)
        data.save()
        return HttpResponseRedirect(reverse('form'))
    else:
        form = PlaceHoldForm()
    return render(request, 'app/libsearch.html', {'form':form,})
