from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Product

class ProductList(ListView):
    model = Product
    #context_object_name = 'my_favorite_publishers'



class ProductDetail(DetailView):
    model = Product
    #template_name = '/product/product_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['product_list'] = Product.objects.all()
        return context


class ProductCreate(CreateView):
    title = "Create New Product"
    model = Product
    fields = ['sap_no', 'product_desc', 'specification', 'image','height_field', 'width_field', 'category', 'cycle_status']



class ProductUpdate(UpdateView):
    model = Product
    fields = ['sap_no', 'product_desc', 'specification', 'image', 'height_field', 'width_field','category', 'cycle_status']
