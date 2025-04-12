from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
   path('',views.index,name="index"),
   path('basic',views.basic,name="basic"),
   path('about',views.about,name="about"),
   path('gallery',views.gallery,name="gallery"),
   path('agents',views.agents,name="agents"),
   path('contact',views.contact,name="contact"),
   path('packages',views.packages,name="packages"),
   path('bookingconfirmed',views.bookingconfirmed,name="bookingconfirmed"),
   path('addpackage',views.addpackage,name="addpackage"),
   path('submitreview',views.submitreview,name="submitreview"),
   path('submitcontact',views.submitcontact,name="submitcontact"),
   path('searchresult',views.searchresult,name="searchresult"),
   path('viewpackages',views.viewpackages,name="viewpackages"),
   path('bookedpackages',views.bookedpackages,name="bookedpackages"),
   path('viewmybookings',views.viewmybookings,name="viewmybookings"),
   path('addpackagesubmit',views.addpackagesubmit,name="addpackagesubmit"),
   path('completeprofile',views.completeprofile,name="completeprofile"),
   path('yourprofile',views.yourprofile,name="yourprofile"),
   path('completeprofilesubmit',views.completeprofilesubmit,name="completeprofilesubmit"),
   path('viewdata', views.viewdata, name='viewdata'),
   path('checkuser', views.checklogin, name='checkuser'),
   path('logout', views.logout, name='logout'),
   path("forgotpassword", views.forgotpassword, name="forgotpassword"),
   path('register', views.register, name='register'),
   path('destinationdetailes/<int:ddid>',views.destinationdetailes,name="destinationdetailes"),  #this is package single page
   path('deletepackage/<int:dpid>',views.deletepackage,name="deletepackage"),
   path('closepackage/<int:cpid>',views.closepackage,name="closepackage"),
   path('reopenpackage/<int:ropid>',views.reopenpackage,name="reopenpackage"),
   path('agentprofile/<int:apid>',views.agentprofile,name="agentprofile"),
   path('agentpackages/<int:apkid>',views.agentpackages,name="agentpackages"),
#   path('bookpackage/<int:bpkid>',views.bookpackage,name="bookpackage"),
   path('bookpackage',views.bookpackage,name="bookpackage"),
   path('cancel/<int:id>',views.destroy,name="cancel"),
]