#coding=UTF-8
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print(123456)
    
f=now
f()    
#函数对象有个name属性 可以获得函数的名字
print(now.__name__)

print(f.__name__)


#decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator


#用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def log(func):
    def warpper(*args,**kw):
        print 'call %s'%func.__name__
        return func(*args,**kw)
    return warpper


@log
def now11_():
    print(11111)
    
now11_()    

#把@log放到now()函数的定义处，相当于执行了语句
now = log(now)

