from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
      path('signup/',views.signup,name='signup'),
      path('signin/',views.signin,name='signin'),
      path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
      path('loginhome/',views.loginhome,name='loginhome'),
    path('',views.mainhome,name='mainhome'),  
    path('contact/',views.contact,name='contact'),
    path('course/',views.course,name='course'),
    path('gallery/',views.gallery,name='gallery'),
    path('login/',views.login,name='login'),
    path('coursedetails/',views.coursedetails,name='coursedetails'),

    
]