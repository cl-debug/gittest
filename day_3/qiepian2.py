# 生成一个0-100的数列
L= list(range(100));


print(L)

# 取出前10个元素 0 可以省略
print(L[:10])
# 取出后10个元素 0 可以省略
print(L[-10:])

# 取出11-20的个数

print(L[10:20])

# 取出 前10个元素  每两个取一个

print(L[:10:2])

#所有的数  每5个去一个

print(L[::5])


# 切片适合list tuple 和string