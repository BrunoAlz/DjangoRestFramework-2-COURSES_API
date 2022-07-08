from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer, UsersSerializer


class CursoAPIView(APIView):
    # DESCRIÇÃO DA PÁGINA.
    """
    API de Cursos para usar no React / Flutter
    """

    # implementa o metodo GET, que recebe a requisição
    def get(self, request):
        # Faz a Consulta para pegar os dados do banco e salva na variavel
        cursos = Curso.objects.filter(ativo=1)
        # Passa os dados da consulta para o Serializador, o many avisa que estamos passando todos os dados
        serilizer = CursoSerializer(cursos, many=True)
        # Retorna o response para a request, com os dados Serializados  
        return Response(serilizer.data)


    # implementa o metodo POST, que recebe os dados na requisição
    def post(self, request):
        # O dados vem da requisição em 'request.data'
        # a variavel 'data' que manda para o Serializador e manda pro bd
        serializer = CursoSerializer(data=request.data)
        # valida os dados, se passar OK, se não lança exceção
        serializer.is_valid(raise_exception=True)
        # salva no bd
        serializer.save()
        # retorna os dados Criados e o status HTTP
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):

    def get(self, request):
        avaliacoes = Avaliacao.objects.filter(ativo=1)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersAPIView(APIView):
    """
    API de Usuários para usar no React / Flutter
    """
    def get(self, request):
        users = User.objects.filter(is_active=1)
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)