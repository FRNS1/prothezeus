# Generated by Django 4.0 on 2022-12-31 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppClientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(db_column='nome_completo', max_length=100)),
                ('telefone', models.CharField(db_column='telefone', max_length=16)),
                ('email', models.CharField(db_column='email', max_length=100)),
                ('endereco', models.CharField(db_column='endereco', max_length=100)),
                ('preco', models.DecimalField(db_column='preco', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'clientes',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='clientes',
        ),
    ]