from django .urls               import path
from django .conf               import settings
from django .conf  .urls.static import static
from        .views              import *

urlpatterns = [
    
    path('account', AccountView.as_view(), name='account' ),
    path('user-personal', AccountView.as_view(), name='account' ),
    path('user-security', AccountView.as_view(), name='account' ),
    path('user-notification', AccountView.as_view(), name='account' ),
    path('user-setting', AccountView.as_view(), name='account' ),
    path('user-privacy', AccountView.as_view(), name='account' ),
    path('user-payment', AccountView.as_view(), name='account' ),
    path('account', AccountView.as_view(), name='account' ),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)