from django.views    .generic import TemplateView, CreateView
from django.shortcuts import render
from apps.user.models import Usuarios
from apps.stock.forms import InmuebleForm

"""
------------------------------------------------------
Visualizacion estandar
------------------------------------------------------ 
"""
class IndexCreateView(CreateView):
    model = Usuarios
    form_class = InmuebleForm
    template_name = "index.html"

#Vista de Inicio
class IndexView(TemplateView):
    template_name = "index.html"

#Vista de contatoc
class ContactView(TemplateView):
    template_name = "info/contact.html"

# Vista de informacion de la pagina
class AboutView(TemplateView):
    template_name = "info/about.html"


# Vista de precios
class PricingView(TemplateView):
    template_name = "info/pricing.html"

# Error 404
class Error404View(TemplateView):
    template_name = "404.html"

# Vista Accion invalida 
class WarningView(TemplateView):
    template_name = "info/warning.html"

