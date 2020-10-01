from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_cd(request):
    if not request.user.is_superuser:
        messages.error(request, "Space reserved to administrators.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = CdForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.save()
            messages.success(request, "CD Added")
            return redirect(reverse("cd_detail", args=[cd.id]))
        else:
            messages.error(
                request, "Failed to add CD. Please check your form."
            )
    else:
        form = CdForm()

    template = "shop/add_cd.html"
    context = {"form": form}

    return render(request, template, context)


@login_required
def edit_cd(request, cd_id):
    if not request.user.is_superuser:
        messages.error(request, "Space reserved to administrators.")
        return redirect(reverse("home"))

    cd = get_object_or_404(Cd, pk=cd_id)
    if request.method == "POST":
        form = CdForm(request.POST, request.FILES, instance=cd)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited CD.")
            return redirect(reverse("cd_detail", args=[cd.id]))
        else:
            messages.error(
                request,
                "Failed to edit the CD. Please make sure the form is valid.",
            )
    else:
        form = CdForm(instance=cd)
        messages.info(request, f"You are editing {cd.name}")

    template = "shop/edit_cd.html"
    context = {
        "form": form,
        "cd": cd,
    }

    return render(request, template, context)


@login_required
def delete_cd(request, cd_id):
    if not request.user.is_superuser:
        messages.error(request, "Space reserved to administrators.")
        return redirect(reverse("home"))

    cd = get_object_or_404(Cd, pk=cd_id)
    cd.delete()
    messages.success(request, "CD deleted.")
    return redirect(reverse("shop"))
