"""GamingWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Register, name='register'),
    path('home/', Home, name='home'),
    path('login/', Login, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('govtevents/', GovtEvents, name='govtevents'),
    path('funquiz/', FunQuiz, name='funquiz'),
    path('quiz/', Quiz, name='quiz'),
    path('quiz2/', Quiz2, name='quiz2'),
    path('quiz3/', Quiz3, name='quiz3'),
    path('contactus', Contactus, name='contactus'),
]
