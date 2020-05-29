from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .context_processors import config


def error_page(request, code, message, details):
    template = f'adminlte_full/error_{code // 100}xx.html'
    context = {
        'status_code': code, 'status_message': message, 'details': details,
    }
    return render(request, template, context, status=code)


@requires_csrf_token
def handler400(request, exception):
    return error_page(
        request, 400, 'Bad Request',
        'The browser (or proxy) sent a request that this server could not understand.'
    )


@requires_csrf_token
def handler403(request, exception):
    return error_page(
        request, 403, 'Forbidden',
        "You don't have the permission to access the requested resource."
        "It is either read-protected or not readable by the server."
    )


@requires_csrf_token
def handler404(request, exception):
    return error_page(
        request, 404, 'Page not found',
        'The requested URL was not found on the server.'
        'If you entered the URL manually please check your spelling and try again.'
    )


@requires_csrf_token
def handler500(request):
    return error_page(
        request, 500, 'Internal Server Error',
        'The server encountered an internal error and was unable to complete your request.'
        'Either the server is overloaded or there is an error in the application.'
    )


class LoginView(auth_views.LoginView):
    template_name = 'adminlte_full/login.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'adminlte_full/auth/change_password.html'
    success_url = reverse_lazy(config['ADMINLTE_LOGIN_ENDPOINT'])


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'adminlte_full/auth/forgot_password.html'
    success_url = reverse_lazy(config['ADMINLTE_LOGIN_ENDPOINT'])

    def form_valid(self, form):
        print(self.get_success_url())
        messages.success(self.request, _('We’ve emailed you instructions for reset your password.'))
        return super().form_valid(form)


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'adminlte_full/auth/recover_password.html'
    success_url = reverse_lazy(config['ADMINLTE_LOGIN_ENDPOINT'])
    reset_url = reverse_lazy(config['ADMINLTE_PASSWORD_RESET_ENDPOINT'])

    def dispatch(self, *args, **kwargs):
        result = super().dispatch(*args, **kwargs)

        if not self.validlink:
            msg = _('The password reset link was invalid, possibly because it has already been used.  Please request a new password reset.')
            messages.error(self.request, msg)
            return HttpResponseRedirect(self.reset_url)

        return result

    def form_valid(self, form):
        messages.success(self.request, _('Your password has been set.  You may go ahead and log in now.'))
        return super().form_valid(form)


__all__ = (
    LoginView.__name__,
    PasswordChangeView.__name__,
    PasswordResetView.__name__,
    PasswordResetConfirmView.__name__,
)


class BaseView(TemplateView):
    __instance = None

    @classmethod
    def replace_with(cls, instance):
        cls.__instance = instance

    @classmethod
    def instance(cls):
        return cls.__instance or cls


class MessageView(BaseView):
    template_name = 'adminlte_full/base-layout.html'

    def get(self, request, *args, **kwargs):
        messages.debug(request, 'Redefine this page')
        return render(request, self.template_name)


class NotificationView(BaseView):
    template_name = 'adminlte_full/base-layout.html'

    def get(self, request, *args, **kwargs):
        messages.debug(request, 'Redefine this page')
        return render(request, self.template_name)


class TaskView(BaseView):
    template_name = 'adminlte_full/base-layout.html'

    def get(self, request, *args, **kwargs):
        messages.debug(request, 'Redefine this page')
        return render(request, self.template_name)


def index(request):
    pass