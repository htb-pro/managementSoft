# Generated by Django 4.2.3 on 2023-09-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_App', '0029_alter_spending_devise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='devise',
            field=models.CharField(choices=[('fr', 'FC'), ('usd', 'USD')], max_length=50, verbose_name='Devise'),
        ),
    ]
