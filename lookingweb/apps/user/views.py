from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


#================================================================
#                   Vistas control de cuentas
#================================================================

class AccountView(TemplateView):
    template_name = "users/account.html"


class UserNotificationView(TemplateView):
    template_name = "user/user-notification.html"


class UserPaymentView(TemplateView):
    template_name = "user/user-payment.html"


class UserPersonalView(TemplateView):
    template_name = "user/user-personal.html"


class UserPrivacyView(TemplateView):
    template_name = "user/user-privacy.html"


class UserSecurityView(TemplateView):
    template_name = "user/user-security.html"


class UserSettingView(TemplateView):
    template_name = "user/user-setting.html"






#================================================================
#                   Vistas agentes inmobiliarios
#================================================================
class AgentsGridView(TemplateView):
    template_name = "agents/agents-grid.html"


class AgentSingleView(TemplateView):
    template_name = "agents/agent-single.html"

