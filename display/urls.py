from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:pk>/', views.image_details, name='details'),
    path('search/', views.search_results, name = 'search_results'),
    path('<category>/', views.image_category, name = 'images_category'),
]