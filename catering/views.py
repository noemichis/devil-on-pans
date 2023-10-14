from django.shortcuts import render
from .models import Item


def all_items(request):
    """
    View that returns all the items
    """

    items = Item.objects.all()

    context = {
      'items': items,
    }

    return render(request, 'items/items.html', context)
