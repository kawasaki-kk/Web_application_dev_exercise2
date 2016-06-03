# import datetime
from django.utils import timezone
from django.db import models
from Daily_report import settings

# Create your models here.
class Report(models.Model):
    """書籍"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reports')
    title = models.CharField('日報タイトル', max_length=255)
    publisher = models.CharField('投稿者', max_length=255, blank=True)
    date = models.DateTimeField('日付', default=timezone.now())
    content = models.TextField('日報', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """感想"""
    report = models.ForeignKey(Report, verbose_name='日報', related_name='comment')
    comment = models.TextField('コメント', blank=True)
    commenter = models.CharField('名前', max_length=255, blank=True)
    date = models.DateTimeField('日付', default=timezone.now())

    def __str__(self):
        return self.comment
