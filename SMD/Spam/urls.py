"""
URL configuration for SMD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from .views import contact_view
from .views import register_view
from .views import login_view


urlpatterns = [
    #path("admin/", admin.site.urls),
    path('', views.index, name = "Index"),
    path('check', views.checkSpam, name = "CheckSpam"),
    path('about.html', views.about, name = 'about'),
    path('contact.html', views.contact, name = 'contact'),
    path('login.html', views.login, name = 'login'),
    path('register.html', views.register, name = 'register'),
    path('contact/', views.contact_view, name = 'contact'),
    path('register/', register_view, name = 'register'),
    path('auth/login/', login_view, name = 'login'),
    path('login/', views.login_view, name = 'login'),
    path('index/', views.index_view, name = 'index'),
    path('index.html', views.index, name = "index"),
]
