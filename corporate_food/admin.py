from django.contrib import admin
from .models import *



@admin.register(Staffer)
class Staffer(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



@admin.register(Dish)
class Dish(admin.ModelAdmin):
    list_display = ('name', 'calories', 'type_of_dish', 'composition', 'price')
    search_fields = ('name', 'calories', 'type_of_dish')
    
    list_filter = ('type_of_dish', 'calories')


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('staffer', 'date_time')
    search_fields = ('staffer__name',)



@admin.register(Order_Dish)
class Order_Dish(admin.ModelAdmin):
    list_display = ('order', 'dish')
    search_fields = ('order', 'dish__name')
    
    list_filter = ('dish__name', 'dish__type_of_dish')