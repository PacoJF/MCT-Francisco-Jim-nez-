while True: 
  calificacion1=int(input('Ingresa una calificacion'))
  calificacion2=int(input('Ingresa otra calificacion'))
  calificacion3=int(input('Ingresa otra calificacion'))

  promedio=(calificacion1+calificacion2+calificacion3)/3

  print('promedio:', promedio)

  if promedio<60:
    print('reprobaste')
  
  if promedio>60: 
    print ('aprobaste')

  if promedio>=90: 
    print ('felicidades ganaste una medallafelicidades ganaste una medalla')