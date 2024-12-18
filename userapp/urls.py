from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views



urlpatterns=[
    path('',views.UserAPIView.as_view()),
    path('<int:pk>/', views.UserAPIView.as_view()),
]   