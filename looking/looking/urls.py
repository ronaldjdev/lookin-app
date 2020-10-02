"""looking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.home.views import IndexView, AboutView, ContactView
from apps.login.views import LoginView, logout_page
from apps.stock.views import AddPropertyView, AddPropertyView1, AddPropertyView2, AddPropertyView3, AddPropertyView4, AddPropertyView5

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('', IndexView.as_view(), name= 'index' ),
    path('index', IndexView.as_view(), name= 'index' ),
    # Info
    path('about', AboutView.as_view(), name= 'about'),
    path('contact', ContactView.as_view(), name= 'contact'),
    # Account
    path('login', LoginView.as_view(), name= 'login'),
    path('logout', logout_page, name= 'logout'),
    # Property
    path('add-property'  , login_required(AddPropertyView .as_view()), name= 'add-property'  ),
    path('add-property-1', login_required(AddPropertyView1.as_view()), name= 'add-property-1'),
    path('add-property-2', login_required(AddPropertyView2.as_view()), name= 'add-property-2'),
    path('add-property-3', login_required(AddPropertyView3.as_view()), name= 'add-property-3'),
    path('add-property-4', login_required(AddPropertyView4.as_view()), name= 'add-property-4'),
    path('add-property-5', login_required(AddPropertyView5.as_view()), name= 'add-property-5'),

]
