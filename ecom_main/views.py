from django.shortcuts import render, redirect, HttpResponse
from menu import models as me
from product import models as pp

menu_item = me.menu.objects.all()
product_item = pp.Product.objects.all()

def index(request):
    context = {
        'menu_items': menu_item,
    }
    return render(request, 'index.html', context)

def electronics(request):
    context = {
        'menu_items': menu_item,
        'product': product_item,
    }
    return render(request, 'electronics.html', context)