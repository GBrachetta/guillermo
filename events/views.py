from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def events(request):
    """ Displays all events """
    events = Event.objects.all().order_by("date")
    context = {"calendar": events, "events": "active"}
    return render(request, "events/events.html", context)


@login_required
def add_event(request):
    """Allows admins to add events"""
    if not request.user.is_superuser:
        messages.error(request, "Only administrators can access this url.")
        return redirect(reverse("events"))

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event added.")
            return redirect(reverse("events"))
        else:
            messages.error(
                request, "Failed to add event. Please check your form."
            )
    else:
        form = EventForm()
    template = "events/add_event.html"
    context = {
        "form": form,
        "events": "active",
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """Allows admins to edit events"""
    event = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Your event has been updated.")
            return redirect("events")
        else:
            messages.error(request, "Please check the information submitted.")
    else:
        form = EventForm(instance=event)
        messages.info(request, f"You are editing {event.name}")
    template = "events/edit_event.html"
    context = {
        "form": form,
        "event": event,
        "events": "active",
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """Allows admins to delete events"""
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, "Event deleted.")
    return redirect(reverse("events"))
