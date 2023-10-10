from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from random import randint

def index(request):

    # return render(request, 'index.html')
    return JsonResponse({'message':'test'}, safe=False)


def history(request):
    return JsonResponse({'message':'test'}, safe=False)


def order(request):
    return JsonResponse({'message':'test'}, safe=False)


def report(request, date):

    return JsonResponse({'message':'test'}, safe=False)
