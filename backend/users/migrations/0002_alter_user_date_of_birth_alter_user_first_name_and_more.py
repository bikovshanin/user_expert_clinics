# Generated by Django 5.1 on 2024-08-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес регистрации'),
        ),
    ]
