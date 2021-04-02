from django.urls import path
from .views import main_page, about, gallery, contact, index

urlpatterns = [
    path('',main_page, name='main_page'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('index/',index, name='index')
]