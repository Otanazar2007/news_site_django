from datetime import timezone

from django.db import models

from news_site.settings import TIME_ZONE


# Create your models here.
class News(models.Model):
    new_news = models.CharField(max_length=200)
    photo_news = models.FileField()
    news_desc = models.TextField(max_length=10000)
    urls = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_news

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Добавить новость"