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