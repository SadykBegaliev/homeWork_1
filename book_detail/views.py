from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models, forms
from django.shortcuts import reverse, redirect
from django.http import Http404, HttpResponse
from django.views import generic

class BooksListView(generic.ListView):
    template_name = "detail_list.html"
    queryset = models.Book_detail.objects.all()

    def get_queryset(self):
        return self.queryset


# def get_book_detail(request):
#     detail = models.Book_detail.objects.filter().order_by("-id")
#     return render(request, "detail_list.html", {"detail": detail})

class BookDetailView(generic.DetailView):
    template_name = "all_detail.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book_detail, id=book_id)

# def get_book_detail2(request, id):
#     details = get_object_or_404(models.Book_detail, id=id)
#     return render(request,"all_detail.html", {"details": details})

class BookCreateView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.Book_detail.objects.all()
    success_url = "/detail/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


# def add_show(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("detail:detail"))
#             # return HttpResponse("Show Created Successfully")
#     else:
#         form = forms.BookForm()
#     return render(request, "add_book.html",{"form":form})


class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/detail/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book_detail, id=book_id)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)

# def push_book_update(request, id):
#     book_id = get_object_or_404(models.Book_detail, id=id)
#     if request.method == "POST":
#         form = forms.BookForm(instance=book_id,
#                               data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("detail:detail"))
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, "book_update.html", {"form": form,
#                                                 "book": book_id})

class BookDeleteView(generic.DeleteView):
    template_name = "confirm_delete_book.html"
    success_url = "/detail/"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Book_detail, id=shows_id)

def book_delete(request, id):
    book_id = get_object_or_404(models.Book_detail, id=id)
    book_id.delete()
    # return HttpResponse("Book Deleted")
    return redirect(reverse("detail:detail"))


