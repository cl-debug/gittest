#coding=UTF-8
#排序算法 sorted
lists=[26,24,62,55,15]

print(sorted(lists))

#sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序

def sorted_re(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

print(sorted(lists,sorted_re))


#字符串排列
lists_1=['bob', 'about', 'Zoo', 'Credit']

#默认按照ascii 码排序
print(sorted(lists_1))

#们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能定义出忽略大小写的比较算法就可以：

def sorted_er(s1,s2):
    u1=s1.upper() #转为大写
    u2=s2.upper() #转为大写
    
    if u1>u2:
        return 1
    if u1<u2:
        return -1
    return 0

print(sorted(lists_1,sorted_er))