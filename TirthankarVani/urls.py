"""TirthankarVani URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.flatpages import views
from django.views.generic.base import TemplateView

admin.site.site_header = 'Tirthankar Vani'
admin.site.site_title = 'Tirthankar Vani admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('navkar/', views.flatpage, {'url': '/navkar/'}, name='navkar'),
    path('tirthankar/', views.flatpage, {'url': '/tirthankar/'}, name='tirthankar'),
    path('pooja/', views.flatpage, {'url': '/pooja/'}, name='pooja'),
    path('stotra/', views.flatpage, {'url': '/stotra/'}, name='stotra'),
    path('more/', views.flatpage, {'url': '/more/'}, name='more'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
