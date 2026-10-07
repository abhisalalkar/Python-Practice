#Program for accepting any three numerical values
# and find biggest of among them and check for equality
a=float(input("Enter a value of a :"))
b=float(input("Enter a value of b :"))
c=float(input("Enter a value of c :"))
bigv= a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "All values are equal"
