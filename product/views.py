from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_list_or_404, get_object_or_404
from menu import models as me
from product import models as pp

# Create your views here.
menu_item = me.menu.objects.all()


def product(request, productlink):
    menu_list = []
    menu_list.append(productlink)
    sub_list = me.menu.objects.filter(parent_menu_id=productlink)
    for x in sub_list:
        menu_list.append(x.id)
        sub_sub_list= me.menu.objects.filter(parent_menu_id=x.id)
        for y in sub_sub_list:
            menu_list.append(y.id)
            
    products = pp.Product.objects.filter(as_menu__in=menu_list)
    
    number_of_videos_per_page = 2
    
    paginator = Paginator(products, number_of_videos_per_page)  # Display 25 items per page
    page = request.GET.get("page")
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    # Add auto-serial numbers to the videos
    start_serial = (products.number - 1) * number_of_videos_per_page + 1  # Adjust for the current page
    for index, video in enumerate(products, start=start_serial):
        video.serial = index 
        
    
    context = {
        'menu_items': menu_item,
        'product_link': productlink,
        'products': products,
    }
    return render(request, 'index.html', context)


def productitem(request, product_slug):
    item = get_object_or_404(pp.Product, slug=product_slug)
    itemimg = pp.ProductImage.objects.filter(product=item.pk)
    context = {
        'menu_items': menu_item,
        'item': item,
        'itemimg': itemimg,
    }
    return render(request, 'item_details.html', context)


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product:product', product_id=product_id)

def view_cart(request):
    cart = request.session.get('cart', {})
    products = pp.Product.objects.filter(id__in=cart.keys())
    context = {'products': products, 'cart': cart}
    return render(request, 'cart.html', context)


# from django.contrib.auth.decorators import login_required

# @login_required
def merge_cart(request):
    cart = request.session.get('cart', {})
    user = request.user
    user_cart = user.cart

    for product_id, quantity in cart.items():
        user_cart.products.add(product_id, through_defaults={'quantity': quantity})

    del request.session['cart']
    return redirect('cart:view_cart')