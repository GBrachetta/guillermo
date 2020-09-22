from django.shortcuts import render
from .models import Cd


# Create your views here.
def shop(request):
    cds = Cd.objects.all
    context = {
        'cds': cds,
    }
    return render(request, 'shop/shop.html', context)
