from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

app_name = 'corporate_food'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('order/', view=views.order, name='order'),
    
    path('history/<user_id>', view=views.history, name='history'),
    path('report/<date>', view=views.report, name='report'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
