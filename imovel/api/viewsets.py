from rest_framework.viewsets import ModelViewSet

from imovel.api.serializers import ImovelSerializer
from imovel.models import Imovel


class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer