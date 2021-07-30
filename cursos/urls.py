from django.urls import path

from .views import CursoAPIView, AvaliacaoAPIVew

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacaoAPIVew.as_view(), name='avaliacoes'),
]
