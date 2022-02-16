from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models, forms
from django.shortcuts import reverse, redirect
from django.http import Http404, HttpResponse

# Create your views here.
def get_book_detail(request):
    detail = models.Book_detail.objects.filter().order_by("-id")
    return render(request, "detail_list.html", {"detail": detail})

def get_book_detail2(request, id):
    details = get_object_or_404(models.Book_detail, id=id)
    return render(request,"all_detail.html", {"details": details})

def add_show(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("detail:detail"))
            # return HttpResponse("Show Created Successfully")
    else:
        form = forms.BookForm()
    return render(request, "add_book.html",{"form":form})

