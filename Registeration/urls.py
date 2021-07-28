from django.contrib import admin
from .import views
from django.urls import path
from .views import *

urlpatterns =[
    path('',views.index,name = 'index'),
    path('index.html',views.index,name = 'index'),
    path('auth-signup.html',views.signup,name = 'signup'),
    path('auth-signin.html',views.signin,name = 'signin'),
    path('signinAPI',signinAPI.as_view(),name = 'signin'),
    path('ReadingJason',ReadingJason.as_view(),name = 'ReadingJason')
]