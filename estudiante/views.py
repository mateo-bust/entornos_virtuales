from django.shortcuts import render

from estudiante.models import Estudiante, Curso


def index(request):
    return render(request, 'estudiante/index.html')


def alta_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        curso_id = request.POST.get('curso')

    if nombre and apellido and edad and curso_id:
        curso = Curso.objects.get(id=curso_id)
        Estudiante.objects.create(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            curso=curso
        )
        return render(request, 'estudiantes/agregar_estudiante.html', {'success': True})

    cursos = Curso.objects.all()
    return render(request, 'estudiantes/agregar_estudiante.html', {'cursos': cursos})



def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiantes/lista_cursos.html', {'cursos': cursos})
