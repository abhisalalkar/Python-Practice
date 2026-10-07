#Program for accepting a value and decided whether it is palindrome or not
value=input("Enter a Value:")
res="Palindrome" if value==value[::-1] else "Not Palindrome"
print("{} is {}".format(value,res))