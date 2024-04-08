from django.contrib import admin
from django.urls import path
from nlt_for_railways import views

urlpatterns = [
   path('',views.index),
   path('home',views.home),
   # Path of Announcement 1
   # Path of Announcement 2
   # Path of Announcement 3
   path('booking',views.booking),
   path('feedback',views.feedback),
   path('contact',views.contact),
   path('arvrmodel',views.arvrmodel),
   path('model1',views.model1),
   path('railtalk',views.railtalk),
   path('announcement1',views.announcement1),
   path('announcement2',views.announcement2),

]