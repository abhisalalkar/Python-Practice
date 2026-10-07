#Program for accepting any two numerical
# values and find biggest of among them and check for equality
a,b=float(input("Enter a number of a:")),float(input("Enter a number of b:"))
bigv= a if a>b else b if b>a  else "Both values are equal"
print("Big({},{})={}".format(a,b,bigv))