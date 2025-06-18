from .models import (
    Propriedade, Cultura, Funcionario, Fornecedor,
    Insumo, Plantio, HistoricoPlantio, Colheita
)

class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'

class CulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultura
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'

class PlantioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantio
        fields = '__all__'

class HistoricoPlantioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoPlantio
        fields = '__all__'

class ColheitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colheita
        fields = '__all__'