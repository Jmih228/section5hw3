# Generated by Django 4.2.6 on 2023-11-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verificated',
            field=models.BooleanField(default=False, verbose_name='Подтверждение почты'),
        ),
    ]
