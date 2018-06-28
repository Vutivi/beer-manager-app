# Generated by Django 2.0.6 on 2018-06-28 02:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerapp', '0005_auto_20180628_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='abv',
            field=models.FloatField(default=4.5, validators=[django.core.validators.MaxValueValidator(4.5), django.core.validators.MinValueValidator(6.2)]),
        ),
        migrations.AlterField(
            model_name='beer',
            name='calories',
            field=models.IntegerField(default=64, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(198)]),
        ),
        migrations.AlterField(
            model_name='beer',
            name='ibu',
            field=models.IntegerField(default=30, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(50)]),
        ),
    ]