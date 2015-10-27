"""Flitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from flitterMainApp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^signUp/', views.signUpUser, name='signUp'),
    url(r'^processSignUp/', views.processSignUp, name='processSignUp'),
    url(r'^generate/', views.authenticateUser, name='authenticate'),
    url(r'^home/', views.homePage, name='home'),
    url(r'^postStatusUpdate/', views.postStatusUpdate, name='statusUpdate'),
    url(r'^saveStatusUpdate/', views.saveStatusUpdate, name='saveStatusUpdate'),
    url(r'^searchPage/', views.searchPage, name='searchPage'),
    url(r'^processFollow/', views.processFollow, name='processFollow'),
    url(r'^processUnFollow/', views.processUnFollow, name='processUnFollow'),
    url(r'^exploreCommunity/', views.exploreCommunity, name='exploreCommunity'),
    url(r'^logOff/', views.logOff, name='logOff'),
    url(r'^$', views.index, name='index'),
]
