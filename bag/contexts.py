from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Cd


def bag_contents(request):

    bag_items = []
    total = 0
    cd_count = 0
    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        cd = get_object_or_404(Cd, pk=item_id)
        total += quantity * cd.price
        cd_count += quantity
        bag_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "cd": cd,
            })

    if cd_count < settings.FREE_DELIVERY_THRESHOLD and cd_count > 0:
        delivery = Decimal(settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - cd_count
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "bag_items": bag_items,
        "total": total,
        "cd_count": cd_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
