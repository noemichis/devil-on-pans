from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Item, Category, Allergen
from .forms import ItemForm, AllergenForm


def all_items(request):
    """
    View that returns all the items
    """

    items = Item.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Please enter a search criteria!"
                )
                return redirect(reverse('items'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
            items = items.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'items': items,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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


@login_required
def add_item(request):
    """ Add an item to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(
                request,
                'Failed to add item. Please ensure the form is valid.'
                )
    else:
        form = ItemForm()

    template = 'items/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_item(request, item_id):
    """ Edit an item on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(
                request,
                'Failed to update item. Please ensure the form is valid.'
                )
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'items/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_item(request, item_id):
    """ Delete an item from the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('items'))


@login_required
def create_allergen(request):
    """ Create an allergen from the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    allergens = Allergen.objects.all()
    if request.method == 'POST':
        allergen_form = AllergenForm(request.POST, request.FILES)
        if allergen_form.is_valid():
            messages.success(request, 'Successfully added allergen!')
            allergen_form.save()
        else:
            messages.error(
                request,
                'Failed to add allergen. Please ensure the form is valid.'
                )
    else:
        allergen_form = AllergenForm()

    template = 'items/create_allergen.html'
    context = {
        'allergens': allergens,
        'allergen_form': allergen_form,
    }

    return render(request, template, context)


@login_required
def delete_allergen(request, allergen_id):
    """ Delete an allergen from the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    allergen = get_object_or_404(Allergen, pk=allergen_id)
    allergen.delete()
    messages.success(request, 'Allergen deleted!')
    return redirect(reverse('create_allergen'))
