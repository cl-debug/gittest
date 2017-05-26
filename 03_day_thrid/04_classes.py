#coding=UTF-8

#定制类

#__str__

class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self): #直接显示变量的调用 而不是显示内存地址的变量
        return 'Student %s'%(self.name)    
    #这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
    #而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    #解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法
    __repr__=__str__    
print Student('chenlong')       




#__iter__  和next常一起使用

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
#该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，
#直到遇到StopIteration错误时退出循环 


class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 # 初始化两个计数器
        
    def __iter__(self):
        return self #示例本身就是可迭代对象，故返回本身
    
    def next(self):
        self.a,self.b=self.b,self.a+self.b #计算下一个值
        if self.a>1000: #退出循环的条件
            raise StopIteration     
        return self.a #返回下一个值
    
for n in Fib():
    print n 
    
#__getitem__
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素

#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法

class Fib1(object):
    
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a     
    
f=Fib1()
print(f[100])    
       
    
        
        
    