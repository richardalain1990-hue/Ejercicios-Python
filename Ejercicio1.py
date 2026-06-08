#Richard Alain Chacon Dzul
# Este es un comentario de una linea

#Este es un comentario s
#Que ocupa varias lineas

"""
Este es otro ejemplo
de comentario multilinea 
"""

entero = 42 #Numeros enteros
decimal = 3.1416 #Numeros decimales (float)
logico = True #Boolean
nombre = "Juan" #String 

print(entero)
print(type(decimal))
print(type(logico))
print(type(nombre))

#Declara variables que almacenen su nombre, apellido paterno,
#apellido materno y edad, estatura

Nombre = "Richard"
Apellido_Paterno = "Chacon"
Apellido_Materno = "Dzul" 
Edad = 18 
Estatura = 1.65

print("  ")
print(Nombre)
print(Apellido_Paterno)
print(Apellido_Materno)
print(Edad)
print(Estatura)

#list, tuple, set, dict, arrays, range, frozenset, nontype, complex

#Str
nombreMateria = "Programacion"
print(nombreMateria[0])
print(nombreMateria[-1])
print(nombreMateria[0:6])

#List - mutable
calificaciones = [8.5, 9.0, 7.5, 10.0]
calificaciones.append(9.5)
calificaciones[0] = 8.0
print (calificaciones)

#tuple - inmutable 
coordenadas = (19.4326, -99.1332)
print(coordenadas[0])

#dict - clave:valor
alumno = {"nombre": "Richard", "edad": 18, "promedio": 10}
print(alumno["nombre"])
alumno["promedio"] = 9.6
print (alumno)

#Crea un diccionario con tus datos: nombre, edad, y materia favorita. Imprime solo tu nombre accediendo a la clave correcta.
diccionario = {"nombre": "Alain", "edad": "18", "materia_favorita": "programacion estructurada"}
print(diccionario["nombre"])