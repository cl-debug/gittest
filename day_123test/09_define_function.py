def my_(x):
	if x>0:
		return x
	else:
		return -x

#如果你已经把my_abs()的函数定义保存为abstest.py文件
#那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：			


#空函数  pass

def po():
	pass


# 参数检查
#对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：

def my_abs(x):
    if not isinstance(x, (int, float)):
        return 1
    if x >= 0:
        return x
    else:
        return -x	

result=my_abs("nihao")       
print(result)