from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class OrderCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_item = models.BooleanField(default=False)
    wishlist_item = models.BooleanField(default=False)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True)


    def __str__(self):
        return self.product