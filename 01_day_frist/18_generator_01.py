#coding=UTF-8

#果列表元素可以按照某种算法推算出来，就可以在循环过程中不断推算出后续的结果

#在Python中，这种一边循环一边计算的机制，称为生成器：generator。

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

d=[x for x in list(range(10))]

#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
c=(x for x in list(range(10)))

print(c)

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

for a in c:
    print(a)
