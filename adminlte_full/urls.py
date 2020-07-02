from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .context_processors import config


urlpatterns = [
    # Auth views
    path('login/', views.LoginView.as_view(), name=config['ADMINLTE_LOGIN_ENDPOINT']),
    path('logout/', auth_views.LogoutView.as_view(), name=config['ADMINLTE_LOGOUT_ENDPOINT']),

    path('password_change/', views.PasswordChangeView.as_view(), name=config['ADMINLTE_CHANGE_PASSWORD_ENDPOINT']),

    path('password_reset/', views.PasswordResetView.as_view(), name=config['ADMINLTE_PASSWORD_RESET_ENDPOINT']),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name=config['ADMINLTE_PASSWORD_RECOVER_ENDPOINT']),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # End auth views
]
