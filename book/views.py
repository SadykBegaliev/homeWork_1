from django.shortcuts import render
from . import models

# Create your views here.

def post_all(request):
    post = models.Book.objects.all()
    return render(request, "post_list.html", {"post": post})
