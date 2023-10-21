from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, \
    DetailView

from product.forms import ProductForm, ProductUpdateForm
from product.models import Product


class ProductCreateView(CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list-of-products')


class ProductListView(ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'


class ProductUpdateView(UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('list-of-products')


class ProductDeleteView(DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('list-of-products')


class ProductDetailView(DetailView):
    template_name = 'product/details_product.html'
    model = Product

