# Generated by Django 3.1.5 on 2021-01-28 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieSearchApp', '0002_review_movietitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviewScroe',
            new_name='reviewScore',
        ),
    ]
