#coding=UTF-8

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs    

f1,f2,f3=count()
#返回的函数并没有立刻执行，而是直到调用了f()才执行
print(f1()) #9
print(f2()) #9
print(f3()) #9

#原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#返回函数不要引用任何循环变量，或者后续会发生变化的变量

#用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count_1():
    fs=[]
    for i in range(1,4):
        def j(j):
            def g():
                return j*j
            return g
        fs.append(j(i))
    return fs

f1,f2,f3=count_1()

print(f1())
print(f2())
print(f3())