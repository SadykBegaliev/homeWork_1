from django.urls import path
from . import views, models


app_name = "detail"

urlpatterns = [
    path('detail/', views.BooksListView.as_view(), name='detail'),
    path('detail/fantasy/', views.BooksListView.as_view(queryset=models.Book_detail.objects.filter(genre="Фэнтези").order_by("-created_date")), name='detail'),
    path('detail/novel/', views.BooksListView.as_view(queryset=models.Book_detail.objects.filter(genre="Роман").order_by("-created_date")), name='detail'),
    path('detail/action/', views.BooksListView.as_view(queryset=models.Book_detail.objects.filter(genre="Боевик").order_by("-created_date")), name='detail'),
    path('detail/<int:id>/', views.BookDetailView.as_view(), name='details'),
    path('detail/<int:id>/update/', views.BookUpdateView.as_view(), name='details_update'),
    path('detail/<int:id>/delete/', views.BookDeleteView.as_view(), name='details_delete'),
    path('add-book/', views.BookCreateView.as_view(), name='add_book'),
]