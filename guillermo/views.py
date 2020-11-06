from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


def handler404(request, exception):
    response = render(request, "errors/404.html")
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, "errors/500.html")
    response.status_code = 500
    return response


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            user_email = contact_form.cleaned_data["email"]
            message = contact_form.cleaned_data["message"]
            try:
                send_mail(
                    f"Message from {name}, <{user_email}>",
                    f"{name}, from {user_email}, says: '{message}'",
                    settings.EMAIL_HOST_USER,
                    [settings.DEFAULT_ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Your email was successfully sent.")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
    else:
        if request.user.is_authenticated:
            user_email = request.user.email
            contact_form = ContactForm(
                initial={
                    "name": request.user.username,
                    "email": user_email,
                }
            )
        else:
            contact_form = ContactForm()
    context = {
        "contact_form": contact_form,
    }
    return render(request, "includes/contact.html", context)
