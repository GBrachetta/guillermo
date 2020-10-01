from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Cd
from .forms import CdForm


# Create your views here.
def shop(request):
    cds = Cd.objects.all
    context = {
        "cds": cds,
    }
    return render(request, "shop/shop.html", context)


def cd_detail(request, cd_id):
    """ Renders cd details """

    cd = get_object_or_404(Cd, pk=cd_id)

    context = {
        "cd": cd,
    }

    return render(request, "shop/cd_details.html", context)


def add_cd(request):
    if request.method == "POST":
        form = CdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "CD Added")
            return redirect(reverse("add_cd"))
        else:
            messages.error(
                request, "Failed to add CD. Please check your form."
            )
    else:
        form = CdForm()

    template = "shop/add_cd.html"
    context = {"form": form}

    return render(request, template, context)
