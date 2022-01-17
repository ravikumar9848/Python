s = input("Enter the string input")
k = int(input("Enter the index of the character"))
if k<=len(s):
    print("The character at Position"+k+"is"+s[k-1])
else:
    print("The length is too large or small")
    
