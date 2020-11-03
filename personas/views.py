from django.shortcuts import render
from . models import Alumno

# Create your views here.
def index(request):
    print("hola estoy en la vista index")
    context={}
    return render(request,'personas/index.html', context)

def listar(request):
    print("hola esto es listar")
    alumnos = Alumno.objects.all()
    context = {'alumnos':alumnos}
    return render(request, 'personas/mostrar_datos.html', context)

def buscar(request):
    print("hola esto es buscar")
    context = {}
    return render(request, 'personas/boton_buscar.html', context)


def buscar_por_rut(request):
    print("hola esto es buscar_por_rut")
    mi_rut = request.POST['rut']
    alumnos = Alumno.objects.get(rut = mi_rut)
    context = {'Alumno':alumnos}
    return render(request , 'personas/datos_alumno.html', context)

def eliminar(request):
    print("hola esto es buscar")
    context = {}
    return render(request, 'personas/boton_eliminar.html', context)

def eliminar_por_rut(request):
    print("hola esto es eliminar_por_rut")
    mi_rut = request.POST['rut']
    alumnos = Alumno.objects.get(rut = mi_rut)
    alumnos.delete()
    context={}
    context = {'Alumno':alumnos}
    return render(request , 'personas/mensaje_alumno_eliminado.html', context)

def agregar(request):
    print("hola esto es agregar")
    context = {}
    return render(request, 'personas/formulario_agregar.html', context)

def agregar_alumno(request):
    print("hola estoy en agregar alumno .....")
    if request.method == 'POST':
        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_paterno = request.POST['apaterno']
        mi_materno = request.POST['amaterno']
        mi_fechaNac = request.POST['fechaNac']
        mi_genero = request.POST['genero']
        mi_foto = request.FILES['foto']
        if mi_rut!="":
            try:
                alumno = Alumno()

                alumno.rut = mi_rut
                alumno.nombre = mi_nombre
                alumno.apellido_paterno = mi_paterno
                alumno.apellido_materno = mi_materno
                alumno.fecha_nacimiento = mi_fechaNac
                alumno.genero = mi_genero
                alumno.foto = mi_foto
                alumno.activo = 1

                alumno.save()

                return render(request, 'personas/mensajes_datos_grabados.html', {})

            except alumno.DoesNotExist:
                return render(request, 'personas/error/error_204.html', {})
        else:
            return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})

def editar(request):
        print("hola esto es editar")
        context = {}
        return render(request, 'personas/boton_editar.html', context)

def buscar_para_editar(request):
        print("hola esto es buscar_para_editar")
        mi_rut = request.POST['rut']
        alumnos = Alumno.objects.get(rut=mi_rut)
        context = {'alumno': alumnos}
        return render(request, 'personas/formulario_editar.html', context)


def actualizar_alumno(request):
    print("hola estoy en actualizar alumno .....")
    if request.method == 'POST':
        mi_id = request.POST['id_alumno']
        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_paterno = request.POST['apaterno']
        mi_materno = request.POST['amaterno']
        mi_fechaNac = request.POST['fechaNac']
        mi_foto = request.FILES['foto']
        mi_genero = request.POST['genero']
        if mi_rut!="":
            try:
                alumno = Alumno()

                alumno.id_alumno = mi_id
                alumno.rut = mi_rut
                alumno.nombre = mi_nombre
                alumno.apellido_paterno = mi_paterno
                alumno.apellido_materno = mi_materno
                alumno.fecha_nacimiento = mi_fechaNac
                alumno.genero = mi_genero
                alumno.foto = mi_foto
                alumno.activo = 1

                alumno.save()

                return render(request, 'personas/mensajes_datos_grabados.html', {})

            except alumno.DoesNotExist:
                return render(request, 'personas/error/error_204.html', {})
        else:
            return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})

def menu(request):
    print("hola esto es vista menu")
    alumnos = Alumno.objects.all()
    context = {'alumnos':alumnos}
    return render(request, 'personas/menu_alumno.html', context)
