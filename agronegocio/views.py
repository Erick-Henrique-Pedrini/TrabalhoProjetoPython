
from rest_framework import viewsets
from .models import (
    Propriedade, Cultura, Funcionario, Fornecedor,
    Insumo, Plantio, HistoricoPlantio, Colheita
)
from .serializers import (
    PropriedadeSerializer, CulturaSerializer, FuncionarioSerializer,
    FornecedorSerializer, InsumoSerializer, PlantioSerializer,
    HistoricoPlantioSerializer, ColheitaSerializer
)

# Create your views here.

class PropriedadeViewSet(viewsets.ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer

class CulturaViewSet(viewsets.ModelViewSet):
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer

class PlantioViewSet(viewsets.ModelViewSet):
    queryset = Plantio.objects.all()
    serializer_class = PlantioSerializer

class HistoricoPlantioViewSet(viewsets.ModelViewSet):
    queryset = HistoricoPlantio.objects.all()
    serializer_class = HistoricoPlantioSerializer

class ColheitaViewSet(viewsets.ModelViewSet):
    queryset = Colheita.objects.all()
    serializer_class = ColheitaSerializer