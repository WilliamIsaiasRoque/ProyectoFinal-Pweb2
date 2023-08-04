# pdfs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
]
