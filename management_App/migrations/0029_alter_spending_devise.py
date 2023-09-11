# Generated by Django 4.2.3 on 2023-09-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_App', '0028_spending_devise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='devise',
            field=models.CharField(choices=[('FC', 'fr'), ('USD', 'usd')], max_length=50, verbose_name='Devise'),
        ),
    ]
