# Generated by Django 3.0.2 on 2022-06-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Наименование'),
        ),
    ]
