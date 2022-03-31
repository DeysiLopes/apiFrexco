from rest_framework import viewsets
from fruit.api import serializers 
from fruit import models

class FruitViewSet(serializers.ModelViewSet):
    serializer_class = serializers.FruitSerializer
    queryset = models.objects.all()