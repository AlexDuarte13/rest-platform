from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from google.cloud import vision
import os
import json
from enum import Enum
import re


from documentosPessoais.models import DocumentosPessoais, RetornoRecibo
from endereco.models import Endereco
from .serializers import DocumentosPessoaisSerializer

class DocumentosPessoaisViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DocumentosPessoais.objects.all()
    serializer_class = DocumentosPessoaisSerializer
    filter_fields = ('nome', 'cpf')


    @action(methods=['post'], detail=False)
    def verificar_recibo(self, request):
        foto = request.data['foto']

        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/tiago/projetos-python/chave-google/ebix-vistoria-auto-356728d11e31.json"
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\projetos-python\chave-google\ebix-vistoria-auto-356728d11e31.json"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/ebix-vistoria-auto-356728d11e31.json"

        print('Credendtials from environ: {}'.format(
            os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

        client = vision.ImageAnnotatorClient()

        response = client.text_detection(image=foto.file)
        # document = response.text_annotations

        boolean_texto_nome_endereco = False
        boolean_proximo_bloco = False
        boolean_proximo_word = False
        boolean_texto_rua = False
        boolean_texto_cep = False
        boolean_texto_complemento = False

        nome = []
        logradouro = []
        complemento = []
        cep = ''
        numero = ''
        cpfCnpj = ''

        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                # print('\nBlock confidence: {}\n'.format(block.confidence))
                if(boolean_texto_nome_endereco or boolean_texto_rua or boolean_texto_cep):
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

                        if(cpfCnpj == ''):
                            regexcpf = re.match(r"(^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2})|(^[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2})", word_text)
                            if regexcpf is not None:
                                cpfCnpj = re.search(r"(^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2})|(^[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2})", word_text).group(0)

                        if(boolean_texto_cep):
                            boolean_proximo_word=True

                        if(word_text == "NOME/ENDEREÇO-" or word_text == "NOME/ENDEREÇO"):
                            boolean_texto_nome_endereco = True

                        if(boolean_proximo_bloco and boolean_texto_nome_endereco):
                            nome.append(word_text)
                            nome.append(' ')

                        if (boolean_proximo_bloco and boolean_texto_rua):
                            regexNum = re.match(r"^N.\s*[0-9]+", word_text)
                            if regexNum is not None:
                                numero += re.search(r"[0-9]+", word_text).group(0)
                                boolean_texto_complemento = True
                            elif(boolean_texto_complemento):
                                complemento.append(word_text)
                                complemento.append(' ')
                            else:
                                logradouro.append(word_text)
                                logradouro.append(' ')

                        textoVerificarAno = ''.join(texto_word).strip()
                        if(cep == ''):
                            regexCEP = re.match(r"^[cC]{1}[eE]{1}[pP]{1}\s{1,}[0-9]{8}", textoVerificarAno)
                            if regexCEP is not None:
                                cep = re.search(r"[0-9]{8}$", textoVerificarAno).group(0)

                        # if(word_text == "CEP"):
                        #     boolean_texto_cep = True
                        # elif(boolean_proximo_word and boolean_texto_cep):
                        #     boolean_texto_cep = False
                        #     boolean_proximo_bloco = False
                        #     cep += word_text

                        print('Word text: {} (confidence: {})'.format(
                            word_text, word.confidence))

                        boolean_proximo_word = False

                        for symbol in word.symbols:
                            print('\tSymbol: {} (confidence: {})'.format(
                                symbol.text, symbol.confidence))

                if(boolean_proximo_bloco and boolean_texto_nome_endereco):
                    boolean_texto_rua = True
                    boolean_texto_nome_endereco = False
                elif (boolean_proximo_bloco and boolean_texto_rua):
                    boolean_texto_rua = False
                    boolean_texto_complemento = False

                boolean_proximo_bloco = False

        resposta = RetornoRecibo(''.join(nome).strip(), ''.join(logradouro).strip(), numero, cep, cpfCnpj, ''.join(complemento).strip()).__dict__

        return HttpResponse(json.dumps(resposta), content_type="application/json")

