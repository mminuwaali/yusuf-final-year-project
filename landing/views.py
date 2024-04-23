from .decorators import role_required
from django.shortcuts import render


@role_required
def about_view(request):
    return render(request, "landing/about.html")


@role_required
def contact_view(request):
    return render(request, "landing/contact.html")


@role_required
def index_view(request):
    return render(request, "landing/index.html")
