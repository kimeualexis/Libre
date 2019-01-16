# Generated by Django 2.1.5 on 2019-01-16 09:43

from django.db import migrations
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=isbn_field.fields.ISBNField(max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN'),
        ),
    ]
