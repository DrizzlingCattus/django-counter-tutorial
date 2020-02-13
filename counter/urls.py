from django.urls import path, include
from . import views

app_name = 'counter'
urlpatterns = [
    path('', views.index, name="index"),
    path('up/', views.up, name="up"),
    path('down/', views.down, name="down"),
    path('clear/', views.clear, name="clear"),
]
