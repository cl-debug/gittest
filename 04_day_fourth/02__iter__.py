#coding=UTF-8

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法

class Fib(object):
    def __init__(self):
        #初始化两个计数器0 1 
        self.a,self.b=0,1
        
    def __iter__(self):
        return self    
    
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        
        return self.a

    
for i in Fib():
    print i    
            
        
        