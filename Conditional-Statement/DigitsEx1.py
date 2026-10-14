#Program for accepting digits and display its name
dobj={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
d=int(input("Enter Any Digits:"))
res=dobj.get(d) if dobj.get(d)!=None else "+VE Number" if d>9 else "-VE Number" \
    if d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] else "-VE Digit"
print("{} is {}".format(d,res))