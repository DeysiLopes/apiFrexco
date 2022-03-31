from rest_framework import viewsets
from region.api import serializers 
from region import models

class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegionSerializer
    queryset = models.Region.objects.all()