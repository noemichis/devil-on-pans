from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import HirePackage
from .forms import HireForm


def get_packages(request):
    """
    View that returns all the packages
    """
    hire_packages = HirePackage.objects.all()

    template = 'hire/hire_packages.html'
    context = {
        'hire_packages': hire_packages,
    }

    return render(request, template, context)

def create_hire_request(request, hire_package_id):
    """
    View that handles the hire request
    """
    hire_package = get_object_or_404(HirePackage, pk=hire_package_id)

    if request.method == 'POST':
        hire_form = HireForm(request.POST, request.FILES)
        if hire_form.is_valid():
            hire_form.save()
            messages.success(request, 'Successfully Sent request!')
            return redirect('hire_packages')
        else:
            messages.error(
                request,
                'Failed to send request. Please ensure the form is valid.'
                )
    else:
        hire_form = HireForm()

    template = 'hire/hire_request.html'
    context = {
        'hire_form': hire_form,
        'hire_package': hire_package,
    }
    return render(request, template, context)
