from django.urls import path, include
from .views import index, csrf_view, escape_view, cors_example

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('csrf_view', csrf_view, name='csrf_view'),
    path('escape', escape_view, name='escape_view'),
    path('cors', cors_example, name='cors_example'),
]

