from django.urls import path

from . import views


urlpatterns = [
    path('go2/', views.go, name='market/go'),
]