from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.comment, name='comment'),
    path('comments/add/', views.add_comments, name='add_comments'),
    path('comments/new/', views.form_comment, name='form_comment'),
]
