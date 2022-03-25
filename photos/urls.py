from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery, name='gallery'),
    path('photo/',views.viewPhoto, name='photo'),
    path('new/',views.newPhoto, name='new'),
]