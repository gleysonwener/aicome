# Generated by Django 4.1 on 2022-08-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_pedido_cod_pedido_end_entrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Aberto', 'Aberto'), ('Recebido', 'Recebido'), ('Em preparo', 'Em preparo'), ('Saiu para entrega', 'Saiu para entrega')], max_length=25, verbose_name='Status'),
        ),
    ]