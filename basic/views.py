from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from . import models

# Create your views here.
def product_desc(request,id):

    obj = get_object_or_404( Product, id=id)
    print(obj.sap_no)
    return render(request, "ajax_product.html", locals())
