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


def push_book_update(request, id):
    book_id = get_object_or_404(models.Book_detail, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_id,
                              data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("detail:detail"))
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, "book_update.html", {"form": form,
                                                "book": book_id})

def book_delete(request, id):
    book_id = get_object_or_404(models.Book_detail, id=id)
    book_id.delete()
    # return HttpResponse("Book Deleted")
    return redirect(reverse("detail:detail"))


