# Generated by Django 2.0.6 on 2018-06-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerapp', '0008_auto_20180628_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='overall',
            field=models.FloatField(default=0.0),
        ),
    ]