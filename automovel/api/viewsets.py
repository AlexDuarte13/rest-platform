from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from google.cloud import vision
import os
import json
import re

from automovel.api.serializers import AutomovelSerializer
from automovel.models import Automovel, RetornoImagem, RetornoCRLV


class AutomovelViewSet(ModelViewSet):
    queryset = Automovel.objects.all()
    serializer_class = AutomovelSerializer
    filter_fields = ('placa', 'chassi')


    @action(methods=['post'], detail=False)
    def verificar_crlv(self, request):
        foto = request.data['foto']

        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/tiago/projetos-python/chave-google/ebix-vistoria-auto-356728d11e31.json"
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\projetos-python\chave-google\ebix-vistoria-auto-356728d11e31.json"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/ebix-vistoria-auto-356728d11e31.json"

        print('Credendtials from environ: {}'.format(
            os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

        client = vision.ImageAnnotatorClient()

        response = client.text_detection(image=foto.file)
        # document = response.text_annotations

        boolean_texto_marca_modelo = False
        boolean_texto_ano_mod = False
        boolean_texto_ano_fab = False
        boolean_texto_ano_veiculo = False
        boolean_proximo_bloco = False

        placa = ''
        uf = ''
        chassi = ''
        renavam = ''
        marcaModelo = []
        anoVeiculo = ''

        ordemMarcaModelo = False

        try:
            for page in response.full_text_annotation.pages:
                for block in page.blocks:

                    if((boolean_texto_ano_mod and boolean_texto_marca_modelo and boolean_texto_ano_fab) or boolean_texto_ano_veiculo):
                        boolean_proximo_bloco = True

                    for paragraph in block.paragraphs:
                        print('Paragraph confidence: {}'.format(
                            paragraph.confidence))

                        texto_word = []

                        for word in paragraph.words:

                            word_text = ''.join([
                                symbol.text for symbol in word.symbols
                            ])

                            texto_word.append(word_text)
                            texto_word.append(' ')

                            try:
                                # if (chassi == ''):
                                regexChassi = re.match(r"^[A0-Z9]{16,}", word_text)
                                if regexChassi is not None:
                                    chassi = re.search(r"^[A0-Z9]{16,}", word_text).group(0)
                            except:
                                print('Erro ao verificar Chassi')

                            try:
                                if (renavam == ''):
                                    regexRenavam = re.match(r"^[0-9]{11}", word_text)
                                    if regexRenavam is not None:
                                        renavam = re.search(r"^[0-9]{11}", word_text).group(0)
                            except:
                                print('Erro ao verificar renavam')

                            try:
                                if(placa == ''):
                                    regexPlaca = re.match(r"^[A-Z]{3}[0-9]{4}", word_text)
                                    if regexPlaca is not None:
                                        placa = re.search(r"^[A-Z]{3}[0-9]{4}", word_text).group(0)
                            except:
                                print('Erro ao verificar placa')

                            try:
                                if(uf == ''):
                                    regexPlacaUf = re.match(r"^[A-Z]{3}[0-9]{4}\/[A-Z]{2}", word_text)
                                    if regexPlacaUf is not None:
                                        uf = re.search(r"[A-Z]{2}$", word_text).group(0)
                            except:
                                print('Erro ao verificar UF')


                            #Se ano modelo então proximo bloco com marca modelo
                            textoVerificarAno = ''.join(texto_word).strip()
                            if (textoVerificarAno == "ANO MOD" or textoVerificarAno == "AN0 M0D" or textoVerificarAno == "MOD" or textoVerificarAno == "M0D"):
                                boolean_texto_ano_mod = True

                            if (textoVerificarAno == "MARCA/MODELO" or textoVerificarAno == "MARCA/M0DEL0"):
                                boolean_texto_marca_modelo = True

                            if (textoVerificarAno == "ANO FAB" or textoVerificarAno == "AN0 FA8" or textoVerificarAno == "FAB" or textoVerificarAno == "FA8"):
                                boolean_texto_ano_fab = True

                            try:
                                if(boolean_texto_ano_mod and boolean_texto_marca_modelo and boolean_texto_ano_fab and boolean_proximo_bloco):
                                    regexAnoVeiculo = re.match(r"^[0-9]{4}", word_text)
                                    if regexAnoVeiculo is not None:
                                        ordemMarcaModelo=True
                                        anoVeiculo = re.search(r"^[0-9]{4}", word_text).group(0)
                                        boolean_texto_ano_mod = True
                                        boolean_texto_ano_fab = True
                                        boolean_texto_marca_modelo = True
                                        boolean_texto_ano_veiculo = False
                                    else:
                                        marcaModelo.append(word_text)
                                        marcaModelo.append(' ')
                                        if(ordemMarcaModelo):
                                            boolean_texto_ano_veiculo = False
                                            ordemMarcaModelo=False
                            except:
                                print('Erro ao verificar preencher modelo/marca')

                            try:
                                if(boolean_texto_ano_veiculo and boolean_proximo_bloco):
                                    regexAnoVeiculo = re.match(r"^[0-9]{4}", word_text)
                                    if regexAnoVeiculo is not None:
                                        anoVeiculo = re.search(r"^[0-9]{4}", word_text).group(0)
                            except:
                                print('Erro ao verificar anoVeiculo')

                            print('Word text: {} (confidence: {})'.format(
                                word_text, word.confidence))

                            for symbol in word.symbols:
                                print('\tSymbol: {} (confidence: {})'.format(
                                    symbol.text, symbol.confidence))

                    if (boolean_texto_marca_modelo and boolean_texto_ano_mod and boolean_texto_ano_fab and boolean_proximo_bloco and ordemMarcaModelo != True):
                        boolean_texto_ano_mod = False
                        boolean_texto_ano_fab = False
                        boolean_texto_marca_modelo = False
                        boolean_texto_ano_veiculo = True
                    elif(boolean_texto_ano_veiculo and boolean_proximo_bloco):
                        boolean_texto_ano_veiculo = False

                    boolean_proximo_bloco = False

        except:
            print('realizar a leitura do documento CRLV')

        resposta = RetornoCRLV(placa.strip(), uf.strip(), chassi.strip(), renavam.strip(), ''.join(marcaModelo).strip(), anoVeiculo.strip()).__dict__

        return HttpResponse(json.dumps(resposta), content_type="application/json")


    @action(methods=['post'], detail=False)
    def verificar_foto(self, request):
        foto = request.data['foto']

        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/tiago/projetos-python/chave-google/ebix-vistoria-auto-356728d11e31.json"
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\projetos-python\chave-google\ebix-vistoria-auto-356728d11e31.json"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/ebix-vistoria-auto-356728d11e31.json"

        print('Credendtials from environ: {}'.format(
            os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

        client = vision.ImageAnnotatorClient()

        response = client.label_detection(image=foto.file)

        labels = response.label_annotations

        resposta = []
        for label in labels:
            label.score = round((label.score * 100))
            resposta.append(RetornoImagem(label.score, label.description).__dict__)

        resposta_json = json.dumps(resposta)

        return HttpResponse(resposta_json, content_type="application/json")

    @action(methods=['post'], detail=False)
    def verificar_propriedades_foto(self, request):
        foto = request.data['foto']

        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/tiago/projetos-python/chave-google/ebix-vistoria-auto-356728d11e31.json"
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\projetos-python\chave-google\ebix-vistoria-auto-356728d11e31.json"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/ebix-vistoria-auto-356728d11e31.json"

        print('Credendtials from environ: {}'.format(
            os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

        client = vision.ImageAnnotatorClient()

        response = client.image_properties(image=foto.file)

        # props = response.image_properties_annotation.dominant_colors
        #
        # resposta = []
        # for prop in props.colors:
        #     prop.score = round((prop.score * 100))
        #     resposta.append(prop.score)
        #     resposta.append(prop.color)

        # resposta_json = json.dumps(resposta)

        # return HttpResponse(resposta, content_type="application/json")


        retorno = response.image_properties_annotation.dominant_colors.colors[0]
        retorno.score = round((retorno.score * 100))
        return HttpResponse(retorno, content_type="application/json")

