from rest_framework.serializers import ModelSerializer

from documentos_pessoais_imoveis.api.serializers import DocumentosPessoaisImoveisSerializer
from documentos_pessoais_imoveis.models import DocumentosPessoaisImoveis
from endereco.api.serializers import EnderecoSerializer
from endereco.models import Endereco
from imovel.api.serializers import ImovelSerializer
from imovel.models import Imovel
from vistoria_imoveis.models import VistoriaImoveis


class VistoriaImoveisSerializer(ModelSerializer):

    documentosPessoaisImoveis = DocumentosPessoaisImoveisSerializer()
    imovel = ImovelSerializer()
    endereco = EnderecoSerializer()

    class Meta:
        model = VistoriaImoveis
        fields = ('id', 'nome', 'dataRegistro', 'documentosPessoaisImoveis', 'endereco', 'imovel')

    def create(self, validated_data):

        documentosPessoaisImoveis = validated_data['documentosPessoaisImoveis']
        del validated_data['documentosPessoaisImoveis']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        imovel = validated_data['imovel']
        del validated_data['imovel']

        imov = Imovel.objects.create(**imovel)
        imov.save()

        docPessoaisImoveis = DocumentosPessoaisImoveis.objects.create(**documentosPessoaisImoveis)
        docPessoaisImoveis.save()

        end = Endereco.objects.create(**endereco)
        end.save()

        vistoriaImovel = VistoriaImoveis.objects.create(**validated_data)

        vistoriaImovel.documentosPessoaisImoveis = docPessoaisImoveis
        vistoriaImovel.imovel = imov
        vistoriaImovel.endereco = end

        vistoriaImovel.save()

        return vistoriaImovel