from django.contrib import admin
from  .models import Propriedade, Funcionario, Plantio, Insumo, HistoricoPlantio, Colheita, Cultura, Fornecedor
# Register your models here.
admin.site.register(Propriedade)
admin.site.register(Funcionario)
admin.site.register(Plantio)
admin.site.register(Insumo)
admin.site.register(HistoricoPlantio)
admin.site.register(Colheita)
admin.site.register(Cultura)
admin.site.register(Fornecedor)
