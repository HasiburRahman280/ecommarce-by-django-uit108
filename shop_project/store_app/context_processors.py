from .models import *

def categories(request):
    catagory = Category.objects.filter(parent_category=None)

    context = {
        'catagory':catagory,
    }
    return context