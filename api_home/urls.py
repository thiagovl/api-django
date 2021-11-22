"""api_home URL Configuration

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

from django.contrib import admin
from django.urls import path
from core.views import ResumoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    # GET ALL
    path('resumos/', ResumoViewSet.list)
]
"""

from core.views import resumo
from rest_framework.routers import DefaultRouter

from django.urls import include, path
from rest_framework import routers

app_name = 'api_home'

router = DefaultRouter()
router.register(r'resumo', resumo.ResumoViewSet, basename='resumo')

router.register(r'users', resumo.UserViewSet)
router.register(r'groups', resumo.GroupViewSet)

urlpatterns = [
    # router.urls
    path('', include(router.urls)), # Route resumo/
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # Route autentication = api-auth/login/ login = users/login/ logout = users/logout/
] 