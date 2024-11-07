from django.db import models

# Create your models here.
class UserMod(models.Model):
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=100)

