from django.shortcuts import render
from ecomapp.models import product

from django.db.models import Q
# Create your views here.


def searchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains=query))
        return render(request,'serach.html',{'query':query,'products':products})