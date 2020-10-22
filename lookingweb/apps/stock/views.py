from django.db                import reset_queries
from django.shortcuts         import render       , redirect
from django.urls              import reverse_lazy
from django.http              import HttpResponseRedirect
from django.views    .generic import TemplateView


# Create your views here.


class WarningView(TemplateView):
    template_name = "account/aviso.html"

class AddPropertyView(TemplateView):
    template_name = "add/add-property.html"

class AddPropertyView1(TemplateView):
    template_name = "add/add-property-1.html"

class AddPropertyView2(TemplateView):
    template_name = "add/add-property-2.html"

class AddPropertyView3(TemplateView):
    template_name = "add/add-property-3.html"

class AddPropertyView4(TemplateView):
    template_name = "add/add-property-4.html"

class AddPropertyView5(TemplateView):
    template_name = "add/add-property-5.html"

