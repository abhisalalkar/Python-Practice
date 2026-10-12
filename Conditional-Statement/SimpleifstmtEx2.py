#Program for accepting three numerical values and find biggest
a=float(input("Enter a value of a: "))
b=float(input("Enter a value of b: "))
c=float(input("Enter a value of c: "))
if(a>=b and a>c):
    print("Max({},{},{})={}".format(a,b,c,a))
if(b>a and b>=c):
    print("Max({},{},{})={}".format(a,b,c,b))
if(c>=a and c>b):
    print("Max({},{},{})={}".format(a,b,c,c))
if(a==b and b==c and c==a):
    print("All values are equal")
