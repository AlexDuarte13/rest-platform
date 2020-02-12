from rest_framework.serializers import ModelSerializer
from documentosPessoais.models import DocumentosPessoais
from endereco.api.serializers import EnderecoSerializer
from endereco.models import Endereco


class DocumentosPessoaisSerializer(ModelSerializer):

    endereco = EnderecoSerializer()

    class Meta:
        model = DocumentosPessoais
        fields = ('id', 'nome', 'cpf', 'email', 'dataNascimento', 'telefone', 'endereco', 'fotoRecibo')

    def create(self, validated_data):

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = DocumentosPessoais.objects.create(**validated_data)

        end = Endereco.objects.create(**endereco)

        ponto.endereco = end

        ponto.save()

        return ponto