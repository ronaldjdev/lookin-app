from django.db                import reset_queries
from django.shortcuts         import render       , redirect
from django.urls              import reverse_lazy
from django.http              import HttpResponseRedirect
from django.views    .generic import TemplateView


# Create your views here.
"""
------------------------------------------------------
Agregar nuevos inmbuebles al stock 
------------------------------------------------------ 
"""


class AddPropertyView(TemplateView):
    template_name = "property/add-property.html"

class AddPropertyView1(TemplateView):
    template_name = "property/add-property-1.html"

class AddPropertyView2(TemplateView):
    template_name = "property/add-property-2.html"

class AddPropertyView3(TemplateView):
    template_name = "property/add-property-3.html"

class AddPropertyView4(TemplateView):
    template_name = "property/add-property-4.html"

class AddPropertyView5(TemplateView):
    template_name = "property/add-property-5.html"

"""
------------------------------------------------------
Visualizaciones de Inmuebles
------------------------------------------------------ 
"""

class PropertyGridView(TemplateView):
    template_name = "property/property-grid.html"

class PropertySingleView(TemplateView):
    template_name = "property/property-single.html"