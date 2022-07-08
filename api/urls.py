from django.urls import path

from .views import CursoAPIView, AvaliacaoAPIView, UsersAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
    path('usuarios/', UsersAPIView.as_view(), name='users'),
]
