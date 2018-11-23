"""Onion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from Main import views

urlpatterns = [
    path('contact/', views.contact_us, name="Contact"),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('sign_up/', views.sign_up),
    path('sign_in/', views.sign_in),
    path('contact_us/', views.contact_us),
    path('logout/', views.log_out),
    path('user/', views.show_prof),
    path('edit/', views.edit_user)
]
