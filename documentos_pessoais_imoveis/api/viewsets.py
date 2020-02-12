from rest_framework.viewsets import ModelViewSet

from documentos_pessoais_imoveis.api.serializers import DocumentosPessoaisImoveisSerializer
from documentos_pessoais_imoveis.models import DocumentosPessoaisImoveis



class DocumentosPessoaisImoveisViewSet(ModelViewSet):
    queryset = DocumentosPessoaisImoveis.objects.all()
    serializer_class = DocumentosPessoaisImoveisSerializer