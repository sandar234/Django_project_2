from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()  # Scorul evaluării (1-5 stele)
    created_at = models.DateTimeField(auto_now_add=True)

