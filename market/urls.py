from django.urls import path

from . import views


urlpatterns = [
    path('go/', views.go, name='go'),
    path('menu/', views.menu, name='menu'),
]