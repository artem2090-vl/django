from django.db import models

class Article(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата публікації')
    def __str__(self):
        return self.title

