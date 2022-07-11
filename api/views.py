from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import mixins

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer, UsersSerializer


# API V1 com GENERIC VIEWS
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


# API V2 COM VIEW SETS
"""
    ModelViewSet, permite a realização completa do CRUD de Um modelo, 
    e ainda faz as rotas automaticamente.
    Basta passar o a Consulta do modelo e o Serealizador dos dados para um Crud Simples.
"""
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # Usaremos o decorador ACTION para criar uma nova Rota para acessar as Avaliações dos Cursos
    # Implementa o método para pegar dados na Requisição
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # Pega o Objeto curso que está vindo na requisição
        curso = self.get_object()
        # Faz uma consulta usando o Objeto Cursom para pegar todas as Avaliações relacionadas, com Many
        # a consulta "curso . 'avaliacoes'. all() está usando o RELATED NAME avaliacoes la do model"
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        # Serializa os dados e devolve na response
        return Response(serializer.data)


# class AvaliacoesViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer



class AvaliacoesViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    """
        Herdando Diretamente os MIXIN podemos personalizar os Métodos HTTP Permitidos
        de forma Simples.
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
