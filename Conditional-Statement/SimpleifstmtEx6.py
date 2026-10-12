#Program for accepting digits and display it name
d=int(input("Enter Any Digits: "))
if(d==0):
    print("{} is Zero".format(d))
if(d==1):
    print("{} is One".format(d))
if(d==2):
    print("{} is Two".format(d))
if(d==3):
    print("{} is Three".format(d))
if(d==4):
    print("{} is Four".format(d))
if(d==5):
    print("{} is Five".format(d))
if(d==6):
    print("{} is Six".format(d))
if(d==7):
    print("{} is Seven".format(d))
if(d==8):
    print("{} is Eight".format(d))
if(d==9):
    print("{} is Nine".format(d))
if(d>9):
    print("{} is Number".format(d))
if(d<0) and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -Ve Number".format(d))
if(d<0) and d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -Ve Digit".format(d))
print("Program Execution Completed")