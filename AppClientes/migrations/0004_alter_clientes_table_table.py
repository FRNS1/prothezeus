# Generated by Django 4.0 on 2022-12-31 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppClientes', '0003_alter_clientes_table_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='clientes_table',
            table='clientes_prot',
        ),
    ]
