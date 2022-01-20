from django.shortcuts import render
from .models import Core
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'coreapp/index.html'

class SingleView(DetailView):
    model = Core
    template_name = 'coreapp/single.html'
    context_object_name = 'comicbook'

class PostView(ListView):
    model = Core
    template_name = 'coreapp/comics.html'
    context_object_name = 'comics_list'

class AddView(CreateView):
    model = Core
    fields = '__all__' #taking all fields from DB
    template_name = 'coreapp/add.html'
    context_object_name = 'add'
    success_url = reverse_lazy('coreapp:comics') #taking users back to comics crud view
