f = open("sample.txt",'r')

print(f.read())
print(f.readline())
print(f.readline(),end = "#")
for i in  f:
    print(i)
