#coding=UTF-8
def my_abs(a):
    if a>0:
        return a
    elif a<0:
        return -a

print(my_abs(-100))

#空函数
def my():
    pass

#参数检查

def my_abs1(a):
    if not isinstance(a,(int,float)):
        raise TypeError('bad')
    if a>0:
        return a
    elif a<0:
        return -a
my_abs1('a')

#Python的函数返回多值其实就是返回一个tuple
#函数执行完毕也没有return语句时，自动return None