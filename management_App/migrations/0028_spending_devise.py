# Generated by Django 4.2.3 on 2023-09-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_App', '0027_alter_spending_motif'),
    ]

    operations = [
        migrations.AddField(
            model_name='spending',
            name='devise',
            field=models.CharField(choices=[('FC', 'fr'), ('USD', 'usd')], default='', max_length=50),
            preserve_default=False,
        ),
    ]