from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from vistoria.models import Vistoria
from .serializers import VistoriaSerializer

class VistoriaViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = VistoriaSerializer
    filter_backends = (SearchFilter,)
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    search_fields = ('id', 'nome', 'data')

    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        data = self.request.query_params.get('data', None)

        queryset = Vistoria.objects.all()
        if id:
            queryset = queryset.filter(pk=id)

        if data:
            queryset = queryset.filter(nome__iexact=data)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(VistoriaViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(VistoriaViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(VistoriaViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(VistoriaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(VistoriaViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(VistoriaViewSet, self).partial_update(request, *args, **kwargs)
