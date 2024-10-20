from rest_framework import serializers
from .models import Totem, Coleta, Rota
from django.contrib.auth.models import User

class TotemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Totem
        fields = '__all__'
        
class ColetaSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.SerializerMethodField()

    class Meta:
        model = Coleta
        fields = ['id', 'totem', 'peso', 'data_hora', 'usuario_nome']
        read_only_fields = ['usuario_nome', 'data_hora']

    def get_usuario_nome(self, obj):
        # Retorna o nome do usuário associado à coleta
        return obj.usuario.username  # Ou use obj.usuario.get_full_name() para o nome completo
    
class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = ['id', 'nome', 'dias_semana', 'periodo', 'data_criacao', 'ordem_totens']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  