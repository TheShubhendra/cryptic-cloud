from django.db import models
class Cloud(models.Model):
  cloudname = models.CharField(max_length=200)
  data = models.CharField(max_length=10000)
