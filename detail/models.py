from turtle import title
from django.db import models

# Create your models here.


class Detail(models.Model):
    title = models.CharField()
    description = models.CharField()
    def __str__(self):
        return self.title
