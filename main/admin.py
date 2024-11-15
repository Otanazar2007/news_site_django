from django.contrib import admin
from .models import News, Commentary, Statistics, Created_news

# Register your models here.
admin.site.register(News)
admin.site.register(Commentary)
admin.site.register(Statistics)
admin.site.register(Created_news)