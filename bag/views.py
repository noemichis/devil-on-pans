from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from catering.models import Item


def view_bag(request):
    """
    View that returns the shopping bag
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified item to the shopping bag """

    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added { item.name } to  bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the item in the bag"""

    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {item.name} in bag')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {item.name} from bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    item = Item.objects.get(pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id)
    messages.success(request, f'Removed {item.name} from bag')

    request.session['bag'] = bag
    return HttpResponse(status=200)
