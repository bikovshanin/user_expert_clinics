# Generated by Django 5.1 on 2024-08-21 07:45

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id', 'email'), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None, unique=True, verbose_name='Номер телефона'),
        ),
    ]
