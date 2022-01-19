from django.shortcuts import render
from .models import Core
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'coreapp/index.html'

class SingleView(DetailView):
    model = Core
    template_name = 'coreapp/single.html'
    context_object_name = 'comicbook'