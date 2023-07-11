from django.contrib import admin
from django.urls import path, include
from home import views



# Django admin dashboard customization
admin.site.site_header = "Login to Kapil's Site"
admin.site.site_title = "Kapil's Django Project"
admin.site.index_title = "Welcome to the Dashboard"



urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),

    
     
]
