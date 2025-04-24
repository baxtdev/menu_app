from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('home/',views.index,name="home"),
    path('missions/',views.missions,name="our-missions")
]