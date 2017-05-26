#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


#序列求和

from functools import reduce

def ad(x,y):
	return x+y

print(reduce(ad,[1,1,22222]))



#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

def fun(x,y):
	return x*10+y

print(reduce(fun,[1,2,3,4]))


#我们就可以写出把str转换为int的函数：
def fu(x,y):
	return x*10+y

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]	

print(reduce(fu,map(char2num,'13579')))


#整理下
def str2int():
	def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))

print(str2int())	


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))    