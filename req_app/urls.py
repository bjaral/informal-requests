from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('getRequests/', views.getRequests, name='getRequests'),
    path('setRequest/', views.setRequest, name='setRequest'),
    path('request/<int:req_id>/', views.request, name='request'),
]