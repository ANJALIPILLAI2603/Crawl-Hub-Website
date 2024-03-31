"""
URL configuration for Web_crawler project.

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
from django.urls import path, include  # Include for app URLs
from CrawlHub import views  # Import views from CrawlHub app
from django.contrib import admin  # For admin interface

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL pattern
    path('', views.crawl, name='crawl'),  # Your app's URL pattern
]
