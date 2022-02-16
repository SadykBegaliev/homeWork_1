from django.urls import path
from . import views


app_name = "detail"

urlpatterns = [
    path('detail/', views.get_book_detail, name='detail'),
    path('detail/<int:id>/', views.get_book_detail2, name='details'),
    path('add-book/', views.add_show, name='add_book'),
]