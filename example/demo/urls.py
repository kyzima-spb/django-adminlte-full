from django.urls import path

from . import views
from adminlte_full.adminlte import config


urlpatterns = [
    path('', views.index),
    path('terms/', views.terms),
    path('profile/', views.profile, name=config['ADMINLTE_PROFILE_ENDPOINT']),
]
