# Generated by Django 4.2.3 on 2023-09-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_App', '0016_alter_command_destination_alter_output_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
