from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_list_or_404
from menu import models as me
from product import models as pp

menu_item = me.menu.objects.all()

def index(request):
    context = {
        'menu_items': menu_item,
    }
    return render(request, 'index.html', context)


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
    context = {
        'menu_items': menu_item,
        'product_link': productlink,
        'products': products,
    }
    return render(request, 'index.html', context)
