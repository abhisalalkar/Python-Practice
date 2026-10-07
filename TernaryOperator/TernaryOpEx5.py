#Program for accepting any word and decided where it is vowel word or not
word=input("Enter a word :")
res="Vowel" if("a" in word or "e" in word or "i" in word or "o" in word or "u" in word or
                "A" in word or "E" in word or "I" in word or "0" in word or "U" in word)\
            else "Not vowel word"
print("'{} is {}".format(word,res))