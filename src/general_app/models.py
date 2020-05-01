from django.db import models


class Words(models.Model):
    english_word = models.CharField(max_length=50, unique=True)
    russian_word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
