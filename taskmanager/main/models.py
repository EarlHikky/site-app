from django.db import models

# Create your models here.
class Task(models.Model): # создаём табличку
    title = models.CharField('Название', max_length=50) # поле с текстом до 50 символов
    task = models.TextField('Описание') # много текста добавить можно

    def __str__(self): # метод вызывается, когда пытаемся вывести на экран объект этого класса
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
