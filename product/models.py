

from django.db import models

from category.models import Category


# Create your models here.
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default='Unknown Author')
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='product_images/', null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recommended_age = models.CharField(max_length=20, blank=True)
    language = models.CharField(max_length=50, default='English')
    publisher = models.CharField(max_length=255, default='Unknown Publisher')
    cover_type = models.CharField(max_length=50, default='Default Cover Type')
    page_count = models.IntegerField(blank=False),
    isbn = models.CharField(max_length=13, default='N/A')
    dimensions_length = models.DecimalField(max_digits=5, decimal_places=2,
                                            default=0.00)
    dimensions_height = models.DecimalField(max_digits=5, decimal_places=2,
                                            default=0.00)

    def __str__(self):
        return f'{self.title} {self.category}'
