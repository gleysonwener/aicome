# Generated by Django 4.1 on 2022-08-05 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0002_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Total')),
                ('status', models.CharField(choices=[('Aberto', 'Aberto'), ('Recebido', 'Recebido'), ('Em preparo', 'Em preparo'), ('Saiu para entrega', 'Saiu para entrega')], max_length=25, verbose_name='Descrição')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
