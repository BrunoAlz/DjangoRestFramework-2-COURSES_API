from asyncore import read
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        # O Email não será apresentado, apenas será exigido no cadastro
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Adicionando Relacionamento via NESTED RELATIONSHIP
    # MELHOR APLICADO NOS RELACIONAMENTOS ONE TO ONE
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Adicionando Relacionamento via HyperLinked Related Field
    # MELHOR APLICADO QUANDO TEMOS MUITOS DADOS RELACIONADOS
    # Ao invés de mostrar os dados, mostrará o Link para os dados relacionados
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='avaliacoes-detail'
    #     )

    # Adiconando Relacionamento via PK
    # MELHOR PERFORMANCE POSSIVEL, Retorna apenas o ID, dos dados relacionados
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
        )
