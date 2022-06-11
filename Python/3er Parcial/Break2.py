import os
import random
base = "0123456789"

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

while True:
  print("Bienvenido a Atencion al Cliente de Megaplay")
  print("¿En que puedo ayudarte?")
  print("1. Reporte de Fallas")
  print("2. Opcion a Pago")
  print("3. Promociones")
  in1 = input()
  clearConsole()
  if (in1 == "1"):
    print("Reporte de Fallas")
    print("Indique el tipo de falla")
    print("1. Television")
    print("2. Red")
    in2 = input()
    clearConsole()
    if (in2 == "1"):
      print("Use el siguiente numero de reporte para solucionar el problema")
      number = ""
      for i in range(10):
        number = number + random.choice(base)
      print(number)
      print("¿Desea regresar a la pagina principal? s para si y n para no")
      q = input()
      if (q == "s"):
        clearConsole()
        continue
      else:
        break
    if (in2 == "2"):
      print("Use el siguiente numero de reporte para solucionar el problema")
      number = ""
      for i in range(10):
        number = number + random.choice(base)
      print(number)
      print("¿Desea regresar a la pagina principal? s para si y n para no")
      q = input()
      if (q == "s"):
        clearConsole()
        continue
      else:
        break
  if (in1 == "2"):
    print("Seleccione el metodo de pago")
    print("1. Tarjeta de credito")
    print("2. Tarjeta de debito")
    in2 = input()
    if (in2 == "1"):
      clearConsole()
      print("Ingrese el numero de trajeta")
      tarjeta = input()
      print("Su pago fue recibido")
      print("¿Desea regresar a la pagina principal? s para si y n para no")
      q = input()
      if (q == "s"):
        clearConsole()
        continue
      else:
        break
      in2 = input()
    if (in2 == "2"):
      clearConsole()
      print("Ingrese el numero de trajeta")
      tarjeta = input()
      print("Su pago fue recibido")
      print("¿Desea regresar a la pagina principal? s para si y n para no")
      q = input()
      if (q == "s"):
        clearConsole()
        continue
      else:
        break
  if (in1 == "3"):
    print("10% de descuento en videojuegos de EA con pago de contado")
    print("15% de descuento en pantallas con pago de contado")
    print("6 meses sin intereses en computadoras")
    print("¿Desea regresar a la pagina principal? s para si y n para no")
    q = input()
    if (q == "s"):
        clearConsole()
        continue
    else:
        break 