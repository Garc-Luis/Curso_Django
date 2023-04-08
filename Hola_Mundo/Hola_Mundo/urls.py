from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludos/', views.saludos, name='saludos'),
    path('despedida/', views.despedida, name='despedida')
]
