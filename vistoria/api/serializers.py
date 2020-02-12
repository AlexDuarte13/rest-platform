from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from automovel.api.serializers import AutomovelSerializer
from automovel.models import Automovel
from documentosPessoais.api.serializers import DocumentosPessoaisSerializer
from documentosPessoais.models import DocumentosPessoais
from endereco.models import Endereco
from equipamentos.models import Equipamento
from vistoria.models import Vistoria


class VistoriaSerializer(ModelSerializer):

    documentosPessoais = DocumentosPessoaisSerializer()
    automovel = AutomovelSerializer()

    class Meta:
        model = Vistoria
        fields = ('id', 'nome', 'data', 'documentosPessoais', 'automovel')

    def create(self, validated_data):

        documentosPessoais = validated_data['documentosPessoais']
        del validated_data['documentosPessoais']

        endereco = documentosPessoais['endereco']
        del documentosPessoais['endereco']


        automovel = validated_data['automovel']
        del validated_data['automovel']

        #equipamentos = automovel['equipamentos']
       # del automovel['equipamentos']
        # del validated_data['automovel']



        # for equipamento in equipamentos:
        #     at = Automovel.objects.create(**equipamento)
        #     ponto.atracoes.add(at)

        auto = Automovel.objects.create(**automovel)
        #self.cria_equipamentos(equipamentos, auto)
        auto.save()
        #equips = Equipamento.objects.create(**equipamentos)


        docPessoais = DocumentosPessoais.objects.create(**documentosPessoais)
        end = Endereco.objects.create(**endereco)
        end.save()
        docPessoais.endereco=end
        docPessoais.save()

        ponto = Vistoria.objects.create(**validated_data)

        # docPessoais.endereco = end
        #auto.equipamentos=equips

        ponto.documentosPessoais = docPessoais
        ponto.automovel = auto

        ponto.save()

        return ponto


    def cria_equipamentos(self, equipamentos, auto):
        for equipamento in equipamentos:
            equip = Equipamento.objects.create(**equipamento)
            auto.equipamentos.add(equip)