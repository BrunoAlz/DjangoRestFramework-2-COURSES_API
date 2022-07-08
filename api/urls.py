from django.urls import path

from .views import (
    AvaliacoesAPIView, CursoAPIView, 
    AvaliacaoAPIView, CursosAPIView, 
    UserAPIView, UsersAPIView
    )

urlpatterns = [
    # Rotas de Listagem
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('usuarios/', UsersAPIView.as_view(), name='users'),

    # Rotas de Detalhes
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('usuarios/<int:pk>', UserAPIView.as_view(), name='user'),
    
]
