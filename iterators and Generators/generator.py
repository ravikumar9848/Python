def lis():
     
     
     yield 1
     yield 2
     yield 3
values = lis()
print(values.__next__())
for i in values:
    print(i)
#instead of fetching all the values generators fetch the values one at a time   
def lis2_squares():
    n = 1
    while(n<=10):
        sq = n*n
        yield sq
        n+=1
        
val = lis2_squares()
for i in val:
    print(i)
    