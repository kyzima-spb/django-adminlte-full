from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import PrependedText, AppendedText, Field, InlineField
from django.contrib.auth import forms as auth_forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


__all__ = (
    'AuthenticationForm',
    'PasswordChangeForm', 'PasswordResetForm', 'SetPasswordForm',
)


class AuthenticationForm(auth_forms.AuthenticationForm):
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_show_labels = False
        helper.form_tag = False
        helper.layout = Layout(
            AppendedText('username', mark_safe('<span class="fas fa-envelope"></span>'), placeholder=_('Username')),
            AppendedText('password', mark_safe('<span class="fas fa-lock"></span>'), placeholder=_('Password')),
        )
        return helper


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        return helper


class PasswordResetForm(auth_forms.PasswordResetForm):
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_show_labels = False
        helper.form_tag = False
        helper.layout = Layout(
            AppendedText('email', mark_safe('<span class="fas fa-envelope"></span>'), placeholder=_('Email'))
        )
        return helper


class SetPasswordForm(auth_forms.SetPasswordForm):
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_show_labels = False
        helper.form_tag = False
        helper.layout = Layout(
            AppendedText('new_password1', mark_safe('<span class="fas fa-lock"></span>'), placeholder=_('New password')),
            AppendedText('new_password2', mark_safe('<span class="fas fa-lock"></span>'), placeholder=_('New password confirmation'))
        )
        return helper
