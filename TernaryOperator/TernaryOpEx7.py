#program for Deciding whether It is Upper OR Lower by accepting an alphabet
alphabet=input("Enter Any Alphabet:")
result="Upper Case Alphabet" if ord(alphabet) in range(65,91) \
    else "Lower Case Alphabet " if ord(alphabet) in range(97,123) else "Not an Alphabet"
print("'{}' is {}".format(alphabet,result))
