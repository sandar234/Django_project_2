from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Review
from .forms import ReviewForm
from product.models import Product

def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()

            # Actualizează scorul mediu și numărul total de evaluări pentru produs
            product.total_ratings += 1
            product.average_rating = (product.average_rating * (product.total_ratings - 1) + review.rating) / product.total_ratings
            product.save()
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'product': product, 'reviews': reviews, 'form': form})

