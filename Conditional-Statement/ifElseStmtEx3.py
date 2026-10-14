#Program for accepting the digits and display its name
d=int(input("Enter Any Digit: "))
if(d==0):
    print("{} is ZERO".format(d))
else:
    if(d==1):
        print("{} is ONE".format(d))
    else:
        if(d==2):
            print("{} is TWO".format(d))
        else:
            if(d==3):
                print("{} is THREE".format(d))
            else:
                if(d==4):
                    print("{} is FOUR".format(d))
                else:
                    if(d==5):
                        print("{} is FIVE".format(d))
                    else:
                        if(d==6):
                            print("{} is SIX".format(d))
                        else:
                            if(d==7):
                                print("{} is SEVEN".format(d))
                            else:
                                if(d==8):
                                    print("{} is EIGHT".format(d))
                                else:
                                    if(d==9):
                                        print("{} is NINE".format(d))
                                    else:
                                        if(d>9):
                                            print("{} is Number".format(d))
                                        else:
                                            if(d<0) and d not in [-1,-2,-3,-4,-5,-5,-6,-7,-8,-9]:
                                                print("{} is -Ve Number".format(d))
                                            else:
                                                print("{} is -Ve Digit".format(d))
print("Program Execution Completed")
