from django.contrib import admin
from django.urls import path
from Route import views
from .views import RouteListAPIView, RouteDetailAPIView
#from .views import  InterserviceCallAPIView



urlpatterns = [
    path("", views.index , name='home'),
    path("/main", views.main_route , name='main'),
    path('routes/', RouteListAPIView.as_view(), name='route-list'),
    path('routes/<int:pk>/', RouteDetailAPIView.as_view(), name='route-detail'),
]
