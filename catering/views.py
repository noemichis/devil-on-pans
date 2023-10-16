from django.shortcuts import render, get_object_or_404
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


def item_detail(request, item_id):
    """
    View that returns individual catering items
    """

    item = get_object_or_404(Item, pk=item_id)

    context = {
      'item': item,
    }

    return render(request, 'items/item_detail.html', context)
