# Generated by Django 3.0.2 on 2022-08-13 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_activated', models.BooleanField(db_index=True, default=False, verbose_name='Прошел активацию?')),
                ('telegram_acc', models.CharField(blank=True, max_length=50, verbose_name='Telegram')),
                ('is_teacher', models.BooleanField(db_index=True, default=False, verbose_name='Преподаватель')),
                ('email', models.EmailField(max_length=254, verbose_name='email adress')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='AdvUser',
        ),
    ]
