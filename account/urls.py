from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('Products/', views.Products),
    path('Customer/', views.Customer),

]
