from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/check/', views.SpellCheckCreateAPI.as_view(), name='api'),
    path('api/check/<int:pk>/', views.SpellCheckRetrieveAPI.as_view()),
]