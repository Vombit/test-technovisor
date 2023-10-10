from django.db import models
from django.utils import timezone


class Staffer(models.Model):
    name = models.CharField(max_length=24)
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        
    def __str__(self):
        return self.name




type_dish = (
    ('first', 'первое'),
    ('second', 'второе'),
    ('drink', 'напиток'),
    ('dessert', 'десерт'),
    ('snack', 'закуска'),
    )
class Dish(models.Model):
    name = models.CharField(max_length=128)
    composition = models.TextField(max_length=512)
    price = models.IntegerField()
    type_of_dish = models.CharField(max_length=30, choices=type_dish)
    calories = models.IntegerField()
      
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        
    def __str__(self):
        return self.name



class Order(models.Model):
    staffer = models.ForeignKey(Staffer, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
    def __str__(self):
        return f'{self.staffer.name} - {self.date}'



class Order_Dish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Блюдо заказа'
        verbose_name_plural = 'Блюда заказов'


    def __str__(self):
        return f'{self.order.staffer.name} - {self.order.date}'
    
