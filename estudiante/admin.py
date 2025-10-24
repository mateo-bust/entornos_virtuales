from django.contrib import admin
from .models import Curso, Estudiante

# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_horas')
    search_fields = ('nombre',)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'nota_curso', 'curso')
    search_fields = ('nombre', 'apellido')