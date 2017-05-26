class Student(object):
    
    def __init__(self,name,sorce):
        self.name=name
        self.sorce=sorce
        
    def print_sorce(self):
        print'%s:%s'%(self.name,self.sorce)
        
        
a=Student('name','18')

print a.print_sorce()
            