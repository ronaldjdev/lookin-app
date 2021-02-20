from django .urls               import re_path, path
from django .conf               import settings
from django .conf  .urls.static import static
from        .views              import *



urlpatterns = [
    
    #================================================================
    #                      URLs GESTION DE CUENTAS
    #===============================================================     =
    re_path(r'^account' , AccountView .as_view(), name                   ='account' ),
    re_path(r'^user-notification' , UserNotificationView .as_view(), name='user-notification' ),
    re_path(r'^user-payment' , UserPaymentView .as_view(), name          ='user-payment' ),
    re_path(r'^user-personal/<int:pk>/' , UserPersonalView .as_view(), name   ='user-personal' ),
    re_path(r'^user-privacy' , UserPrivacyView .as_view(), name          ='user-privacy' ),
    re_path(r'^user-security' , UserSecurityView .as_view(), name        ='user-security' ),
    re_path(r'^user-settings' , UserSettingView .as_view(), name         ='user-settings' ),
    

    #================================================================
    #                     URLs aGENTES INMOBILIARIOS
    #================================================================

    re_path(r'^agents-grid' , AgentsGridView .as_view(), name='agents-grid' ),
    re_path(r'^agent-single', AgentSingleView.as_view(), name='agent-single'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
