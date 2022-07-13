"""isdcbackend URL Configuration

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
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('test/', views.TestPage.as_view(), name="test"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('admin/', admin.site.urls),
    path('rest/', include('webpages.urls-rest')), # rest api
    path('', include('webpages.urls')), # Sites here in django
    path('api-token-auth/', obtain_jwt_token),
    path('ml/', include('ml.urls')),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
]