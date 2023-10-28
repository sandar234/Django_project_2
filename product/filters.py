import django_filters
from django import forms

from product.models import Product


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title',
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control'}))
    author = django_filters.CharFilter(lookup_expr='icontains', label='Author',
                                       widget=forms.TextInput(
                                           attrs={'class': 'form-control'}))
    price = django_filters.NumberFilter(label='Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    in_stock = django_filters.BooleanFilter(label='In stock',
                                            widget=forms.NumberInput(attrs={
                                                'class': 'form-control'}))
    recommended_age = django_filters.NumberFilter(label='Recommended age',
                                                  widget=forms.NumberInput(
                                                      attrs={
                                                          'class': 'form-control'}))
    language = django_filters.CharFilter(lookup_expr='icontains',
                                         label='Language',
                                         widget=forms.TextInput(
                                             attrs={'class': 'form-control'}))
    publication_date = django_filters.DateFilter(
        label='Publication date',
        widget=forms.DateInput(
            attrs={'class': 'form-control'}))
    publisher = django_filters.CharFilter(lookup_expr='icontains',
                                          label='Publisher',
                                          widget=forms.TextInput(
                                              attrs={'class': 'form-control'}))
    cover_type = django_filters.CharFilter(lookup_expr='icontains',
                                           label='Cover type',
                                           widget=forms.TextInput(
                                               attrs={'class': 'form-control'}))
    page_count = django_filters.NumberFilter(label='Page count',
                                             widget=forms.NumberInput(attrs={
                                                 'class': 'form-control'}))
    isbn = django_filters.NumberFilter(label='I.S.B.N.',
                                       widget=forms.NumberInput(attrs={
                                           'class': 'form-control'}))
    dimensions_length = django_filters.NumberFilter(label='Dimensions length',
                                                    widget=forms.NumberInput(
                                                        attrs={
                                                            'class': 'form-control'}))
    dimensions_height = django_filters.NumberFilter(label='Dimensions height',
                                                    widget=forms.NumberInput(
                                                        attrs={
                                                            'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['title', 'author', 'price', 'in_stock',
                  'recommended_age', 'language', 'publication_date',
                  'publisher', 'cover_type', 'page_count', 'isbn',
                  'dimensions_length', 'dimensions_height']
