L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取出元素
# 开始索引，结束索引 不包括结束索引 0 可以省略
print(L[0:3])
print(L[:3])

#既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片

print(L[-2:])



L = list(range(100))

#前10个数
L[:10]

#后10个数
L[-10:]

#前11-20个数
L[10:20]

#前10个数，每两个取一个
print(L[:10:2])

#所有数，每5个取一个
print(L[::5])


#只写[:]就可以原样复制一个list
print(L[:])



# tuple和字符串 也是 一种list   也可用切片


name= list(range(100))

print(name[-10:-8:2])
