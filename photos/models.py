
from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    location_name = models.CharField(max_length=50)  


    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        location=Location.objects.all()

        return location      


class Photo(models.Model):
    category =models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE, default='') 
    image=models.ImageField(null=False, blank=False)
    description=models.TextField()
    

    def __str__(self):
        return self.description 

    
    def __str__(self):
        return self.photo_name

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def update_photo(cls, id,photo):
        cls.objects.filter(id=id).update(photo=photo) 

    @classmethod
    def search_category(cls,category):
        photo =cls.objects.filter(category__category_name__icontains=category)

        return photo

    @classmethod
    def fetch_by_location(cls,location_name):
        location = cls.objects.filter(location__location_name = location_name).all()
        return location


    @classmethod
    def get_photo_by_id(cls, photo_id):
        photo = cls.objects.get(id=photo_id)
        return photo              
  