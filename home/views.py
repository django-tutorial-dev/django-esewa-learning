from django.shortcuts import render,get_object_or_404

from .models import Product, Transaction



def index(request):
    products = Product.objects.all()
    context={
        'products': products
        }
    return render(request, 'index.html',context)

def buy(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'buy.html',context )