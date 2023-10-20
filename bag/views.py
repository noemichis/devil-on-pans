from django.shortcuts import render


def view_bag(request):
    """
    View that returns the shopping bag
    """

    return render(request, 'bag/bag.html')
