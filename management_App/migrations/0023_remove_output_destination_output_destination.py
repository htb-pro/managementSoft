# Generated by Django 4.2.3 on 2023-09-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_App', '0022_output_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='output',
            name='destination',
        ),
        migrations.AddField(
            model_name='output',
            name='destination',
            field=models.ManyToManyField(to='management_App.destination', verbose_name='Distribution'),
        ),
    ]