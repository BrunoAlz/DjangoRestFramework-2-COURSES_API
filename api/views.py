from rest_framework import generics
from .models import Curso, Avaliacao
from django.contrib.auth.models import User
from .serializers import CursoSerializer, AvaliacaoSerializer, UsersSerializer


class CursosAPIView(generics.ListCreateAPIView):
    """
    API de Cursos para usar no React / Flutter
    """
    
    # Faz a Consulta para pegar os dados do banco.
    queryset = Curso.objects.filter(ativo=1)
    # Chama o serealizador e passa os dados
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Faz a Consulta para pegar os dados do banco.
    queryset = Curso.objects.all()
    # Chama o serealizador e passa os dados
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    """
    API de Avaliações para usar no React / Flutter
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Faz a Consulta para pegar os dados do banco.
    queryset = Curso.objects.all()
    # Chama o serealizador e passa os dados
    serializer_class = CursoSerializer


class UsersAPIView(generics.ListCreateAPIView):
    """
    API de Usuários para usar no React / Flutter
    """
    queryset = User.objects.filter(is_active=1)
    serializer_class = UsersSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API de Usuários para usar no React / Flutter
    """
    queryset = User.objects.filter(is_active=1)
    serializer_class = UsersSerializer