from django.urls import path

from .views import LibreriaListView, Search

app_name = 'librerias'

urlpatterns = [
    path('librerias_list', LibreriaListView.as_view(), name='librerias_list'),
    path('search', Search, name = 'search')
]