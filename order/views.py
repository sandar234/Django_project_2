



from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from order.models import OrderCart

@login_required()
def add_to_cart(request, pk):
    if OrderCart.objects.filter(user_id=request.user.id,
                                product_id=pk).exists():
        quantity = OrderCart.objects.get(user_id=request.user.id,
                                product_id=pk).quantity
    else:
        quantity = 1

    # verificam daca produsul este in cosul de cumparaturi
    if OrderCart.objects.filter(user_id=request.user.id,
                                product_id=pk).exists():
        quantity += 1
        OrderCart.objects.filter(user_id=request.user.id,
                                 product_id=pk).update(quantity=quantity)
    else:
        # adauga produsul in cosul de cumparaturi
        OrderCart.objects.create(
            user_id=request.user.id,
            product_id=pk,
            cart_item=True,
            quantity=quantity,
            created_at=datetime.now()
        )

    return redirect('home_page')


class CartListView(ListView):
    template_name = 'order/cart_list.html'
    model = OrderCart
    context_object_name = 'cart_products'

    def get_queryset(self):
        return OrderCart.objects.filter(cart_item=1)
