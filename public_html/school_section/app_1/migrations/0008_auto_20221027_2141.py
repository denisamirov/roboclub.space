# Generated by Django 3.0.2 on 2022-10-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0007_registration_date_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date_registration',
            field=models.DateField(auto_now_add=True, verbose_name='registration date'),
        ),
    ]