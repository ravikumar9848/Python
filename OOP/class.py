class car:
    def __init__(self,modelname,year,price):
        self.modelname = modelname
        self.year = year
        self.price = price
        
    def price_increase(self):
        self.price = int(self.price*1.15)
    
        

# inheritance
class supcar(car):
    def __init__(self,modelname,yearm,price,cc):
        super.__init__(modelname,year,price)
        self.cc = cc
        

honda  = supcar("City",2017,1000000)
tata = car("Bolt",2016,600000)
'''
print(honda.modelname)
print(honda.price)

honda.cc =  1500

print(honda.cc)
print(honda.__dict__)
print(tata.__dict__)

honda.price_increase()
print(honda.price)
'''
print(honda.year)





print(help(honda))


honda.price_increase()
print(honda.price)