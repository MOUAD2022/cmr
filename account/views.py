from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request ,'account/index.html')
def Products(request):
    return HttpResponse('Products')
def Customer(request):
    return HttpResponse('Customer')