from asyncore import read
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Curso, Avaliacao

from django.db.models import Avg


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

    # Por padrão, as validações devem começar com "validade_" e o nome do campo que está sendo validado
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A Avaliação precisa estar entre 1 e 5')


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

    # Cria o campo no serializador que será alimentado por um Método
    media_avaliacoes = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    # Por padrão, os MethodFields devem começar com "get_" e o nome do campo que está sendo calculado
    def get_media_avaliacoes(self, obj):
        """
        1- obj é o model, o CURSO.
        2- avaliacoes é o related_name 'avaliacoes'
        3- aggregate é a função para agregar os dados 
        4- Avg('avaliacao') está pegando a coluna avaliação do model Avaliacoes e fazendo a média
        5- avaliacao__avg é o resultado da agragação
        """
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2


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
