from rest_framework import viewsets
from .models import Totem, Coleta, Rota
from .serializers import TotemSerializer, ColetaSerializer, RotaSerializer, UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response

from core import serializers

class TotemViewSet(viewsets.ModelViewSet):
    queryset = Totem.objects.filter(status='ativo')
    serializer_class = TotemSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        """Implementação de soft delete para marcar o totem como excluído."""
        instance = self.get_object()
        instance.status = 'excluido'
        instance.save()
        return Response({"message": "Totem excluído com sucesso!"})

    @action(detail=False, methods=['get'])
    def excluidos(self, request):
        """Retorna a lista de totens excluídos."""
        excluidos = Totem.objects.filter(status='excluido')
        serializer = self.get_serializer(excluidos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def restaurar(self, request, pk=None):
        """Restaura um totem excluído para o status ativo."""
        # Aqui usamos `get_queryset` para garantir que buscamos todos os registros, inclusive os excluídos
        try:
            totem = Totem.objects.get(pk=pk, status='excluido')
            totem.status = 'ativo'
            totem.save()
            return Response({'status': 'Totem restaurado com sucesso!'})
        except Totem.DoesNotExist:
            return Response({'detail': 'Totem não encontrado ou já está ativo.'}, status=404)

class ColetaViewSet(viewsets.ModelViewSet):
    queryset = Coleta.objects.all()
    serializer_class = ColetaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Pega os dados do request e cria um novo usuário
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        nome_completo = request.data.get('nome_completo')

        # Criar um novo usuário
        user = User.objects.create_user(username=username, email=email, password=password, first_name=nome_completo)
        return Response({'message': f'Usuário {user.username} cadastrado com sucesso!'})
    
class RotaViewSet(viewsets.ModelViewSet):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer
    permission_classes = [IsAuthenticated]
