#Program for accepting a numerical integer value and decided whether it is even or odd
n=int(input("Enter a Number:"))
result="Even" if(n%2==0) else "Odd"
print("{} is {}".format(n,result))