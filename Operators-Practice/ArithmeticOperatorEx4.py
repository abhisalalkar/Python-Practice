#Program for calculate square root of given number
#without using pre-defined function sqrt() of math module

import math
n=float(input("Enter a number for cal square root:"))
result=n**0.5 #result=n**(1/2)
print("Sqrt: ({})= {}".format(n,result))
print("---------------OR--------------------------")
print("Sqrt: ({})= {}".format(n,round(result,2)))