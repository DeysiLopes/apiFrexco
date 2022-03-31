from django.db import models
from uuid import uuid4

# Create your models here.

class Fruit(models.Model):
    id_fruit = models.UUIDField(primary_key =True, default = uuid4, editable=False)
    name_fruit = models.CharField(max_length=255)
    # name_region = models.ForeignKey('Region', on_delete=models.CASCADE)