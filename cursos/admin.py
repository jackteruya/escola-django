from django.contrib import admin
# from axes.models import AccessAttempt, AccessLog

from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')

# @admin.register(AccessAttempt)
# class AcessAttemptAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#
# @admin.register(AccessLog)
# class AcessAttemptAdmin(admin.ModelAdmin):
#     list_display = '__all__'
