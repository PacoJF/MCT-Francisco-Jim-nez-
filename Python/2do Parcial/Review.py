#comentarios: son notas para organizar el programa

# print(mensaje): permite mandar informacion a la consola

print ("hola")

print ("saludos")

print (5)

print(5+5)

#constantes son datos que no cambian

dia = 4

print (dia)

pi = 3.14

print(pi)

#variables son datos que pueden o no cambiar

calificacion = 6

print (calificacion)

calificacion = calificacion + 2

print (calificacion)

# print mas bonito

print ("tu claificacion es", calificacion)

print ("hoy es", dia, "de enero")

print (pi, "es el valor de pi que usaremos")

#operadores matematicos suma (+), resta (-),
#multiplicacion (*), division (/)

a = 2 
b = 3

print (a + b)
print (a - b)
print (a * b)
print (b / a)

#loop se refiere a cualquier programa que se pueda ciclar o repetir n numero de veces

#while: mientras una condicion sea verdadera (o no) se ejecuta todo el programa dentro de la misma 

#operadores logicos
#a>b a es mayor que b
#a<b a es menor que b
#a==b a es identico a b

#a>=b a es mayor o igual que b
#a<=b a es menor o igual que b

tomate = 2 
while (tomate > 0):
  print ("hay tomate")
  tomate = tomate - 1 

#identacion: esta nos dice que las lineas pertenecen a un ciclo o condicion, puede ser un simple espacio o un Tab

# while true es una condicion que pregunta si se puede ejecutar, si responde que si el programa se ejecuta

""" while True:
   print ("hola")"""

# input(): nos permite ingresar informacion al programa a traves de la consola


nombre = input()
print ("saludos", nombre)

apellido = input ("apellido: ")
print ("saludos mr.", apellido)

edad = input()
print (edad*10)

# input() solo recibe strings, necesitas convertirla al trabajar con numeros

edad = int(input())
print (edad*10)