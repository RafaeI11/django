# Generated by Django 4.2.7 on 2023-12-10 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0004_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='detallepedido',
            options={'verbose_name': 'Detalle de Pedido', 'verbose_name_plural': 'Detalles de Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
