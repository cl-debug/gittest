#List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
li = list(range(1,11))

print(li)

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

l=[]

for x in range(1,11):
	l.append(x*x)

print(l)

#列表生成式则可以用一行语句代替循环生成上面的list

Re=[ x*x for x in range(1,11)]

Re=[x+x for x in range(1,11)]
# 生成列表时  要把生成的元素放到最前面 后面加for循环 就可以生成一个列表


# for循环后面可以加判断
# 所有偶数的和
Re = [x+x for x in range(1,11) if x%2==0]

#所有偶数的平方
Re = [x*x for x in range(1,11) if x%2==0]

# 可以用两层循环形成全排列
Re = [x+y for x in "ABC" for y in "def"]

print(Re)


