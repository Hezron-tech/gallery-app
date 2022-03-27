from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery, name='gallery'),
    path('photo/<str:pk>/',views.viewPhoto, name='photo'),
    path('new/',views.newPhoto, name='new'),
    path('location/ <str:location_name>/',views.photo_location,name = 'location'),
    # path('location/(?P<location_name>\w+)',views.photo_location,name = 'location'),
]

