from django.urls import path

from order import views

urlpatterns = [
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('cart_list/', views.CartListView.as_view(), name='cart-list'),
    path('add_to_wishlist/<int:pk>/', views.add_to_wishlist, name='add-to-wishlist'),
    path('wish_list/', views.ListViewWishList.as_view(), name='wish-list'),
    path('delete_from_cart/<int:pk>/', views.delete_from_cart, name='delete-from-cart'),
    path('delete_from_wishlist/<int:pk>/', views.delete_from_wishlist, name='delete-from-wishlist'),
    path('increase_quantity/<int:pk>/', views.increase_quantity, name='increase-quantity'),
    path('decrease_quantity/<int:pk>/', views.decrease_quantity, name='decrease-quantity'),
    path('move_favorites_to_cart/<int:pk>/', views.move_favorites_to_cart, name='move-favorites-to-cart'),
    path('place_order/', views.PlaceOrderCreateView.as_view(), name='place-order'),
]