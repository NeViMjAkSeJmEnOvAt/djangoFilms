from django.urls import path

from Filmy import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topten', views.topten, name='topten'),
]


