from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

"""
------------------------------------------------------
Agregar hojas al Blog de usuarios 
------------------------------------------------------ 
"""



"""
------------------------------------------------------
Visualizacion de Blog de usuarios
------------------------------------------------------ 
"""


class BlogGridView(TemplateView):
    template_name = "blog/blog-grid.html"

class BlogSingleView(TemplateView):
    template_name = "blog/blog-single.html"