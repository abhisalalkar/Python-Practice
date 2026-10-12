#Program for accepting a numerical value and decided whether it is +Ve or -Ve
a=float(input("Enter the value of a:"))
if(a==0):
    print("{} is Zero".format(a))
if(a>0):
    print("{} is +Ve".format(a))
if(a<0):
    print("{} is -Ve".format(a))