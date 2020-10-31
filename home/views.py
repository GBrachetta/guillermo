from django.shortcuts import render


# Create your views here.
def home(request):
    """ renders the landing page """
    context = {"home": "active"}
    return render(request, "home/home.html", context)
