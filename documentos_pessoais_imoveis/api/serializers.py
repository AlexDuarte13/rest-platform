from rest_framework.serializers import ModelSerializer
from documentos_pessoais_imoveis.models import DocumentosPessoaisImoveis


class DocumentosPessoaisImoveisSerializer(ModelSerializer):
    class Meta:
        model = DocumentosPessoaisImoveis
        fields = '__all__'
