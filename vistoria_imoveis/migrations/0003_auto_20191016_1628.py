# Generated by Django 2.2.5 on 2019-10-16 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos_pessoais_imoveis', '0001_initial'),
        ('imovel', '0001_initial'),
        ('endereco', '0001_initial'),
        ('vistoria_imoveis', '0002_auto_20191016_1513'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vistoria_Imoveis',
            new_name='VistoriaImoveis',
        ),
        migrations.RenameField(
            model_name='vistoriaimoveis',
            old_name='documentosPessoais',
            new_name='documentosPessoaisImoveis',
        ),
    ]