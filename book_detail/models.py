from django.db import models

class Book_detail(models.Model):
    GENRE_CHOICE = (
        ('Фэнтези', 'Фэнтези'),
        ('Боевик', 'Боевик'),
        ('Драма', 'Драма'),
        ("Роман", "Роман"),
        ("Комедия", "Комедия")
    )
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=25)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=70, choices=GENRE_CHOICE)
    pages = models.PositiveIntegerField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    image = models.ImageField(null=True, upload_to='')

    def __str__(self):
        return self.name

class ShowComment(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    connect = models.ForeignKey(Book_detail, on_delete=models.CASCADE,
                                related_name="shows_comment")





