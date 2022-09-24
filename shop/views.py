
from django.shortcuts import render, redirect
from . models import *
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string

# Create your views here.



def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'data': products, 'categories': categories}
    return render(request, 'shop.html', context)


# def category(request, slug):
#     category = Category.objects.get(slug=slug) 
#     categories = Category.objects.all()  
#     products = Product.objects.filter(category=category) 
#     context = {
#         'products': products,
#         'category':category,
#         'categories': categories


#     }
    # return render(request, 'category_list.html', context )


def item(request, slug):

    product = Product.objects.get(slug=slug)
    related_product = Product.objects.filter(category__in=product.category.all()).exclude(slug=slug).distinct()[:3]
    # promos = Product.objects.filter(has_discount=True)
    if product.price_before_discount > 0:
        old_price = Product.objects.filter(has_discount=True)

        context = {
        'product':product,
        'related': related_product,
        'old_price':old_price,
        }
 
        return render(request, 'item.html', context)
    else:
        data ={
             'product':product,
             'related': related_product,
        }
        return render(request, 'item.html',  data)    



def filter_category(request):
    categories = request.GET.getlist('category[]')
    allProducts = Product.objects.all()
    if len(categories) > 0:
        allProducts = allProducts.filter(category__id__in=categories).distinct()


    t = render_to_string('ajax/category_products.html', {'data':allProducts})
    return JsonResponse({'data':  t})
    