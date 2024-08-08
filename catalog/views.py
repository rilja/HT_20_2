from django.shortcuts import render

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"product_list": products}
    return render(request, 'catalog/product_list.html', context)
