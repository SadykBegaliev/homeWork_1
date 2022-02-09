from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.post_all, name='books_list'),
]