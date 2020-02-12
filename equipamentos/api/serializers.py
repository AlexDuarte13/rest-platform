from rest_framework.serializers import ModelSerializer
from equipamentos.models import Equipamento

class EquipamentoSerializer(ModelSerializer):
    class Meta:
        model = Equipamento
        fields = ['id', 'nome']
