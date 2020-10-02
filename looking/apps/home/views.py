from django.shortcuts         import render      , redirect
from django.http              import HttpResponse
from django.views    .generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "info/contact.html"


class AboutView(TemplateView):
    template_name = "info/about.html"


class AddPropertyView(TemplateView):
    template_name = "add/add-property.html"


