from django import forms
from .models import Product


class ProductCreateForm(forms.ModelForm):
    context={title:"Create New Product"}
    model = Product
    exclude = ('create_at','modify' )
