from django.urls import path
from . import views


urlpatterns = [
    path('detail/', views.get_book_detail, name='detail'),
    path('detail/<int:id>/', views.get_book_detail2, name='details'),
]