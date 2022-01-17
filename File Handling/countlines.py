f = open('merge.txt','r')
d = f.readlines()
l = len(d)
l_a=0
l_b = 0
l_c = 0
for i in d:
    for j in i:
        if j[0]=='A':
            l_a+=1
        elif j[0]=='B':
            l_b+=1
        elif j[0]=='C':
            l_c+=1
            
print("The Total number of lines:",l)
print("The number of lines starting with A",l_a)
print("The number of lines starting with B",l_b)
print("The number of lines starting with C",l_c)










# ref::   https://www.tutorialaicsip.com/cs-xii-pra/python-file-handling-programs/