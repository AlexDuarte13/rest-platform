"""ebix_auto_vistoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from automovel.api.viewsets import AutomovelViewSet
from documentosPessoais.api.viewsets import DocumentosPessoaisViewSet
from documentos_pessoais_imoveis.api.serializers import DocumentosPessoaisImoveisSerializer
from documentos_pessoais_imoveis.api.viewsets import DocumentosPessoaisImoveisViewSet
from equipamentos.api.viewsets import EquipamentoViewSet
from imovel.api.serializers import ImovelSerializer
from imovel.api.viewsets import ImovelViewSet
from vistoria.api.viewsets import VistoriaViewSet
from endereco.api.viewsets import EnderecoViewSet
from vistoria_imoveis.api.viewsets import VistoriaImoveisViewSet

router = routers.DefaultRouter();
router.register('vistoria', VistoriaViewSet, base_name='Vistoria')
router.register('endereco', EnderecoViewSet)
router.register('automovel', AutomovelViewSet)
router.register('documentosPessoais', DocumentosPessoaisViewSet)
router.register('equipamento', EquipamentoViewSet)
router.register('documentosPessoaisImoveis', DocumentosPessoaisImoveisViewSet)
router.register('imovel', ImovelViewSet)
router.register('vistoria_imoveis', VistoriaImoveisViewSet, base_name='VistoriaImoveis')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
