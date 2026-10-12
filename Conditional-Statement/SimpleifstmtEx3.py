#Program for accepting three numerical values and find biggest
a=float(input("Enter the first number a: "))
b=float(input("Enter the second number b: "))
c=float(input("Enter the third number c: "))
if(b<=a>c):
    print("Max({},{},{})={}".format(a,b,c,a))
if(a<b>=c):
    print("Max({},{},{})={}".format(a,b,c,b))
if(a<=c>b):
    print("Max({},{},{})={}".format(b,a,c,c))
if(a==b==c):
    print("All values are equal")
print("Completed")