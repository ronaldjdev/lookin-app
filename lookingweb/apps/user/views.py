from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib  .auth.models import User
from django.views    .generic     import TemplateView     , CreateView, UpdateView
from       .forms                 import PerfilForm
from       .models                import Usuarios
# Create your views here.


#================================================================
#                   Vistas control de cuentas
#================================================================

class AccountView(TemplateView):
    template_name = "users/account.html"


class UserNotificationView(TemplateView):
    template_name = "users/user-notification.html"


class UserPaymentView(TemplateView):
    template_name = "users/user-payment.html"


class UserPersonalView(UpdateView):
    model = Usuarios
    form_class = PerfilForm
    template_name = "users/user-personal.html"
    success_url = reverse_lazy("user-personal")

    def get_object(self):
        return get_object_or_404 (User)

    def form_valid(form) :
        form.save()
        return super().form_valid(form)




    


class UserPrivacyView(TemplateView):
    template_name = "users/user-privacy.html"


class UserSecurityView(TemplateView):
    template_name = "users/user-security.html"


class UserSettingView(TemplateView):
    template_name = "users/user-settings.html"






#================================================================
#                   Vistas agentes inmobiliarios
#================================================================
class AgentsGridView(TemplateView):
    template_name = "agents/agents-grid.html"


class AgentSingleView(TemplateView):
    template_name = "agents/agent-single.html"

