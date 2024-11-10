from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu.html'),
]