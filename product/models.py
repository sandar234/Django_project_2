from django.db import models

from category.models import Category


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='product_images/', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recommended_age = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=50, null=True)
    publication_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True)
    cover_type = models.CharField(max_length=50, null=True)
    page_count = models.IntegerField(null=True)
    isbn = models.CharField(max_length=13, null=True)
    dimensions_length = models.DecimalField(max_digits=5, decimal_places=2,
                                            null=True, blank=True)
    dimensions_height = models.DecimalField(max_digits=5, decimal_places=2,
                                            null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.category}'
