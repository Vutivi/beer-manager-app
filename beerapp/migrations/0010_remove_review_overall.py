# Generated by Django 2.0.6 on 2018-06-28 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beerapp', '0009_review_overall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='overall',
        ),
    ]