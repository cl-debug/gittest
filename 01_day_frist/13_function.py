#coding=UTF-8
#求绝对值函数
abs(110)
#比较函数cmp(x,y)
#比较函数cmp(x, y)就需要两个参数，如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1
print(cmp(3,2))

#数据类型转换
int()
float()
str()
unicode()
bool()

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

a=abs

print(a(-100))