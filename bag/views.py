from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404,
)
from django.contrib import messages
from shop.models import Cd


def view_bag(request):
    """
    Renders the template with bag contents
    """
    context = {"bag": "active"}
    return render(request, "bag/bag.html", context)


def add_to_bag(request, item_id):
    """
    Adds the item passed as second parameter to the shopping bag in the session
    """

    cd = get_object_or_404(Cd, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated "{cd.name}" amount to {bag[item_id]}'
        )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added "{cd.name}" to your bag.')

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjusts the quantity of the item passed as second parameter.
    """

    cd = get_object_or_404(Cd, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated "{cd.name}" amount to {bag[item_id]}'
        )
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed "{cd.name}" from your bag.')

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """
    Removes the item passed as second parameter from the shopping bag
    """

    try:
        cd = get_object_or_404(Cd, pk=item_id)
        bag = request.session.get("bag", {})
        bag.pop(item_id)
        messages.success(request, f'Removed "{cd.name}" from your bag.')

        request.session["bag"] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
