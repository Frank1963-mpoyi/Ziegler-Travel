from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from .models import DriverLogsheet
from .forms import DriverLogsheetForm


#@login_required.
def logsheet_list_view(request):
    # Template name for rendering the HTML template
    template_name = 'logsheet/list_logsheet.html' 
    # Retrieve all DriverLogsheet objects from the database
    logsheet_queryset = DriverLogsheet.objects.all()
    # Create a context dictionary to pass data to the template
    context = {'logsheet_queryset': logsheet_queryset}
    # Render the template with the given context and return the response
    return render(request, template_name, context)

# Detail View
def view_driver_logsheet(request, pk):
    template_name = 'logsheet/view_driver_logsheet.html'
    # Retrieve the DriverLogsheet object with the given pk (primary key)
    logsheet = get_object_or_404(DriverLogsheet, pk=pk)
    return render(request, template_name, {'logsheet': logsheet})

# Create View
#@login_required
def create_driver_logsheet(request):
    # Template name for rendering the HTML template
    template_name = 'logsheet/create_driver_logsheet.html.html' 

    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = DriverLogsheetForm(request.POST or None)

        # Validate the form data
        if form.is_valid():
            # Check if a logsheet with the same information already exists
            driver_name = form.cleaned_data['driver_name']
            vehicule_type = form.cleaned_data['vehicule_type']
            time_out = form.cleaned_data['time_out']
            
            if DriverLogsheet.objects.filter(driver_name=driver_name, vehicule_type=vehicule_type, time_out=time_out).exists():
                # If a logsheet with the same information exists, display an error message
                form.add_error(None, 'A logsheet with the same information already exists.')
            else:
                # If the form is valid and no logsheet with the same information exists, save the logsheet object
                logsheet = form.save(commit=False)
                logsheet.user = request.user
                logsheet.save()

                # Redirect to the logsheet list view
                return redirect('logsheet_list_view')
    else:
        # If the request method is not POST, create a new form
        form = DriverLogsheetForm()

    # Render the template with the form and return the response
    return render(request, template_name, {'form': form})


# Update
def update_driver_logsheet(request, pk):
    template_name = 'logsheet/update_driver_logsheet.html'
    logsheet = get_object_or_404(DriverLogsheet, pk=pk)
    if request.method == 'POST':
        form = DriverLogsheetForm(request.POST, instance=logsheet)
        if form.is_valid():
            form.save()
            return redirect('logsheet_list_view')
    else:
        form = DriverLogsheetForm(instance=logsheet)
    return render(request, template_name, {'form': form})

# Delete 
def delete_driver_logsheet(request, pk):
    template_name = 'logsheet/delete_driver_logsheet.html'
    logsheet = get_object_or_404(DriverLogsheet, pk=pk)
    if request.method == 'POST':
        logsheet.delete()
        return redirect('logsheet_list_view')
    return render(request, template_name, {'logsheet': logsheet})
