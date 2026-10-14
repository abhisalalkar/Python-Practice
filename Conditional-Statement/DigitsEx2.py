##Accepting the Digits and Display Its Name
#DigitsEx1.py
dobj={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
d=int(input("Enter Any Digits:")) #  0 1 2 3 4 5 6 7 8 9
print("{} is {}".format(d,dobj.get(d) if dobj.get(d)!=None else "+VE Number" if d>9 else "-VE Number" \
    if d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] else "-VE Digit"))