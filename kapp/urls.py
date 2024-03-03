
from django.contrib import admin
from django.urls import path
from kapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('registration/', views.register, name='registration'),
    path('login/', views.login, name='login'),
]
