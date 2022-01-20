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

class EditView(UpdateView):
    model = Core
    fields = '__all__'
    template_name = 'coreapp/edit.html'
    pk_url_kwarg = 'pk' #<int:pk> passed over here
    success_url = reverse_lazy('coreapp:comics')

class Delete(DeleteView):
    model = Core
    fields = '__all__'
    template_name = 'coreapp/delete.html'
    pk_ulr_kwarg = 'pk'
    success_url = reverse_lazy('coreapp:comics')