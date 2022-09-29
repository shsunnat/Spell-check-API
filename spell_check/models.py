from django.db import models


class SpellCheck(models.Model):
    text = models.TextField()

