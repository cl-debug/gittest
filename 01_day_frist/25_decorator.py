#coding=UTF-8
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print '11'
    
f=now

f()

#函数有个__name__属性可以拿到函数的名称

print(f.__name__)

#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

#decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator

def log(func):
    def warpper(*args,**kw):
        print 'call %s'%func.__name__
        return func(*args,**kw)
    return warpper


@log
def now_1():
    print(11111)
    
now_1()    
    
        
    