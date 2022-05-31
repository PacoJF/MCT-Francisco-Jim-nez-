import datetime 

dia = datetime.date.today()
w = dia.weekday() + 1

if (w == 0):
  print ("feliz domingo")

elif (w == 1):
  print ("es lunes")

elif (w == 2):
  print ("wuhu, es martes")

elif (w ==3):
  print ("aaaaaa, es miercoles")

elif (w == 4):
  print ("eeeeee, es jueves")

elif (w == 5):
  print ("siiiiii, es viernes")

else:
  print ("yahoo, es sabado")