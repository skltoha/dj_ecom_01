from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_list_or_404
from menu import models as me
from product import models as pp

menu_item = me.menu.objects.all()

def index(request):
    context = {
        'menu_items': menu_item,
    }
    return render(request, 'index.html', context)

