from django.shortcuts import render
from django.views.generic import TemplateView


class ShopFinderTemplateView(TemplateView):
    template_name = 'shop_finder/shop_finder.html'

