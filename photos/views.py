from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def gallery(request):
    return render(request, 'photos/gallery.html')


def viewPhoto(request,pk):
     return render(request, 'photos/photo.html')


def newPhoto(request):
     return render(request, 'photos/new.html')