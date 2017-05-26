#coding=UTF-8
class Student(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
            
        return a
    
f=Student()

print(f[1])    
        
        