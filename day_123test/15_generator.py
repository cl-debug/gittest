#生成器 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
#从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

L = [x * x for x in range(10)]

g = (x * x for x in range(10))

#而是通过for循环来迭代它

for n in g:
	print(n)

#斐波拉契数列

def feb(max):
	n,a,b=0,0,1
	while n>max:
		print(b)
        a, b = b, a + b
        n = n + 1
  	return 'done'

#上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了  	      

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'