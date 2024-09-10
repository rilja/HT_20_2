from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'cost', 'created_at', 'updated_at', 'category')
    success_url = reverse_lazy('products:catalog_home')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()

        return super().form_valid(form)


# class ProductDeleteView(DeleteView):
#     model = Product
#     success_url = reverse_lazy('product:list')
