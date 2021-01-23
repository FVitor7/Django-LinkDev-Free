from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Link(models.Model):
    title = models.CharField(verbose_name='Título', max_length=100)
    url = models.URLField(verbose_name='URL', max_length=2083)
    background_color = models.CharField(max_length=100)
    description = models.TextField(
        verbose_name='Descrição', blank=True, null=True)
    clicks_count = models.PositiveIntegerField(default=0)
    date_create = models.DateTimeField(
        verbose_name='Data de Criação', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "link"

    def __str__(self):
        return self.title

    def get_create_date(self):
        return self.date_create.strftime('%d/%m/%Y %H:%M')
