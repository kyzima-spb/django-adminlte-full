from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.urls.base import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .adminlte import config
from .forms import *


__all__ = (
    'error_page', 'handler400', 'handler403', 'handler404', 'handler500',
    'LoginView',
    'PasswordChangeView', 'PasswordResetView', 'PasswordResetConfirmView',
)


def error_page(request, code, message, details):
    template = 'adminlte_full/http_error_page.html'
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
    form_class = AuthenticationForm
    template_name = 'adminlte_full/login.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'adminlte_full/change_password.html'
    success_url = reverse_lazy(config['ADMINLTE_LOGIN_ENDPOINT'])


class PasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'adminlte_full/forgot_password.html'
    success_url = reverse_lazy(config['ADMINLTE_LOGIN_ENDPOINT'])

    def form_valid(self, form):
        messages.success(self.request, _('We’ve emailed you instructions for reset your password.'))
        return super().form_valid(form)


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'adminlte_full/recover_password.html'
    success_url = reverse_lazy(config['ADMINLTE_LOGIN_ENDPOINT'])

    def form_valid(self, form):
        messages.success(self.request, _('Your password has been set.  You may go ahead and log in now.'))
        return super().form_valid(form)
