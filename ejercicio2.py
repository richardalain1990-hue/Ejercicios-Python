# - Casting basico
# Implicita: int + float = float automaticamente 
resultado = 5 + 2.0
print(resultado)
print(type(resultado))

print("")
#Emplicita: str a int
texto_numero = "42"
numero_real = int(texto_numero)
print(numero_real + 8)

print("") 
#Emplicita: int a str para concatenar
edad = 18
mensaje = "hola, soy Richard y mi edad es " + str(edad)
print(mensaje)

print("")
#float a int
precio = 9.99
print(int(precio))

numero = 7.99
redondeado = round(numero)
print(redondeado) 

print("")
#simularemos input con variables fijas
dato_usuario = "25"
print(type(dato_usuario))

edad_correcta = int(dato_usuario)
print(edad_correcta + 5)

#patron correcto para entrada de datos:
edad = int(input("ingresa tu edad "))

print("")
#Escribe un programa que pida al usuario su nombre y su año de nacimiento (int). Calcula e imprime su edad aproximada restando al año actual (2026)
nombre = input("ingrese su nombre :")
año = int(input("ingrese su año de nacimiento: "))
edad_aproximada = 2026 - año
print(str(nombre)+ str("su edad es: ") + str(edad_aproximada))

