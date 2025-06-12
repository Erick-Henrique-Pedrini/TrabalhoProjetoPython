from django.db import models

# Create your models here.

class Propriedade(models.Model):
    nome = models.CharField(max_length=255)
    cep = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Cultura(models.Model):
    nome = models.CharField(max_length=32)
    tipo = models.CharField(max_length=32)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    cpf = models.CharField(max_length=32)
    telefone = models.CharField(max_length=32)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=32, unique=True)
    telefone = models.CharField(max_length=32, unique=True)
    endereco = models.CharField(max_length=45)    
    
    class Meta:
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.nome

class Insumo(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=32)
    unidade = models.CharField(max_length=32)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Plantio(models.Model):
    area = models.FloatField()
    tipo = models.CharField(max_length=32)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.PROTECT)
    cultura = models.ForeignKey(Cultura, on_delete=models.PROTECT)

    def __str__(self):
        return f"Plantio {self.id} - {self.tipo}"

class HistoricoPlantio(models.Model):
    plantio = models.ForeignKey(Plantio, on_delete=models.PROTECT)
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT)
    data_aplicacao = models.DateField()

    def __str__(self):
        return f"Histórico {self.id} do plantio {self.plantio.id}"

class Colheita(models.Model):
    quantidade_kg = models.FloatField()
    data_colheita = models.DateField()
    plantio = models.ForeignKey(Plantio, on_delete=models.PROTECT)

    def __str__(self):
        return f"Colheita {self.id} - {self.quantidade_kg} kg"(32)
    

    
