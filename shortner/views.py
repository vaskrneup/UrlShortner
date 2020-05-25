from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from . import forms
from . import models


def shortner_view(request):
    if request.method == "POST":
        form = forms.LinkForm(request.POST)
        if form.is_valid():
            link = form.save()
            messages.success(request, f"your url is "
                                      f"http://localhost:8000/{link.token} "
                                      f"for {link.url}.")
            return redirect("shortner")
    else:
        form = forms.LinkForm()

    return render(
        request, template_name="shortner.html",
        context={
            "form": form,
        }
    )


def redirect_view(request, token):
    data = get_object_or_404(models.Link, token=token)
    url = data.url
    url = f"https://{url}" if url[:4] != "http" else url
    return redirect(url)
