# Generated by Django 2.1.3 on 2018-11-28 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_auto_20181125_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
