import data
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, \
    DetailView

from product.filters import ProductFilter
from product.forms import ProductForm, ProductUpdateForm
from product.models import Product


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_message = 'The product {title} has been successfully added!'
    success_url = reverse_lazy('list-of-products')

    def get_success_message(self, clened_data):
        return self.success_message.format(title=self.object.title)


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_all_products = Product.objects.all()
        filters = ProductFilter(self.request.GET, queryset=get_all_products)
        context['all_products'] = filters.qs
        context['form_filters'] = filters.form
        return context


class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductUpdateForm
    success_message = 'The product {title} has been successfully updated!'
    success_url = reverse_lazy('list-of-products')

    def get_success_message(self, clened_data):
        return self.success_message.format(title=self.object.title)


class ProductDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_message = 'The product {title} has been successfully updated!'
    success_url = reverse_lazy('list-of-products')

    def get_success_message(self, clened_data):
        return self.success_message.format(title=self.object.title)


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'product/details_product.html'
    model = Product



def products_by_category(request, pk):
    products = Product.objects.filter(category_id=pk)
    return render(request, 'product/products_by_category.html', {'products': products})

