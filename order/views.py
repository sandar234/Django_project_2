from datetime import datetime
from pprint import pprint
from random import randint
from urllib import request

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from order.forms import PlaceOrderForm
from order.models import OrderCart, PlaceOrder
from product.models import Product


@login_required()
def add_to_cart(request, pk):
    # verificam daca produsul este in cosul de cumparaturi
    if OrderCart.objects.filter(user_id=request.user.id,
                                product_id=pk).exists():
        current = OrderCart.objects.get(product_id=pk, user_id=request.user.id)
        quantity = current.quantity + 1

        amount = current.product.price * quantity
        OrderCart.objects.filter(user_id=request.user.id,
                                 product_id=pk).update(quantity=quantity,
                                                       amount=amount)
    else:
        # adauga produsul in cosul de cumparaturi
        quantity = 1
        current = Product.objects.get(id=pk)

        amount = current.price * 1
        OrderCart.objects.create(
            user_id=request.user.id,
            product_id=pk,
            cart_item=True,
            quantity=quantity,
            amount=amount,
            created_at=datetime.now()
        )
    messages.success(request, f"Product added to the cart successfully.")

    return redirect('products-by-category', pk)


@login_required()
def increase_quantity(request, pk):
    cart_product = get_object_or_404(OrderCart, product_id=pk,
                                     user_id=request.user.id)
    cart_product.quantity += 1
    cart_product.amount = cart_product.product.price * cart_product.quantity
    cart_product.save()
    return redirect('cart-list')


@login_required()
def decrease_quantity(request, pk):
    cart_product = get_object_or_404(OrderCart, product_id=pk,
                                     user_id=request.user.id)
    if cart_product.quantity > 1:
        cart_product.quantity -= 1
        cart_product.amount = cart_product.product.price * cart_product.quantity
        cart_product.save()
    else:
        cart_product.delete()
    return redirect('cart-list')


class CartListView(ListView):
    """
        The CartListView class represents a view for the shopping cart.

        Class Attributes:
        - template_name: The HTML template name for displaying the list.
        - model: The data model associated with this view (OrderCart).
        - context_object_name: The name through which objects in the list are accessed in the template.

        Methods:
        - get_queryset: Returns a filtered queryset of OrderCart objects based on cart_item and user_id.
        - get_context_data: Calculates the total amounts in the shopping cart and adds it to the view's context.
        """
    template_name = 'order/cart_list.html'
    model = OrderCart
    context_object_name = 'cart_products'

    def get_queryset(self):
        """
                Returns a filtered queryset of OrderCart objects.
                Filtering is based on cart_item and user_id.
                """
        result = (
            OrderCart.objects.filter(cart_item=1, user_id=self.request.user.id))
        return result

    def get_context_data(self, **kwargs):
        """
                Calculates the total amounts in the shopping cart and adds it to the view's context.
                """
        context = super().get_context_data(**kwargs)
        total_amount = 0
        for cart_product in context['cart_products']:
            total_amount += (cart_product.amount)
        context['total_amount'] = total_amount
        return context


def add_to_wishlist(request, pk):
    """
       View function to add a product to the user's wishlist.

       Parameters:
       - request: The HTTP request object.
       - pk: The primary key of the product to be added to the wishlist.

       Logic:
       - Check if the product is already in the shopping cart.
       - If yes, update the existing entry to mark it as a wishlist item.
       - If not, create a new entry in the shopping cart with wishlist_item set to True.

       Messages:
       - Display a success message after adding the product to the wishlist.

       Redirect:
       - Redirect the user to the 'products-by-category' view for the specified category after the operation.
       """
    # verificam daca produsul este in cosul de cumparaturi
    if OrderCart.objects.filter(user_id=request.user.id,
                                product_id=pk).exists():

        OrderCart.objects.filter(user_id=request.user.id,
                                 product_id=pk).update(wishlist_item=True)

    else:
        # adauga produsul in cosul de cumparaturi
        OrderCart.objects.create(
            user_id=request.user.id,
            product_id=pk,
            cart_item=False,
            wishlist_item=True,
            quantity=1,
            amount=Product.objects.get(id=pk).price,
            created_at=datetime.now()
        )
    messages.success(request, f"Product added to the wishlist successfully.")
    return redirect('products-by-category', pk)


class ListViewWishList(ListView):
    template_name = 'order/wish_list.html'
    model = OrderCart
    context_object_name = 'wish_lists'

    def get_queryset(self):
        result = (OrderCart.objects.filter(wishlist_item=1,
                                           user_id=self.request.user.id))
        return result


@login_required()
def delete_from_cart(request, pk):
    if OrderCart.objects.filter(user_id=request.user.id, id=pk,
                                wishlist_item=1).exists():
        OrderCart.objects.filter(user_id=request.user.id, id=pk).update(
            cart_item=0)
        return redirect('cart-list')
    else:
        OrderCart.objects.filter(user_id=request.user.id, id=pk).delete()
        return redirect('cart-list')


@login_required()
def delete_from_wishlist(request, pk):
    if OrderCart.objects.filter(user_id=request.user.id, id=pk,
                                cart_item=1).exists():
        OrderCart.objects.filter(user_id=request.user.id, id=pk).update(
            wishlist_item=0)
        return redirect('wish-list')
    else:
        OrderCart.objects.filter(user_id=request.user.id, id=pk).delete()
        return redirect('wish-list')


@login_required()
def move_favorites_to_cart(request, pk):
    """
        View function to move a product from the wishlist to the shopping cart.

        Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the wishlist item to be moved to the cart.

        Logic:
        - Retrieve the current wishlist item based on the provided primary key.
        - Calculate the total amount for the quantity of the product.
        - Update the current wishlist item to mark it as a cart item and update the amount.
        - Display a success message after moving the product to the cart.

        Redirect:
        - Redirect the user to the 'cart-list' view after the operation.
        """
    current_order = OrderCart.objects.get(user_id=request.user.id, id=pk)
    amount = current_order.quantity * current_order.product.price
    OrderCart.objects.filter(user_id=request.user.id, id=pk).update(cart_item=1,
                                                                    wishlist_item=1,
                                                                    amount=amount)
    messages.success(request, f"Product added to the cart successfully.")

    return redirect('cart-list')


class PlaceOrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'order/place_order.html'
    model = PlaceOrder
    form_class = PlaceOrderForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        if form.is_valid():
            new_order = form.save(commit=False)

            # user_id
            new_order.user_id = self.request.user.id

            # order number
            generic_order = randint(1, 100)
            new_order.order_number = f'ESHOP_{generic_order}'

            # product list
            products = {'data': []}
            final_price = 0
            products_per_user = OrderCart.objects.filter(
                user_id=self.request.user.id, cart_item=1)

            for item in products_per_user:
                products['data'].append({'title': item.product.title,
                                         'quantity': item.quantity,
                                         'price': f'{item.product.price * item.quantity}'
                                         })

                final_price += item.product.price * item.quantity
            new_order.product_list = products
            pprint(products)

            # price
            new_order.price = final_price

            # invoice_address

            new_order.invoice_address = new_order.delivery_address

            # created_at

            new_order.created_at = datetime.now()

            new_order.save()

            return redirect('home_page')
