#coding=UTF-8

def fn(x,y):
    return x*10+y

#可迭代对象

print(reduce(fn, (1,2,3)))


#自定义一个转换函数

def str2(s):
    def fn(x,y):
        return x*10+y
    def char2(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2,s))


print(str2('5298'))    


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

s = ['adam', 'LISA', 'barT']
def string_good(s):
    return s[0].upper()+s[1:].lower()
print map(string_good,s)

print(string_good(s))