f = open('merge.txt','r')
data = f.read()
u = 0
l= 0
d = 0
for i in data.split():
    for j in i:
        if j.isupper():
            u+=1
        elif j.islower():
            l+=1
        elif j.isdigit():
            d+=1
print(data)
print("\n")
print("Upper Case:",u)
print("Lower case:",l)
print("Digits    :",d) 
            
    