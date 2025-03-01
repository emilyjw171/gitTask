from django.contrib import admin
from django.urls import path, include  
from band import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('members/', views.band_members, name='members'),    
    path('album/', views.album, name='album'), # Album page
    path('', include('band.urls')),
]
