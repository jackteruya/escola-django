import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    class Status(models.TextChoices):
        ATIVO = 'ativo', 'Ativo'
        INATIVO = 'inativo', 'Inativo'

    class Perfil(models.TextChoices):
        PROFESSOR = 'professor', 'Professor'
        ALUNO = 'aluno', 'Aluno'

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nome = models.CharField(max_length=150)
    celular = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    perfil = models.CharField(max_length=10, choices=Perfil.choices, default=Perfil.ALUNO)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ATIVO)

    def __str__(self):
        return self.nome
