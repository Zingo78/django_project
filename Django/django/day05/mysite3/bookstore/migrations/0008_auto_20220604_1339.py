# Generated by Django 2.2.12 on 2022-06-04 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_book_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
    ]
