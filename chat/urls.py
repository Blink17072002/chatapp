from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('login/', views.Login, name='login'),
    path('signup/', views.sign_up, name='sign_up'),
]