#Program for accepting two numerical values and find the biggest
a=float(input("Enter Value of a :"))
b=float(input("Enter Value of b :"))
if(a>b):
    print("Max({},{})={}".format(a,b,a))
else:
    if(b>a):
        print("Max({},{})={}".format(a,b,b))
    else:
        print("Both values are equal")
    print("\t I am from another statment of inner if..else Stmt")
print("\tI am from other statment of outer if..else Stmt")