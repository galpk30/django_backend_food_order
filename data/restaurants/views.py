from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Restaurant
from .models import Item

# Create your views here.

def index(request):
    return HttpResponse("index")

def restaurant_list(request):
    restaurants_list = Restaurant.objects.order_by('id')
    context = {"restaurants_list": restaurants_list}
    return render(request, "restaurants/index.html", context)

def restaurant_detailed(request, restaurant_id):
    try:
        restaurant_detailed = Restaurant.objects.get(pk=restaurant_id)
        #restaurant_item = Item.objects.get(item_seller=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist.")
    return render(request, "restaurants/detailed.html", {"restaurant_detailed": restaurant_detailed})

def restaurant_menu(request, restaurant_id):
    return HttpResponse("You're looking at the menu for restaurant %s." % restaurant_id)