# -*- coding: utf-8 -*-
#著名的斐波拉契数列  除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
	n,a,b=0,0,1  #变量的命名方式
	while n <max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'	

#fib(10)


#可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。



#上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了 yield yield yield

def fib_(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'

re=fib_(10)	
for  r in re:
	print(r)

#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：	