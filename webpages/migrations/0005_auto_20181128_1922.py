# Generated by Django 2.1.3 on 2018-11-28 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpages', '0004_auto_20181128_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='webpage',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='date',
            field=models.DateField(),
        ),
    ]