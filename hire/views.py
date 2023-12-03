from django.shortcuts import render

from .models import HirePackage


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