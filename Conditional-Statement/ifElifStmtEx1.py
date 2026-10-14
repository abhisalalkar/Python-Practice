#program for accepting a two numerical value and find biggest
a=float(input("Enter Number of a: "))
b=float(input("Enter Number of b: "))
if(a>b):
    print("Max({},{}={}".format(a,b,a))
elif(b>a):
    print("Max({},{})={}".format(a,b,b))
else:
    print("Both Value Are Equal")
print("Program execution end")