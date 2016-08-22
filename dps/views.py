from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import WorkOrder
from .forms import WorkorderDetailForm

class WorkorderList(ListView):
    model = WorkOrder
    template_name = 'workorder_list.html'


class WorkorderDetail(DetailView):
    model = WorkOrder

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WorkorderDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['workorder_list'] = WorkOrder.objects.all()
        return context
