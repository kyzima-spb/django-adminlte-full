from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),

    url(r'^message/(?P<id>\w+)$', views.index, name='adminlte_full_show_message'),
    url(r'^messages$', views.index, name='adminlte_full_all_messages'),

    url(r'^notification/(?P<id>\w+)$', views.index, name='adminlte_full_show_notification'),
    url(r'^notifications$', views.index, name='adminlte_full_all_notifications'),

    url(r'^task/(?P<id>\w+)$', views.index, name='adminlte_full_show_task'),
    url(r'^tasks$', views.index, name='adminlte_full_all_tasks'),

    url(
        r'^profile$',
        auth_views.password_change,
        {
            'template_name': 'adminlte_full/user/password_change_form.html',
            'post_change_redirect': 'adminlte_full_profile'
        },
        name='adminlte_full_profile'
    ),

    url(
        r'^logout$',
        auth_views.logout_then_login,
        {
            'login_url': '/'
        },
        name='adminlte_full_logout'
    ),
]
