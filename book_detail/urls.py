from django.urls import path
from . import views


app_name = "detail"

urlpatterns = [
    path('detail/', views.get_book_detail, name='detail'),
    path('detail/<int:id>/', views.get_book_detail2, name='details'),
    path('detail/<int:id>/update/', views.push_book_update, name='details_update'),
    path('detail/<int:id>/delete/', views.book_delete, name='details_delete'),
    path('add-book/', views.add_show, name='add_book'),
]