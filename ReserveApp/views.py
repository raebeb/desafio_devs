from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from .services import get_holidays
from .models import *

class IndexView(TemplateView):
    template_name = "ReserveApp/index.html"
    def get_context_data(self, *args, **kwargs):
        context = {
            'holidays' : get_holidays(),
        }
        return context

    