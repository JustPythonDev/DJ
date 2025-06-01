from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class News_post(models.Model):
    title = models.CharField("Название новости", max_length=100)
    short_description = models.CharField("Краткое описание новости", max_length=200)
    content = models.TextField("Новость")
    date_posted = models.DateTimeField("Даа публикации",default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"