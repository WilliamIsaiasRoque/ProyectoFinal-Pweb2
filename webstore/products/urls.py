from django.urls import path
from . import views

urlpatterns = [
    path('', views.pag_main, name='pag_main'),
]