import cal
#help('modules') #Display all the Modules
import sys   #Python modules search path
import math
import random
import datetime

from matplotlib import pyplot as plt





plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance in km')
plt.title("information")
plt.show()
print(datetime.date.today())
print(random.randrange(0,40))
print(sys.path)
print(dir(cal)) # dir() returns sorted list of strings containing names difined by a module

print(math.factorial(10))
print(math.exp(10))
print(math.sqrt(223))