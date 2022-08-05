# Generated by Django 4.1 on 2022-08-05 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
                ('estoque', models.PositiveIntegerField(verbose_name='Estoque')),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.restaurante', verbose_name='Restaurante')),
            ],
        ),
    ]