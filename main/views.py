from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *

# Create your views here.
class HomePage(TemplateView):
    template_name = 'main/home.html'

class ServicioList(ListView):
    model = Servicio

class ServicioDetail(DetailView):
    model = Servicio

class ServicioCreate(CreateView):
    model = Servicio
    fields = '__all__'
    template_name_suffix = '_create_form'

class ServicioUpdate(UpdateView):
    model = Servicio
    fields = '__all__'
    template_name_suffix = '_update_form'

class ServicioDelete(DeleteView):
    model = Servicio
    fields = ['cliente', 'motor', 'mantenimiento']
    success_url = reverse_lazy('servicio-list')
