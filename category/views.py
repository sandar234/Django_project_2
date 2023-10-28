import data
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, \
    DetailView

from category.filters import CategoryFilter
from category.forms import CategoryForm, CategoryUpdateForm
from category.models import Category


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_message = 'The category {name} has been successfully added!'
    success_url = reverse_lazy('list-of-category')

    def get_success_message(self, clened_data):
        return self.success_message.format(name=self.object.name)


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'category/list_of_category.html'
    model = Category
    context_object_name = 'all_categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_all_categories = Category.objects.all()
        filters = CategoryFilter(self.request.GET, queryset=get_all_categories)
        context['all_categories'] = filters.qs
        context['form_filters'] = filters.form
        return context



class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'category/update_category.html'
    model = Category
    form_class = CategoryUpdateForm
    success_message = 'The category {name} has been successfully updated!'
    success_url = reverse_lazy('list-of-category')

    def get_success_message(self, clened_data):
        return self.success_message.format(name=self.object.name)


class CategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_message = 'The category {name} has been successfully deleted!'
    success_url = reverse_lazy('list-of-category')

    def get_success_message(self, clened_data):
        return self.success_message.format(name=self.object.name)


class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'category/details_category.html'
    model = Category