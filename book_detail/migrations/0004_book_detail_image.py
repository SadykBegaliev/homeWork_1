# Generated by Django 4.0.2 on 2022-02-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_detail', '0003_rename_create_date_showcomment_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_detail',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
