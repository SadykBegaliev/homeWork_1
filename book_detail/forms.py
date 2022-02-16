from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book_detail
        fields = '__all__'
