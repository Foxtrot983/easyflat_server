"""
URL configuration for realtHouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls.conf import include
# DRF YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Djoser API",
        default_version="v1",
        description="REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model.",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path("admin/", admin.site.urls),
    path(r"auth/", include('djoser.urls')),
    path(r"auth/", include('djoser.urls.authtoken')),
    re_path(
        r"^api/v1/docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    

    path("", include("houses.urls")),
    path('acc/', include("account.urls")),

]

"""
test credentials:
{
    "email": "user7@example.com",
    "password": "TestRegPass",
}
token: 
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNzIwODQ2LCJpYXQiOjE2ODM3MTcyNDYsImp0aSI6IjA4ZDJjZjhmNjM3MDQ2ZDBiZWY5ZGZlNDEyZTc1ODc0IiwidXNlcl9pZCI6Nn0.iZONZ7tEiYJ2tgDHwdB7n4Vrsu55Q254RvoyomSeEpM
"""

