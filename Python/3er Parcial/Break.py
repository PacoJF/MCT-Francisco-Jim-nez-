while True: 
  number = int(input("Enter a number: "))
  number = number + number
  print(number)
  end = input("Would you like to terminate the program? Yes/No ")
  if (end == "Yes"):
    break

print("Program terminated")