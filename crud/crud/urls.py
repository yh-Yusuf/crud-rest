"""DjangoRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from crudapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('post_model/' , post_model, name = 'post_model'),
    path('get_model/', get_model , name= 'get_model'),
    path('delete_all/', delete_all , name= 'delete_all'),
    path('getPost/<int:id>', single_post, name='single_post'),
    path('delete_post/<int:id>', delete_post, name='delete_post'),
    path('update/<int:id>', update_post, name='update_post'),

]
