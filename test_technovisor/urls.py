from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', include('corporate_food.urls', namespace='corporate_food'))
]