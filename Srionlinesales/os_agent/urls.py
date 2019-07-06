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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from os_agent import views

urlpatterns = [
    path('agenthome/',views.agenthome,name='agenthome'),
    path('agentwelcome/',TemplateView.as_view(template_name='os_agent_templates/os_agent_welcome.html')),
    path('agentlogincheck/',views.agentlogincheck),
    path('agentotpcheck/', views.agentotpcheck),
    path('agentproperty/', views.agentproperty),
    path('agentpropertysave/',views.agentpropertysave),
    path('block/',views.blockproperty),
    path('sold/',views.soldproperty),
    path('viewsold/',views.viewsoldproperty),
    path('agentdeleteconformation<int:pk>/',views.agentdeleteconformation.as_view())
]
