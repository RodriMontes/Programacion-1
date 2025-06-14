# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "14:00"): "Clase de programación"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato hh:mm): ")

clave = (dia, hora)
if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividad agendada.")