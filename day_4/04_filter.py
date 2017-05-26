# 用来过滤序列

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 删掉偶数 只保留奇数

def  is_odd(n):
	return n%2==1

a=list(filter(is_odd,[1,2,3,4,5,6,7,8,9,0]))

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
print(a)








# 去素数
#可以先构造一个从3开始的奇数序列：

def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

#然后定义一个筛选函数：
def _not_divisible(n):
	return lambda x:x % n >0

def primes():
	yield 2
	it = _odd_iter()
	while  True:
		n= next(it)
		yield n
		it = filter(_not_divisible(n),it)
		for n in primes():
			if n<1000:
				print(n)
			else:
				break	

		