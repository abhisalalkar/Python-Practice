#Program for Swapping of any Two Integer Values--Logic-3
a,b=input("Enter Number of a:"),input("Enter Number of b:")
print("-"*90)
print("Display Number of a:{}".format(a))
print("Display Number of b:{}".format(b))
print("-"*90)
#Swapping
a=a+b
a=b-a
b=a-b
print("Swapped Number of a:{}".format(a))
print("Swapped Number of b:{}".format(b))