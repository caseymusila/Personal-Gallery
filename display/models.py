from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 50)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length = 50)

    def save_category(self):
        self.save()

    def delete_catgory(self):
        self.delete()

    def __str__(self):
        return self.category

class Images(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length = 100)
    image_description = models.TextField()
    image_category = models.ManyToManyField(Category, related_name = 'posts')
    image_location = models.ForeignKey(Location, related_name = 'posts', on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)