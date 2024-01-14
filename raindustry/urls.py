"""
URL configuration for raindustry project.

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
from django.urls import path
from weather.views import login_view, test_view, tavg_forecast, rhavg_forecast, ffavg_forecast

urlpatterns = [
    path('admin/', admin.site.urls),

  
    path('login/', login_view, name='login'),
    path('test/', test_view, name='test'),  # Tambahkan path untuk view 'test'
    path('forecastsuhu/', tavg_forecast, name='tavg_forecas'),
    path('forecastrh/', rhavg_forecast, name='rhavg_forecast'),
    path('forecastff/', ffavg_forecast, name='ffavg_forecast'),


]
