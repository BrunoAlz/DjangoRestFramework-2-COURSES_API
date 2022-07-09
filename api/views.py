from rest_framework.generics import get_object_or_404
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
    # Faz a Consulta para pegar os dados do banco.
    queryset = Avaliacao.objects.all()
    # Chama o serealizador e passa os dados
    serializer_class = AvaliacaoSerializer

    # sobrescreve o metodo get queryset
    def get_queryset(self):
        # Se a pk do curso vier nos kwargs da request
        if self.kwargs.get('curso_pk'):
            # pega a pk nos kwargs e filtra a consulta das avaliacoes baseada nessa pk do curso
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        # se não retorna a consulta completa 
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Faz a Consulta para pegar os dados do banco.
    queryset = Avaliacao.objects.all()
    # Chama o serealizador e passa os dados
    serializer_class = AvaliacaoSerializer

    # Sobrescreve o método get_object => retorna apenas 1 linha da consulta
    def get_object(self):
        # pega a PK do curso na requisição
        if self.kwargs.get('curso_pk'):
            # retorna a consulta filtrando 
            return get_object_or_404(
                self.get_queryset(), 
                # Filtra o curso pela PK na requisição
                curso_id=self.kwargs.get('curso_pk'),
                # Filtra a Avaliação relacionada pelo PK na requisição
                pk=self.kwargs.get('avaliacao_pk')
                )

        # Se não achar, traz só a avaliação 
        return get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs.get('avaliacao_pk')
        )


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