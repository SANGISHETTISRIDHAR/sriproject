"""Srionlinesales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView,DeleteView
from os_admin import views
from .models import Agent
urlpatterns = [
    path('adminhome/', views.adminhome,name='adminhome'),
    path('adminwelcome/',TemplateView.as_view(template_name='os_admin_templates/os_admin_welcome.html')),
    path('adminlogincheck/',views.adminlogincheck,name='adminlogincheck'),
    path('adminotpcheck/', views.adminotpcheck),
    path('agentregister/',views.agentregister),
    path('savedata/', views.savedata),
    path('agentdelete/',views.agentdelete),
    path('adminlogout/',views.adminlogout),
    path('aboutus/',views.aboutsus),
    path('contactus/',views.contactus),
    path('client/', views.viewallclients),
    path('property/',views.propertyall),
    path('deleteclient/',views.deleteclient)
]
