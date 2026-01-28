from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = 'Вы залогинены'


class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)
