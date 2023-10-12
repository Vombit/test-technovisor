from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from random import randint
from django.shortcuts import get_object_or_404

def index(request):
    dates = Order.objects.values_list('date', flat=True).distinct()
    staffers = Staffer.objects.all()
    
    context = {
        'dates': dates,
        'staffers': staffers,
    }
    
    return render(request, 'corporate_food/base.html', context)
    


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
    form = OrderForm()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            staffer = form.cleaned_data['staffer']
            date = form.cleaned_data['date']
            dishes = form.cleaned_data['dishes']
            
            selected_dish_ids = form.cleaned_data['dishes']
            selected_dishes = Dish.objects.filter(pk__in=selected_dish_ids)
            
            order = Order.objects.create(staffer=staffer, date=date)

            for dish in selected_dishes:
                Order_Dish.objects.create(order=order, dish=dish)

            return redirect('')

    else:
        dishes = Dish.objects.all()
        return render(request, 'corporate_food/order.html', {'form': form, 'dishes': dishes})


def report(request, date):
    orders = Order.objects.filter(date=date)
    order_dishes=[]
    total_sum = 0
    
    for order in orders:
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