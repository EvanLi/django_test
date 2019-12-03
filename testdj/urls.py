"""testdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# new:
from django.conf.urls import *
 
from . import view,testdb
 
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^testdb1$',testdb.testdb1),
    url(r'^testdb2$',testdb.testdb2),
    url(r'^testdb3$',testdb.testdb3),
    url(r'^testdb4$',testdb.testdb4)
]