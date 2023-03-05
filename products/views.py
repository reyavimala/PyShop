from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.db.models import Q
import logging
from django.http import HttpResponseRedirect

logger = logging.getLogger("products")

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

    

def new(request):
    return HttpResponse('Welcome to PyShop New Arrivals')



def search(request):
    query = request.GET.get('search')
    # matched_products = Product.objects.filter(Q(name__icontains=query))
    matched_products = Product.objects.filter(name__icontains=query)
    logger.info(matched_products[0].image_url)
    return render(request, 'search.html', {'all_search_results': matched_products})


# def search(request):
#     if request.method == 'GET': 
#         # form = search(request.get) 
#         query = request.GET.get('search')
#         # if form.is_valid(): 
#         return HttpResponseRedirect('/search') 
#     else:
#         form = search() 

#     return render('search.html', {
#         'form': form,
#     })

# def custom_data_generator(request):
#     logger.info(" matched_products[0].image_url") 
#     return 