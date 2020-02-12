from rest_framework.viewsets import ModelViewSet

from equipamentos.api.serializers import EquipamentoSerializer
from equipamentos.models import Equipamento

class EquipamentoViewSet(ModelViewSet):

    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    filter_fields = ('nome','descricao')