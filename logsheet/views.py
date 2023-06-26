from django.views.generic import View
from django.shortcuts import render

from .models import DriverLogsheet
from .forms import DriverLogsheetForm


# Create your views here.
def logsheet_list_view(request):
    
    template_name = 'logsheet/list_logsheet.html'
    
    logsheet_queryset = DriverLogsheet.objects.all()
    
    context = {'logsheet_queryset': logsheet_queryset}
    
    return render(request, template_name, context)

# Detail View
# def logsheet_detail_view(request, pk):
    
#     template_name = 'logsheet/index.html'
    
#     logsheet_queryset = DriverLogsheet.objects.get(id=pk)
    
#     context = {'logsheet_queryset': logsheet_queryset}
    
#     return render(request, template_name, context)

#Update View
def logsheet_create_view(request):
    
    template_name = 'logsheet/create_logsheet.html'
    
    form = DriverLogsheetForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {'form': form}
    
    return render(request, template_name, context)
