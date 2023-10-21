from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from catering.models import Item


def view_bag(request):
    """
    View that returns the shopping bag
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified item to the shopping bag """

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if bag[item_id] + quantity > item.stock_nr:
            quantity = item.stock_nr
            messages.error(
                request,
                f"Sorry, seems like we don't that many { item.name } in stock"
                )
        else:
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated { item.name } quantity to {bag[item_id]}'
                )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added { item.name } to  bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the item in the bag"""

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {item.name} quantity to {bag[item_id]}'
            )
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {item.name} from bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    item = get_object_or_404(Item, pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id)
    messages.success(request, f'Removed all {item.name} from bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
