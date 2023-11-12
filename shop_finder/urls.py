from django.urls import path

from shop_finder import views

urlpatterns = [
    path('shop_finder', views.ShopFinderTemplateView.as_view(), name='shop-finder'),
]