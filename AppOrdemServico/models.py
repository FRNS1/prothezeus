from django.db import models
from AppTiposOs.models import *
from AppClientes.models import *

# Create your models here.
class ordem_servico(models.Model):
    tipo_os_id = models.ForeignKey(tipoos, on_delete = models.CASCADE, db_column='tipo_os_id', name='tipo_os')
    numero_pecas = models.IntegerField(db_column='numero_pecas')
    cliente_id = models.ForeignKey(clientes, on_delete=models.CASCADE, db_column='cliente_id', name='cliente_id')
    status = models.CharField(db_column='status', max_length=20)
    previsao_entrega = models.DateField(db_column='previsao_entrega')
    dt_entrada = models.DateField(db_column='dt_entrada')
    dt_concluida = models.DateField(db_column='dt_concluida')
    dt_entrega = models.DateField(db_column='dt_entrega')
    preco_total = models.DecimalField(db_column='preco_total', decimal_places=2, max_digits=10)

    class Meta:
        managed = False
        db_table = 'ordem_servico'