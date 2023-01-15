# Generated by Django 3.0.2 on 2022-08-09 13:22

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_group', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': 'группа текстов',
                'verbose_name_plural': 'группы текстов',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='наименование предмета')),
            ],
            options={
                'verbose_name': 'наименование предмета',
                'verbose_name_plural': 'наименование предметов',
            },
        ),
        migrations.CreateModel(
            name='SClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='классы')),
            ],
            options={
                'verbose_name': 'класс',
                'verbose_name_plural': 'классы',
            },
        ),
        migrations.CreateModel(
            name='SpeedText',
            fields=[
                ('id_text', models.AutoField(primary_key=True, serialize=False, verbose_name='ID_text')),
                ('name_text', models.CharField(max_length=70, verbose_name='Название_текста')),
                ('text', models.TextField(verbose_name='Текст')),
                ('id_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_1.Group_text', verbose_name='Группа текстов')),
            ],
            options={
                'verbose_name': 'название текста',
                'verbose_name_plural': 'название текстов',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=256, verbose_name='промежутки времени')),
            ],
            options={
                'verbose_name': 'промежуток времени',
                'verbose_name_plural': 'промежутки времени',
            },
        ),
        migrations.CreateModel(
            name='Ways',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Направления')),
            ],
            options={
                'verbose_name': 'направление',
                'verbose_name_plural': 'направления',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('name_text', models.OneToOneField(db_column='name_text', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app_1.SpeedText')),
                ('q_1', models.CharField(blank=True, max_length=100, null=True)),
                ('a_11', models.CharField(blank=True, max_length=45, null=True)),
                ('a_12', models.CharField(blank=True, max_length=45, null=True)),
                ('a_13', models.CharField(blank=True, max_length=45, null=True)),
                ('a_14', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.IntegerField(blank=True, null=True, verbose_name='День недели_цифрой')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_1.SClass', verbose_name='номер класса')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_1.Lesson', verbose_name='ID урока')),
                ('time_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_1.Time', verbose_name='Время')),
            ],
            options={
                'verbose_name': 'расписание',
                'verbose_name_plural': 'расписания',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70, verbose_name='Имя ребёнка')),
                ('last_name', models.CharField(blank=True, max_length=70, verbose_name='Фамилия ребёнка')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(18)], verbose_name='Возраст')),
                ('about', models.TextField(max_length=200, verbose_name='Увлечения ребенка')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')], verbose_name='Номер телефона')),
                ('way', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_1.Ways', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'регистрация',
                'verbose_name_plural': 'регистрации',
            },
        ),
        migrations.CreateModel(
            name='AdvUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_activated', models.BooleanField(db_index=True, default=True, verbose_name='Прошел активацию?')),
                ('telegram_acc', models.CharField(max_length=50, verbose_name='Telegram')),
                ('is_teacher', models.BooleanField(db_index=True, default=False, verbose_name='Преподаватель')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]