from django.shortcuts import render, get_object_or_404
from .models import Cd


# Create your views here.
def shop(request):
    cds = Cd.objects.all
    context = {
        'cds': cds,
    }
    return render(request, 'shop/shop.html', context)


def cd_detail(request, cd_id):
    """ Renders cd details """

    cd = get_object_or_404(Cd, pk=cd_id)

    context = {
        "cd": cd,
    }

    return render(request, "shop/cd_details.html", context)
