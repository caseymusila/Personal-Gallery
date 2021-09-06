from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Images(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length = 100)
    image_description = models.TextField()
    image_category = models.ManyToManyField(Category, related_name = 'posts')
    image_location = models.ForeignKey(Location, related_name = 'posts', on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)