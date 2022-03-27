from unicodedata import category
from django.test import TestCase

from photos.models import Category,Location,Image

# Create your tests here.

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.travel= Category(category_name='Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))


    def test_save_method(self):
        self.travel.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)  

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0) 


class LocationTestCase(TestCase):
    def setUp(self):
        self.location=Location(location_name='Coast')
        self.location.save_location()
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    
    def test_save_location(self):
        self.location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        category = Location.objects.all()
        self.assertTrue(len(category) == 0)
    
    
    def test_get_location(self):
        location = Location.get_locations()
        self.assertTrue(location)   

class ImageTestcase(TestCase):
    def setUp(self):

        self.category=Category(category_name='Hiking')
        self.category.save_category()

        self.location = Location(location_name='Coast')
        self.location.save_location()

        self.beach= Image(id=1,image_name = 'Hike', description ='hike Test',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.beach,Image)) 

    def test_save_image(self):
        self.beach.save_image()
        img = Image.objects.all()
        self.assertTrue(len(img) > 0)

    def test_delete_image(self):
        self.beach.delete_image()
        image= Image.objects.all()
        self.assertTrue(len(image)== 0)
    
    def test_update_image(self):
        self.beach.save_image()                        
        
             



