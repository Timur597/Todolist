from django.db import models


class Todo(models.Model):
    text = models.CharField('Текст', max_length=150)
    complete = models.BooleanField('Состояние публикации', default=False)

    def __str__(self):
        return self.text
