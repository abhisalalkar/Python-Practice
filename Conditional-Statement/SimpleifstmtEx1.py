#Program for accept two numerical values and find biggest
a=float(input("Enter a value of a: "))
b=float(input("Enter a value of b: "))
if(a>b):
    print("Big({},{})={}".format(a,b,a))
if(b>a):
     print("Big({},{})={}".format(b,a,b))
if(a==b):
    print("Both values are equal")
print("Program execution ends")