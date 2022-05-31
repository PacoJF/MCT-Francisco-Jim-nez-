print ("Welcome to Oxxo")
employee = input("Attends: ")
print ("Hello", employee)
customer = input("Customer: ")
print (employee,"attends",customer)

product1 = input("Enter a product: ")
price1 = int(input("Enter the price: "))

product2 = input("Enter a product: ")
price2 = int(input("Enter the price: "))

product3 = input("Enter a product: ")
price3 = int(input("Enter the price: "))

product4 = input("Enter a product: ")
price4 = int(input("Enter the price: "))

product5 = input("Enter a product: ")
price5 = int(input("Enter the price: "))

print ("Subtotal:",price1+price2+price3+price4+price5)

print ("Prices with taxes:")

iva1 = price1+price1*0.16
print (product1,":",iva1)

iva2 = price2+price2*0.16
print (product2,":",iva2)

iva3 = price3+price3*0.16
print (product3,":",iva3)

iva4 = price4+price4*0.16
print (product4,":",iva4)

iva5 = price5+price5*0.16
print (product5,":",iva5)

print ("Total:",iva1+iva2+iva3+iva4+iva5)