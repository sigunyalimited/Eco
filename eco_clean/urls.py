from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('careers/', views.career_view, name='careers'),
    path('contact/', views.contact_view, name='contact'),
    path('media/', views.media_view, name='media'),
]

# Correct way to add static URL patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
