# Generated by Django 4.2.3 on 2023-09-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_App', '0013_alter_command_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='nomArticle',
            field=models.ManyToManyField(to='management_App.article', verbose_name='Article'),
        ),
    ]