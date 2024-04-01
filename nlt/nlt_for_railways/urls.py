from django.contrib import admin
from django.urls import path
from nlt_for_railways import views

urlpatterns = [
   path('',views.index),
   # path('register',views.register),
   path('servicesbt',views.service_sbt),
   path('servicesbs',views.service_sbs),
   path('servicesbp',views.service_sbp),
   path('contact',views.contact),
   path('home',views.home),
   path('about',views.about)

]