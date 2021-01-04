"""user_profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from details import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create_detail',views.UserCreate.as_view()),
   
    path('api-auth/',include('rest_framework.urls')),#only adding this and no other fn will add logout dropdown buttom
    #near usernmae or just login if not logged in
]