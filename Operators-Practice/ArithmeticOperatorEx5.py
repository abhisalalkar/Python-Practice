#Demonstrating ATM Amount of Dispatching the Notes
wamt=int(input("Enter hoe many amount you want to withdraw"))
#==========
rs500=wamt//500
wamt=wamt%500
#==========
rs200=wamt//200
wamt=wamt%200
#==========
rs100=wamt//100
wamt=wamt%100
print("-"*90)
print("Dispatching Cash Detail")
print("\tNumber of 500:{}".format(rs500))
print("\tNumber of 200:{}".format(rs200))
print("\tNumber of 100:{}".format(rs100))
print("-"*90)