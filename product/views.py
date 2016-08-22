from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductList(ListView):
    model = Product
    #context_object_name = 'my_favorite_publishers'
    template_name = '/product/list.html'


class ProductDetail(DetailView):
    model = Product
    #template_name = '/product/product_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['product_list'] = Product.objects.all()
        return context
