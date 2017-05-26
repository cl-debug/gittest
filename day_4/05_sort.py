#list 排序算法

# sorted

l=sorted([1,3,5,7,9,-1])

print(l)

#sorted 是高阶函数 可以接收一个key函数来实现自定义排序

r=sorted([36, 5, -12, 9, -21],key=abs)

print(r)

#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面

#我们给sorted传入key函数，即可实现忽略大小写的排序：

r=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

print(r)

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

r=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

print(r)