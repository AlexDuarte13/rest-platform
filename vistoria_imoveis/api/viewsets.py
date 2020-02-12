from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from vistoria_imoveis.models import VistoriaImoveis
from .serializers import VistoriaImoveisSerializer

class VistoriaImoveisViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = VistoriaImoveisSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('id', 'nome', 'dataRegistro')

    lookup_field = 'id'

    def get_queryset(self):
        queryset = VistoriaImoveis.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        return super(VistoriaImoveisViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(VistoriaImoveisViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(VistoriaImoveisViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(VistoriaImoveisViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(VistoriaImoveisViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(VistoriaImoveisViewSet, self).partial_update(request, *args, **kwargs)
