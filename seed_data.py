from ejemplo.models import Familiar, Mascota, Actividad
Familiar(nombre="Maria", direccion="Alem 2200", nacimiento="22-02-1960").save()
Familiar(nombre="Alberto", direccion="Alem 2200", nacimiento="16-05-1967").save()
Familiar(nombre="Vanesa", direccion="Neuquen 2113", nacimiento="13-06-1989").save()
Familiar(nombre="Agustin", direccion="Mendoza 1133", nacimiento="18-08-1987").save()
print("Se cargo con éxito los usuarios de pruebas")

Mascota(nombre="Blanquito", raza="europeo", edad="4").save()
Mascota(nombre="Peludin", raza="europeo", edad="4").save()
Mascota(nombre="Morty", raza="europeo", edad="3").save()
print("Se cargo con éxito los usuarios de pruebas")

Actividad(nombre="Natacion", dia="Martes y Jueves", horario="09:00 am").save()
Actividad(nombre="Calistenia", dia="lunes y Viernes", horario="11:00 am").save()
Actividad(nombre="Yoga", dia="Sabado", horario="15:00 pm").save()
print("Se cargo con éxito los usuarios de pruebas")