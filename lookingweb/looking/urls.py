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


from apps.user.views import UserSecurityView
from django.contrib                 import admin
from django.urls                    import path
from django.contrib.auth.decorators import login_required
from apps  .home   .views           import *
from apps  .login  .views           import *
from apps  .stock  .views           import *
from apps  .user   .views           import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path(''     , IndexCreateView.as_view(), name= 'index' ),
    path('index', IndexCreateView.as_view(), name= 'index' ),
    # Info
    path('about'  , AboutView  .as_view(), name= 'about'  ),
    path('contact', ContactView.as_view(), name= 'contact'),
    # Account
    path('login'  , LoginView        .as_view    (         ), name= 'login'  ),
    path('logout' , login_required   (logout_page          ), name= 'logout' ),
    path('account', login_required   (AccountView.as_view()), name= 'account'),
    path('sign-in', RegistrarUsuarios.as_view    (         ), name= 'sign-in'),
    # User Personal Edit
    path('user-personal'    , UserUpdateView      .as_view(), name= 'user-personal'    ),
    path('user-security'    , UserSecurityView    .as_view(), name= 'user-security'    ),
    path('user-settings'    , UserSettingsView    .as_view(), name= 'user-settings'    ),
    path('user-notification', UserNotificationView.as_view(), name= 'user-notification'),
    path('user-privacy'     , UserPrivacyView     .as_view(), name= 'user-privacy'     ),
    path('user-payment'     , UserPaymentView     .as_view(), name= 'user-payment'     ),
    # Property
    path('warning'      , WarningView     .as_view(), name= 'warning'      ),
    path('add-property' , AddPropertyView .as_view(), name= 'add-property' ),
    path('add-property-1', login_required(AddPropertyView1.as_view()), name= 'add-property-1'),
    path('add-property-2', login_required(AddPropertyView2.as_view()), name= 'add-property-2'),
    path('add-property-3', login_required(AddPropertyView3.as_view()), name= 'add-property-3'),
    path('add-property-4', login_required(AddPropertyView4.as_view()), name= 'add-property-4'),
    path('add-property-5', login_required(AddPropertyView5.as_view()), name= 'add-property-5'),
]
