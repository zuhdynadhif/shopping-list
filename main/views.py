from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product

def show_main(request):
    #  import Product dari models
    products = Product.objects.all()

    context = {
        'name': 'Zuhdy Nadhif Ayyasy',
        'class': 'PBP C',
        'products': products
    }
    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect('main:show_main')
    context = {'form':form}
    return render(request, "create_product.html", context)