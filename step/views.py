from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class About(TemplateView):
    template_name= 'about.html'
class Contact(TemplateView):
    template_name= 'contact.html'
class Index(TemplateView):
    template_name= 'index.html'
