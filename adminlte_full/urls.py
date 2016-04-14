from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^message/(?P<id>\w+)$', views.index, name='adminlte_full_show_message'),
    url(r'^messages$', views.index, name='adminlte_full_all_messages'),

    url(r'^notification/(?P<id>\w+)$', views.index, name='adminlte_full_show_notification'),
    url(r'^notifications$', views.index, name='adminlte_full_all_notifications'),

    url(r'^task/(?P<id>\w+)$', views.index, name='adminlte_full_show_task'),
    url(r'^tasks$', views.index, name='adminlte_full_all_tasks'),
]
