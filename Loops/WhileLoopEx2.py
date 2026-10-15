#Program for Generating n to 1 where  is +ve
n=int(input("Enter how many number you want to generate: "))
if(n<=0):
    print("{} Invalid Input".format(n))
else:
    print("="*50)
    print("Numbers Within: {}".format(n))
    print("="*50)
    i=n
    while(i>=1):
        print("\t{}".format(i))
        i-=1 #i=i-1
    else:
        print("="*50)