#coding=UTF-8

#filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#去掉奇数，只保留偶数
def is_odd(n):
    return n%2==0

print(filter(is_odd, [1,2,3,4,5,6]))

#去掉空元素

def is_empty(s):
    return  s.strip()

print([ x for x in  ['name','','age','','124'] if x .strip()])