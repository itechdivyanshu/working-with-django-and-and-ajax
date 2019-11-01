from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home,name='home'),
    path('add', views.add,name='add'),
    path('sendajax/', views.sendajax,name='sendajax'),
    path('', views.index,name='index'),
]
