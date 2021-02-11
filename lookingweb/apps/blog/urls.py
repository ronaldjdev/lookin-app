from django.urls              import re_path
from django.conf              import settings
from django.conf .urls.static import static
from       .views             import *

urlpatterns = [
    re_path(r'^blog-grid'  , BlogGridView  .as_view(), name='blog-grid'  ),
    re_path(r'^blog-single', BlogSingleView.as_view(), name='blog-single'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)