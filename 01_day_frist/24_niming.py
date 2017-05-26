#coding=UTF-8

#匿名函数lambda

l=map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])
print(l)

#lambda x:x*x 相当于 def def g(x): return x*x

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

f= lambda x: x+x

print(f(10))