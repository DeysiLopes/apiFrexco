from rest_framework import serializers
from fruit import models

class FruitSerializer(serializers.ModelSerializers):
    class Meta:
        model = models.Fruit 
        fields = '__all__'