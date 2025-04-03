from django.urls import path, include
from .views import index, csrf_view

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('csrf_view', csrf_view, name='csrf_view'),
]

