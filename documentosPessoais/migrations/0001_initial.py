# Generated by Django 2.2.5 on 2019-10-08 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentosPessoais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=150)),
                ('dataNascimento', models.TextField()),
                ('fotoRecibo', models.ImageField(blank=True, null=True, upload_to='fotoRecibo')),
                ('enderecos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='endereco.Endereco')),
            ],
        ),
    ]
