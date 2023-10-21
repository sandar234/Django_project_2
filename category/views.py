
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, \
    DetailView

from category.forms import CategoryForm, CategoryUpdateForm
from category.models import Category


class CategoryCreateView(CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('list-of-category')


class CategoryListView(ListView):
    template_name = 'category/list_of_category.html'
    model = Category
    context_object_name = 'all_categories'


class CategoryUpdateView(UpdateView):
    template_name = 'category/update_category.html'
    model = Category
    form_class = CategoryUpdateForm
    success_url = reverse_lazy('list-of-category')


class CategoryDeleteView(DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_url = reverse_lazy('list-of-category')


class CategoryDetailView(DetailView):
    template_name = 'category/details_category.html'
    model = Category