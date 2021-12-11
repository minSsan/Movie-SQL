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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('movie_detail', movie_detail, name="movie_detail"),
    path('ticket_list', ticket_list, name="ticket_list"),
    path('movie_list', movie_list, name="movie_list"),
    path('signup', signup_view, name="signup"),
    path('login', login_view, name="login"),
    path('events', events, name="events"),
    path('event_detail', event_detail, name="event_detail"),
    path('forget', forget, name="forget"),
    path('findID', findID, name="findID"),
    path('logout/',logout_view, name='logout'),
    path('ticketing', ticketing, name="ticketing"),
    path('ticketing_seat', ticketing_seat, name="ticketing_seat"),
    
    path('mypage', mypage, name="mypage"),
    path('eventrecord', eventrecord, name="eventrecord"),
    path('infomodification', infomodification, name="infomodification"),
    path('reservationinfo', reservationinfo, name="reservationinfo"),

    path('manage_main', manage_main, name="manage_main"),
    path('manage_revenue', manage_revenue, name="manage_revenue"),
    path('manage_revenue_search', manage_revenue_search, name="manage_revenue_search"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)