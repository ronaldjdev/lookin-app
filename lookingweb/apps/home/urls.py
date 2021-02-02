from django .urls              import path
from django .conf              import settings
from django .conf .urls.static import static
from apps.home.views import *

urlpatterns = [
    path(''       , IndexView   .as_view(), name='index'  ),
    path('index'  , IndexView   .as_view(), name='index'  ),
    path('contact', ContactView .as_view(), name='contact'),
    path('about'  , AboutView   .as_view(), name='about'  ),
    path('pricing', PricingView .as_view(), name='pricing'),
    path('404'    , Error404View.as_view(), name='404'    ),
    path('warning', WarningView .as_view(), name='warning'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)