#代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator） 
#decorator就是一个返回函数的高阶函数

def now():
	print("2015-07-08 11:11:11")
d=now
d()


#函数对象有一个__name__属性，可以拿到函数的名字：
now._name_='name'



print(d._name_)



def logs(func):
	def wrapper(*arg,**kw):
		

