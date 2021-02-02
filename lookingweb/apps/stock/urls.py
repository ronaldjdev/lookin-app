from django .urls              import path
from django .conf              import settings
from django .conf .urls.static import static
from .views import *

urlpatterns = [
    # Agregar Inmuebles
    path('add-property', AddPropertyView.as_view(), name='add-property' ),
    path('add-property-1', AddPropertyView1.as_view(), name='add-property-1' ),
    path('add-property-2', AddPropertyView2.as_view(), name='add-property-2' ),
    path('add-property-3', AddPropertyView3.as_view(), name='add-property-3' ),
    path('add-property-4', AddPropertyView4.as_view(), name='add-property-4' ),
    path('add-property-5', AddPropertyView5.as_view(), name='add-property-5' ),
    # Visualizador de Inmuebles
    path('property-grid', PropertyGridView.as_view(), name='property-grid' ),
    path('property-single', PropertySingleView.as_view(), name='property-single' ),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)