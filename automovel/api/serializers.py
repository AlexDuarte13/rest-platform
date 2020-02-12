from rest_framework.serializers import ModelSerializer

from automovel.models import Automovel
from equipamentos.api.serializers import EquipamentoSerializer


class AutomovelSerializer(ModelSerializer):

    # equipamentos = EquipamentoSerializer(many=True, allow_null=True)

    class Meta:
        model = Automovel
        fields = ['id', 'placa', 'ufPlaca', 'chassi', 'renavam', 'marcaModelo',
                  'anoDoVeiculo', 'km', 'cor', 'combustivel', 'tipoVeiculo',
                  'capacidadePassageiros', 'fabricante', 'fotoCNH', 'fotoCRLV', 'fotoDianteiraDireita',
                  'fotoDianteiraEsquerda', 'fotoTraseiraDireita', 'fotoTraseiraEsquerda']
        extra_kwargs = {
            'equipamentos': {'required': False},
        }