"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('movie_detail', movie_detail, name="movie_detail"),
    path('ticketing', ticketing, name="ticketing"),
    path('movie_list', movie_list, name="movie_list"),
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
<<<<<<< HEAD
    path('forget', forget, name="forget"),
=======
    path('events', events, name="events"),
    path('event_detail', event_detail, name="event_detail"),
>>>>>>> 7ad79f6c0aa9f42d34f238a2cdf718c6b40b465e
    path('findID', findID, name="findID"),
    path('events', events, name="events"),
    path('event_detail', event_detail, name="event_detail"),
    path('mypage', mypage, name="mypage"),
    path('eventrecord', eventrecord, name="eventrecord"),
    path('infomodification', infomodification, name="infomodification"),
    path('reservationinfo', reservationinfo, name="reservationinfo"),

    path('manage_main', manage_main, name="manage_main"),
    path('manage_revenue', manage_revenue, name="manage_revenue"),
]
