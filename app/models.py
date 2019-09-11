from django.db import models

# Create your models here.


class Texts(models.Model):
    title = models.TextField(unique=True)
    text_value = models.TextField()
    tags = models.TextField()
