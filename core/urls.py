from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.core_index, name='index'),
]