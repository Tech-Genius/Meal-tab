
from django.shortcuts import render, redirect
from . models import *
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

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
    



#add to cart
def add_to_cart(request):
	# del request.session['cartdata']
	cart_p={}
	cart_p[str(request.GET['id'])]={
        'title':request.GET['title'],
		'image':request.GET['image'],	
		'qty':request.GET['qty'],
		'price':request.GET['price'],
	}
	if 'cartdata' in request.session:
		if str(request.GET['id']) in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
			cart_data.update(cart_data)
			request.session['cartdata']=cart_data
		else:
			cart_data=request.session['cartdata']
			cart_data.update(cart_p)
			request.session['cartdata']=cart_data
	else:
		request.session['cartdata']=cart_p
	return JsonResponse({'data': request.session['cartdata'], 'totalitems':len(request.session['cartdata'])})





#cart
def cart_view(request):
	total_amt=0
	if 'cartdata' in request.session:
		for p_id,item in request.session['cartdata'].items():
			total_amt+=int(item['qty'])*float(item['price'])
		return render(request, 'cart_view.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
	else:
		return render(request, 'cart_view.html',{'cart_data':'','totalitems':0,'total_amt':total_amt})



# Delete Cart Item
def delete_cart_item(request):
	p_id=str(request.GET['id'])
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			del request.session['cartdata'][p_id]
			request.session['cartdata']=cart_data
	total_amt=0
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*float(item['price'])
	t=render_to_string('ajax/cart-after-delete-and-update.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})



#update Item
def update_cart_item(request):
	p_id=str(request.GET['id'])
	p_qty=request.GET['qty']
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']=p_qty
			request.session['cartdata']=cart_data
	total_amt=0
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*float(item['price'])
	t=render_to_string('ajax/cart-after-delete-and-update.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})




#checkout
@login_required
def checkout(request):
	total_amt=0
	if 'cartdata' in request.session:
		for p_id,item in request.session['cartdata'].items():
			total_amt+=int(item['qty'])*float(item['price'])
		return render(request, 'checkout.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
	else:
		return render(request, 'checkout.html',{'cart_data':'','totalitems':0,'total_amt':total_amt})

	
