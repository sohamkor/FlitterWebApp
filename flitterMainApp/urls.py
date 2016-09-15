from django.conf.urls import url

from . import views

app_name = 'flitterMainApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signUp/', views.signUpUser, name='signUp'),
    url(r'^processSignUp/', views.processSignUp, name='processSignUp'),
    url(r'^generate/', views.authenticateUser, name='authenticate'),
    url(r'^home/', views.homePage, name='home'),
    url(r'^postStatusUpdate/', views.postStatusUpdate, name='postStatusUpdate'),
    url(r'^saveStatusUpdate/', views.saveStatusUpdate, name='saveStatusUpdate'),
    url(r'^searchPage/', views.searchPage, name='searchPage'),
    url(r'^processFollow/', views.processFollow, name='processFollow'),
    url(r'^processUnFollow/', views.processUnFollow, name='processUnFollow'),
    url(r'^exploreCommunity/', views.exploreCommunity, name='exploreCommunity'),
    url(r'^logOff/', views.logOff, name='logOff'),
]
