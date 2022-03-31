from rest_framework import viewsets
from fruit.api import serializers 
from fruit import models

class FruitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FruitSerializer
    queryset = models.Fruit.objects.all()