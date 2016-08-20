from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import WorkOrder

class WorkorderList(ListView):
    model = WorkOrder
    template_name = 'workorder_list.html'


'''
class WorkorderDetail(DetailView):
    model = WorkOrder
    queryset = WorkOrder.objects.all()

    template_name = 'workorder_detail.html'

    def get_object(self):
        # Call the superclass
        object = super(WorkorderDetail, self).get_object()
        # Record the last accessed date
        object.modify = timezone.now()
        object.save()
        # Return the object
        return object
'''
