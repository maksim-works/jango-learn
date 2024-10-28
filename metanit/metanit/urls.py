"""
URL configuration for metanit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
from hello import views

urlpatterns = [
    path('index', views.index),
    path('headers', views.headers),
    path('send-error', views.send_error),
    path('send-text', views.send_text),
    re_path(r'^about', views.about, kwargs={"name": "Tom", "age": 38}),
    re_path(r'^contact', views.contact)
]