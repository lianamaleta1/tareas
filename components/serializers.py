from rest_framework import serializers
from .models import *


class CatIndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model= CategoriaIndicadores
        fields= ('__all__')
        

class MetaSerializer(serializers.ModelSerializer):

    tipo = CatIndicadorSerializer()
    class Meta:
        model = Meta
        fields = ('id','orden','codigo','nombre','tipo','um','estado')
        read_only_fields=('codigo', 'orden','um','tipo', )


class IndicadoreSerializer(serializers.ModelSerializer):
    id_indicador = MetaSerializer()
    class Meta:
        models=IndicadorValor
        fields=('id','valor', 'plan','mes','anno','fecha_carga','id_indicador')
        read_only_fields=('fecha_carga', 'id_indicador', )

