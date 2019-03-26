from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class Modulo1View(TemplateView):
    template_name = "inicio.html"
