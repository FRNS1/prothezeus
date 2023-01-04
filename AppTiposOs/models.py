from django.db import models

# Create your models here.


class tipoos(models.Model):
    nome_tipo_os = models.CharField(db_column='nome_tipo_os', max_length=100)

    class Meta:
        managed = False
        db_table = 'tipos_os'
