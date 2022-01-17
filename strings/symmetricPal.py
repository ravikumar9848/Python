s = input()
f1 = 0
f2  = 0
mid = len(s)//2
if s==s[::-1]:
    f1=1
if (len(s)%2==0) and (s[0:mid]==s[mid:len(s)]):
    f2=1
if f1==1 and f2==1:
    print(s,"is palindrome")
    print(s,"is symmetrical")
elif f1==1 and f2==0:
    print(s,"is palindrome")
    print(s,"is not symmetrical")
elif f1==0 and f2==1:
    print(s,"is not a palindrome")
    print(s,"is symmetrical")
else:
    print(s,"is not a palindrome")
    print(s,"is not symmetrical")
    
    
    