#Program for generating 1 to n where n is +ve
n=int(input("Enter How many number you want generate: "))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print("-"*50)
    print("Numbers Within: {}".format(n))
    print("-"*50)
    i=1
    while(i<=n):
        print("\t{}".format(i))
        i+=1 #i=i+1
    else:
        print("-"*50)
    print("Program execution completed")