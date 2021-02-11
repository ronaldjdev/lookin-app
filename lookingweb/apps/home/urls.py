from django .urls              import path, re_path
from django .conf              import settings
from django .conf .urls.static import static
from apps.home.views import *

urlpatterns = [
    re_path(r'^$'      , IndexCreateView   .as_view(), name='index'  ),
    re_path(r'^index'  , IndexCreateView   .as_view(), name='index'  ),
    re_path(r'^contact', ContactView .as_view(), name='contact'),
    re_path(r'^about'  , AboutView   .as_view(), name='about'  ),
    re_path(r'^pricing', PricingView .as_view(), name='pricing'),
    re_path(r'^404'    , Error404View.as_view(), name='404'    ),
    re_path(r'^warning', WarningView .as_view(), name='warning'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)