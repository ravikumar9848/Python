class student:
    #school is a class variable
    school   = 'sps'
    #  m1,m2,m3 are the instace variables
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    #to use class variables use classmethod decorator
    @classmethod
    def getschool(cls):
        return cls.school
    # "Accessor" fetches the value

    # "Mutator" modifies the value
    '''
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1 = value
        
        '''
    @staticmethod
    def info():
        print("This is student class.. in some module")
    
    
    
s1 = student(31,32,34)
s2 = student(21,23,24)

print(s1.avg())
print(s2.avg())
print(student.getschool())
student.info()

