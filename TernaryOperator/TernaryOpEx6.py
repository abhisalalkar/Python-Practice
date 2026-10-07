#Program for cal area of circle when radius is +v
r=float(input("Enter Radius :"))
result=3.14*r**2 if r>0 else "{} is Invalid Input".format(r)
print("Area of Circle=",result)