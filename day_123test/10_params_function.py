# 函数的参数

# 1 位置参数
# 2 默认参数

# 3 可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum 

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：    


#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

nums = [1, 2, 3]
calc(*nums)


# 关键字参数

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：

person('Michael', 30)

#也可以传入任意个数的关键字参数：

person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')


#当然，上面复杂的调用可以用简化的写法：

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


# 5 命名关键字参数

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

def person(name, age, *, city, job):
    print(name, age, city, job)

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。    

person('Jack', 24, city='Beijing', job='Engineer')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。    