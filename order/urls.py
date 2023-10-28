from django.urls import path

from order import views

urlpatterns = [
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('cart_list/', views.CartListView.as_view(), name='cart-list'),
]