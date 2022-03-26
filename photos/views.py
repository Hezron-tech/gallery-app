
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from.models import Category,Photo

# Create your views here.


def gallery(request):
     categories=Category.objects.all()
     photos = Photo.objects.all()
     context ={'categories':categories , 'photos':photos} 
     return render(request, 'photos/gallery.html', context)


def viewPhoto(request,pk):
     photo = Photo.objects.get(id=pk)
     return render(request, 'photos/photo.html' ,{'photo':photo})
     


def newPhoto(request):

     categories=Category.objects.all()
     context ={'categories':categories}
     return render(request, 'photos/new.html',context)