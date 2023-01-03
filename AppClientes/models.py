from django.db import models


# Create your models here.
class clientes(models.Model):
    nome_completo = models.CharField(db_column='nome_completo', max_length=100)
    telefone = models.CharField(db_column='telefone', max_length=16)
    email = models.CharField(db_column='email', max_length=100)
    endereco = models.CharField(db_column='endereco', max_length=100)
    preco = models.DecimalField(
        db_column='preco', decimal_places=2, max_digits=10)

    class Meta:
        managed = False
        db_table = 'clientes'
