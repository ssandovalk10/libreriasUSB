from django.urls import path

from .views import Reports

app_name = 'reportes'

urlpatterns = [
    path('reports', Reports, name='reports')
]

