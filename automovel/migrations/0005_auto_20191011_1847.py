# Generated by Django 2.2.5 on 2019-10-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automovel', '0004_auto_20191011_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovel',
            name='equipamentos',
            field=models.ManyToManyField(blank=True, to='equipamentos.Equipamento'),
        ),
    ]