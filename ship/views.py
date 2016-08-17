from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import QuoteHead
from .forms import QuoteHeadCreateForm

# Create your views here.

def ship_list(request):
    title = "銷售管理"

    queryset_list = QuoteHead.objects.all()

    paginator = Paginator(queryset_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    print(queryset)
    footer = "this is Footer"

    return render(request, "ship_list.html", locals())


def create_header(request):
    title = "新增報價單"
    form = QuoteHeadCreateForm(request.POST or None)

    return render(request, "ship_header.html", locals())


def quote_detail(request, id):
    title = "報價單明細"
    record = get_object_or_404( QuoteHead, id=id)

    return render(request, "quote_detail.html", locals())
