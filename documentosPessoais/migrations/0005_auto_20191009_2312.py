# Generated by Django 2.2.5 on 2019-10-09 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentosPessoais', '0004_auto_20191009_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentospessoais',
            old_name='enderecos',
            new_name='endereco',
        ),
    ]
