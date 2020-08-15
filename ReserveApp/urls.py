from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'ReserveApp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
]