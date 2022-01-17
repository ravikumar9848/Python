
f1 = open("sample.txt",'r')
data1 = f1.read()
print(data1)

f2 = open("rp.txt",'r')
data2 = f2.read()
print(data2)
f3 = open("merge.txt",'a')
f3.write(data1)
f3.write(data2)
f1.close()
f2.close()
f3.close()





