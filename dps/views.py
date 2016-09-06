from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# Create your views here.
from .models import WorkOrder
from .forms import WorkorderDetailForm

from ship.models import Customer
from basic.models import Product,OrderCategory, ZmmsOption, MaterialCtrlOption

class WorkorderList(ListView):
    model = WorkOrder



class WorkorderDetail(DetailView):
    model = WorkOrder

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WorkorderDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['workorder_list'] = WorkOrder.objects.all()
        return context



class WorkorderCreate(CreateView):
    model = WorkOrder

    fields=[ 'category', 'recevice_date', 'material_ctrl', 'ships_order' ,'customer',
             'work_order', 'product', 'ord_amount', 'deliverly', 'reuqest_user',
             'material_duty', 'manage_memo'  ]
             
    success_url = '/dps'




class WorkorderUpdate(UpdateView):
    model = WorkOrder









    success_url = '/product'
