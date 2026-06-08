#identificadores y variables 
#variables con snake_case
#Quiero obtener el nombre de un alumno, ¿como debo definir mi identificador?

nombre_alumno = "Richard Chacon"
edad_alumno = 18
promedio_final = 9.5

#constantes con SCREAMING SNAKE CASE 
TASA_IVA = 0.16
CALIFICACION_MINIMA = 6.0
PESO_PARCIAL = 0.20
PI = 3.1416
GRAVEDAD_PLANETA = 9.84
CAPACIDAD_MAXIMA_SALON = 25
PESO_PROYECTO = 0.40

#tipado dinanico - la variable cambia de tipo
dato = 100
print(type(dato))
dato = "cien"
print(type(dato))

#uso de constantes en un calculo 
precio_base = 500.0
precio_final = precio_base * (1 + TASA_IVA)
#rint(f"precio con IVA: ${precio_final:2.f}")

print("")
#define 3 constantes: PESO_PARCIAL = 0.20, PESO_.PROYECTO = 0.40 Y CALIFICACION_MINIMA = 6.0. Luego crea 4 variables con calificaciones y calcula el promedio usando las constantes. imprime si el alumno aprobo o reprobo.
cal1 = 5
cal2 = 5
cal3 = 5
proyecto = 5
suma_calificaciones = float(cal1 + cal2 + cal3)
resultado_proyecto = proyecto * PESO_PROYECTO
resultado_parcial = suma_calificaciones * PESO_PARCIAL 
promedio = resultado_proyecto + resultado_parcial
print ("aprobado" if promedio >= CALIFICACION_MINIMA else "Reprobado")

