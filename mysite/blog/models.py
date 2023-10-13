from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class PublishManager(models.Manager):
    """Создание своего менеджера"""
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """
    Таблица с данными поста
    """

    class Status(models.TextChoices):
        """Используемые статусы поста"""
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()  # Использование менежера по умолчанию
    publish = PublishManager()  # Использование своего менеджера

    class Meta:
        ordering = ['-publish']  # Сортировка записей в обратном порядке
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
