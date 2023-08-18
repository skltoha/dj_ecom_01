from django.shortcuts import render, redirect, HttpResponse
from menu import models as me
from product import models as pp

menu_item = me.menu.objects.all()

def index(request):
    context = {
        'menu_items': menu_item,
    }
    return render(request, 'index.html', context)

def product(request, productlink):
    products = pp.Product.objects.filter(as_menu=productlink)
    context = {
        'menu_items': menu_item,
        'product_link': productlink,
        'products': products
    }
    return render(request, 'index.html', context)
