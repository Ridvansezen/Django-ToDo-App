from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
