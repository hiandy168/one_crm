# Generated by Django 3.0.8 on 2020-07-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20200711_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='职称'),
        ),
    ]