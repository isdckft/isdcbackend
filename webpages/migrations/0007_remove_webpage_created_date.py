# Generated by Django 2.1.3 on 2018-11-28 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_remove_webpage_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='created_date',
        ),
    ]