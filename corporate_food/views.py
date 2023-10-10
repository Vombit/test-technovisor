from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from random import randint
from django.shortcuts import get_object_or_404

def index(request):
    
    return render(request, 'corporate_food/base.html')


def history(request, user_id):
    staffer = Staffer.objects.get(name = user_id)
    orders = Order.objects.filter(staffer = staffer)
    
    order_dishes={}
    for i, order in enumerate(orders):
        dish = Order_Dish.objects.filter(order = order)
        
        items = []
        for item in dish:
            items.append({ 
                'name': item.dish.name,
                'price': item.dish.price,
                },)
        order_dishes[f'{i+1}'] = items
        
    context = {
        'orders': order_dishes,
    }
    return render(request, 'corporate_food/history.html', context)


def order(request):
    dishes = Dish.objects.all()
    form = OrderForm(request.POST)
    
    context = {
        'form': form,
        'dishes': dishes,
    }
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('corporate_food:order')
        else:
            return render(request, 'corporate_food/order.html', context)
        
    return render(request, 'corporate_food/order.html', context)



def report(request, date):
    orders = Order.objects.filter(date=date)
    
    order_dishes=[]
    
    total_sum = 0
    counter = {}
    for i, order in enumerate(orders):
        dish = Order_Dish.objects.filter(order = order)
        
        for item in dish:
            total_sum += item.dish.price
            
            dishs = { 
                'name': item.dish.name,
                'price': item.dish.price,
                'count': 1,
                }
            order_dishes.append(dishs)
              
    result_dict = {}
    for item in order_dishes:
        name = item['name']
        if name in result_dict:
            result_dict[name]['count'] += item['count']
        else:
            result_dict[name] = item
    result_list = list(result_dict.values())


    context = {
        'report': result_list,
        'total': total_sum,
    }
    
    return render(request, 'corporate_food/report.html', context)
