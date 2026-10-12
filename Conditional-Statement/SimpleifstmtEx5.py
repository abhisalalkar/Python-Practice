#Program for calculating a simple interest provided(p,t,r) all values +Ve Otherwise Corresponding error message
p=float(input("Enter principle amount p: "))
t=float(input("Enter time t: "))
r=float(input("Enter rate of interest r: "))
if(p>0 and t>0 and r>0):
    si=(p*r*t)/100
    totat=si+p
    print("*"*50)
    print("\tPrinciple Amount:{} ".format(p))
    print("\tTime:{} ".format(t))
    print("\tRate:{} ".format(r))
    print("\tTotal Amount to pay:{} ".format(totat))
    print("*"*50)
if(p<=0):
    print("\tPrinciple Amount:{} is Invalid ".format(p))
if(t<=0):
    print("\tTime:{} is Invalid ".format(t))
if(r<=0):
    print("\tRate of interest:{} is Invalid ".format(r))