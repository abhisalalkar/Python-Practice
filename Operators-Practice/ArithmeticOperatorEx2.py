#Program for calculate simple interest and total amount of pay
p=float(input("Enter Princile Amount :"))
t=float(input("Enter Time :"))
r=float(input("Enter Rate of Interest :"))
#calculate rate of interest and total amount to pay
si=(p*t*r)/100
totalamt=si+p
print("*"*90)
print("\tResult of Simple Interest")
print("*"*90)
print("\tPrinciple Amount: {}".format(p))
print("\tTime: {}".format(t))
print("\tRate of Interest: {}".format(r))
print("\tSimple Interest: {}".format(si))
print("\tTotal Amount of to Pay: {}".format(totalamt))
print("*"*90)
print("*"*90)