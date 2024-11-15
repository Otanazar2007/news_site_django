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

class Commentary(models.Model):
    news_name = models.ForeignKey(News, on_delete=models.CASCADE, related_name='commentaries')
    user_name = models.CharField(max_length=20)
    comm = models.TextField(max_length=150)
    comm_photo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    urls = models.ForeignKey(News, on_delete=models.CASCADE, related_name='url_commentaries')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Добавить комментарий"
        verbose_name_plural = "Комментарии"
