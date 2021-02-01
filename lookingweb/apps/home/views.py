from django.views    .generic import TemplateView, CreateView
from django.shortcuts import render
from django.views.defaults import page_not_found
from apps.user.models import Usuarios
from apps.stock.forms import InmuebleForm



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


def custom_error_404(request):
 
    return render(request,'info/404.html')




