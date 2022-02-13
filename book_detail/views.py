from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models

# Create your views here.
def get_book_detail(request):
    detail = models.Book_detail.objects.all()
    return render(request, "detail_list.html", {"detail": detail})

def get_book_detail2(request, id):
    details = get_object_or_404(models.Book_detail, id=id)
    return render(request,"all_detail.html", {"details": details})

