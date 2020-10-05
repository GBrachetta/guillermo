from django.shortcuts import render


# Create your views here.
def events(request):
    context = {"events": "active"}
    return render(request, "events/events.html", context)
