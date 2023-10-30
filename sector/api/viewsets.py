from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from sector.api.serializers import SectorSerializer
from sector.models import Sector

class SectorViewSet(ModelViewSet):
    serializer_class       = SectorSerializer
    search_fields          = ["id"]
    filter_backends        = (SearchFilter, OrderingFilter)
    ordering               = ('id')

    def get_queryset(self):
        return Sector.objects.all()