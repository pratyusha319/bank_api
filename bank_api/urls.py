"""bank_api URL Configuration

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
from django.urls import path,include
from app.views import *
from rest_framework.routers import DefaultRouter
DRO=DefaultRouter()

DRO.register('branch',branch_jd,basename='branch')
DRO.register('bank',bank_jd,basename='bank')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bank_upload_data/',bank_upload_data,name='bank_upload_data'),
    path('branch_upload_data/',branch_upload_data,name='branch_upload_data'),
    #path('display/',display,name='display'),
   # path('display_data/',display_data,name='display_data'),
    path('app/',include(DRO.urls))

]