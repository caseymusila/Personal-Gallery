from django.shortcuts import render
from .models import Images, Location, Category

# Create your views here.
def home(request):
    '''
    Function to display the home page
    '''
    images = Images.objects.all().order_by('-last_modified')
    location = Location.objects.all()
    context = {
        'images': images,
        'location': location
    }
    return render(request, "all-images/images.html", context)

def image_details(request, pk):
    image = Images.objects.get(pk = pk)
    location = Location.objects.all()
    context = {
        'image': image,
        'location': location
    }
    return render(request, "all-images/image_details.html", context)

def search_results(request):
    location = Location.objects.all()

    if 'search_item' in request.GET and request.GET["search_item"]:
        search_term = request.GET.get("search_item")
        searched_images = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, "all-images/search.html", {"message": message, "searched_images": searched_images, "location": location})

    else:
        return render(request, 'all-images/search.html', {"location": location})

