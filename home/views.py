
from django.views.generic import TemplateView

from product.models import Product


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            'products'] = Product.objects.all()  # Obține toate produsele și le trimite către șablonul HTML
        return context



