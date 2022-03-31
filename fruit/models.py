from django.db import models
from uuid import uuid4
# Create your models here.
class Fruit(models.Model):
    id_fruit = models.UUIDFIELD(primary_key = true, default = uuid4, ediTable = false)
    name_fruit = models.CharField(max_length=255)