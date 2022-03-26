
from django.shortcuts import render
from django.http import HttpResponse
from.models import Category,Photo

# Create your views here.


def gallery(request):
     categories=Category.objects.all()
     photos = Photo.objects.all()
     context ={'categories':categories , 'photos':photos} 
     return render(request, 'photos/gallery.html')


def viewPhoto(request):
     return render(request, 'photos/photo.html')


def newPhoto(request):
     return render(request, 'photos/new.html')