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
from django.views.generic import TemplateView

from os_client import views

urlpatterns = [
    path('clienthome/',TemplateView.as_view(template_name='os_client_templates/os_client_home.html')),
    path('clientwelcome/',TemplateView.as_view(template_name='os_client_templates/os_client_welcome.html')),
    path('clientlogincheck/',views.clientlogincheck),
    path('clientotpcheck/',views.clientotpcheck),
    path('clientregister/',views.clientregister),
    path('clientsavedata/',views.clientsavedata),
    path('clientproperty/',views.clientproperty),
    path('block/',views.blockproperty),
    path('unblock/',views.unblockproperty),
    path('blocked/',views.blokedproperty),
    path('complaint/',views.complaint),
    path('comsubmit/',views.comsubmit),
    path('comdelete/',views.comcdelete)
]
