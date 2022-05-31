while True:

  speed = int(input("Meteorite speed: "))

  if (speed >= 25):
   print ("Warning! meteorite speed is", speed,"km/s, Critical impact")

  elif (speed == 20):
   print ("Meteorite speed is", speed, "km/s, lightning in the sky")

  elif (speed >= 10):
    print ("Meteorite speed is", speed, "km/s, shooting star")

  else:
    print ("No issues")