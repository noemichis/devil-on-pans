from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import HirePackage
from .forms import HireForm

from profiles.models import UserProfile


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
    initial_package = {
        'hire_package': hire_package,
    }

    if request.method == 'POST':
        hire_form = HireForm(request.POST, request.FILES)
        if hire_form.is_valid():
            hire_request = hire_form.save(commit=False)
            hire_request.hire_package = hire_package
            hire_form.save()
            messages.success(request, 'Successfully Sent request!')
            return redirect('hire_packages')
        else:
            messages.error(
                request,
                'Failed to send request. Please ensure the form is valid.'
                )
    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                hire_form = HireForm(initial={
                    'email': profile.user.email,
                    'hire_package': hire_package,
                })
            except UserProfile.DoesNotExist:
                hire_form = HireForm(initial_package)
        else:
            hire_form = HireForm(initial_package)

    template = 'hire/hire_request.html'
    context = {
        'hire_form': hire_form,
        'hire_package': hire_package,
    }
    return render(request, template, context)
