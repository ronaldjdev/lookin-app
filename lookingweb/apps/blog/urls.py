from django.urls              import path
from django.conf              import settings
from django.conf .urls.static import static
from       .views             import *

urlpatterns = [
    path('blog-grid'  , BlogGridView  .as_view(), name='blog-grid'  ),
    path('blog-single', BlogSingleView.as_view(), name='blog-single'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)