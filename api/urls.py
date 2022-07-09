from django.urls import path

from .views import (
    AvaliacoesAPIView, AvaliacoesViewSet, CursoAPIView, 
    AvaliacaoAPIView, CursoViewSet, CursosAPIView, 
    UserAPIView, UsersAPIView
    )

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'avaliacoes', AvaliacoesViewSet, basename='avaliacoes')
router.register(r'cursos', CursoViewSet, basename='cursos')

urlpatterns = [
    # Rotas de Listagem
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('usuarios/', UsersAPIView.as_view(), name='users'),

    # Rotas de Detalhes
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('usuarios/<int:pk>', UserAPIView.as_view(), name='user'),

    # Rotas de Relacionamentos
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    
]
