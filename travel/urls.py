"""travel URL Configuration

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
from django.urls import path 
from webdulich import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('exp/', views.exp_view, name='exp'),
    path('discover/', views.discover_view, name='discover'),
    path('heritage/', views.heritage_view, name='heritage'),
    path('fastnew/', views.fastnew_view, name='fastnew'),
    path('food/', views.food_view, name='food'),
    path('brand/', views.brand_view, name='brand'),
    re_path(r'^editor/', include('ckeditor_uploader.urls')),
    path('<int:id>/', views.postDetail, name='postDetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
