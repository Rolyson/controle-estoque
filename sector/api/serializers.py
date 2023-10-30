from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from sector.models import Sector

class SectorSerializer(ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'