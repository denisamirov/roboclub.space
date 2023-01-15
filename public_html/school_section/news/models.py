from django.db import models


class Type(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Тип', max_length=256, blank=True)

    class Meta:
        verbose_name = 'тип'
        verbose_name_plural = 'типы'


class News(models.Model):
    title = models.CharField('Наименование', max_length=40)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='Тип_объявления')
    news = models.TextField('Объявление', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-created_at']



