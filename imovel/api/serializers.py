from rest_framework.serializers import ModelSerializer
from imovel.models import Imovel


class ImovelSerializer(ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'
