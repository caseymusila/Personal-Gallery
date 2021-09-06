from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:pk>/', views.image_details, name='details'),
    path('search/', views.search_results, name = 'search_results'),
    path('<category>/', views.image_category, name = 'images_category'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)   