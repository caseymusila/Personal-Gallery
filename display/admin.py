from django.contrib import admin
from .models import Location, Category, Images
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('image_category',)

class CategoryAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Images, ImageAdmin)