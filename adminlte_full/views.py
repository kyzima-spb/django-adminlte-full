from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages


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