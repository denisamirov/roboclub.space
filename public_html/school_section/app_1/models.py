from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_activated = models.BooleanField(default=False, db_index=True, verbose_name="Прошел активацию?")
    telegram_acc = models.CharField(max_length=50, verbose_name="Telegram")
    is_teacher = models.BooleanField(default=False, db_index=True, verbose_name="Преподаватель")
    email = models.EmailField('email adress')


class diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', blank=False)
    author = models.CharField(max_length=50, verbose_name="автор")
    title = models.CharField(max_length=100, verbose_name="название")
    start_page = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="начальная стараница")
    end_page = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="последняя страница")
    date = models.DateField('Дата')



class Ways(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Направления', max_length=256, blank=True)


    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'
        

class Registration(models.Model):

    first_name = models.CharField('Имя ребёнка', max_length=70)
    last_name = models.CharField('Фамилия ребёнка', max_length=70, blank=True)
    age = models.IntegerField('Возраст', validators=[MinValueValidator(7), MaxValueValidator(18)])
    about = models.TextField('Увлечения ребенка', max_length=200)
    way = models.ForeignKey(Ways, on_delete=models.PROTECT, verbose_name='Направление')
    email = models.EmailField('Электронная почта')
    phoneNumberRegex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    phone_number = models.CharField('Номер телефона', validators=[phoneNumberRegex], max_length=16, unique=True)
    date_registration = models.DateField('registration date', auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'регистрация'
        verbose_name_plural = 'регистрации'


# Модели для оценки скорости чтения

class Group_text(models.Model):
    def __str__(self):
        return self.id_group

    id_group = models.CharField(max_length=70)

    class Meta:
        verbose_name = 'группа текстов'
        verbose_name_plural = 'группы текстов'

   

class SpeedText(models.Model):
    def __str__(self):
        return self.name_text
    
    id_text = models.AutoField(verbose_name='ID_text', primary_key=True)
    name_text = models.CharField('Название_текста', max_length=70)
    text = models.TextField('Текст')
    id_group = models.ForeignKey(Group_text, on_delete=models.PROTECT, verbose_name='Группа текстов')

    class Meta:
        verbose_name = 'название текста'
        verbose_name_plural = 'название текстов'


class Questions(models.Model):
    name_text = models.OneToOneField(SpeedText, models.DO_NOTHING, db_column='name_text', primary_key=True)
    q_1 = models.CharField(max_length=100, blank=True, null=True)
    a_11 = models.CharField(max_length=45, blank=True, null=True)
    a_12 = models.CharField(max_length=45, blank=True, null=True)
    a_13 = models.CharField(max_length=45, blank=True, null=True)
    a_14 = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


# Конец описания моделей для оценки скорости чтения