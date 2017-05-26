#这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
s = input('birth: ')
birth = int(s)
#数据类型转换 int()
if birth < 2000:
    print('00前')
else:
    print('00后')