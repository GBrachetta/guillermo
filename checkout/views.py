from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There's nothing in your bag yet.")
        return redirect(reverse("shop"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51FFigNKZb5qTUkA0O38c6pEm9sgJ4YVEvJU05ZblVHcFy7SB7dMnEBQBm0sChReJxPUrNJXJO7evtfVoV8QUy6k900B35D0E3t",
        "client_secret": "My deep secret!",
    }

    return render(request, template, context)
