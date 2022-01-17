f = open("sample.txt",'a')
inp = input("enter the single line input into file")
f.write(inp)
#writing into file with seperating the lines
n = "\n"
#i1 = 
f.write(input("Enter the 1st line"))
f.write(n)
i2 = input("Enter the 2nd line")
f.write(i2)
f.write(n)
i3 = input("Enter the 3rd line")
f.write(i3)
f.write(n)
f.close()
