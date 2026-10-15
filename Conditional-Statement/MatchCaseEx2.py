#Implementing Temperature Conversion Scale
#MatchCaseEx2.py
import sys
s="""===================================================
	Temperature Conversion Scale
===================================================
        1. F to C
        2. F to K
        3. C to F
        4. C to K
        5. K to F
        6. K to C
        7. Exit
==================================================="""
print(s)
ch=int(input("Enter UR Choice:"))
match(ch):
    case 1:
        F=float(input('Enter Temp in terms of F:'))
        C = (F - 32) * (5 / 9)
        print("Temp in terms of F={}".format(F))
        print("Temp in terms in C={}".format(C))
    case 2:
        F = float(input('Enter Temp in terms of F:'))
        K = (F-32)* (5/9) + 273.15
        print("Temp in terms of F={}".format(F))
        print("Temp in terms in K={}".format(K))
    case 3:
        C = float(input('Enter Temp in terms of C:'))
        F = C*(9/5) + 32
        print("Temp in terms in C={}".format(C))
        print("Temp in terms of F={}".format(F))
    case 4:
        C = float(input('Enter Temp in terms of C:'))
        K=C + 273.15
        print("Temp in terms in C={}".format(C))
        print("Temp in terms in K={}".format(K))
    case 5:
        K = float(input('Enter Temp in terms of K:'))
        F = (K-273.15)* (9/5) + 32
        print("Temp in terms in K={}".format(K))
        print("Temp in terms of F={}".format(F))
    case 6:
        K = float(input('Enter Temp in terms of K:'))
        C = K - 273.15
        print("Temp in terms in K={}".format(K))
        print("Temp in terms in C={}".format(C))
    case 7:
        print("Thx for Using this program")
        sys.exit()
    case _:
        print("Ur Selection of Operation is Wrong-try again")





