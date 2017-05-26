#coding=UTF-8
names=['chen','long','hello','ha']

for i in names:
    print(i)
    
    
lists=list(range(500))
sum=0
for i in lists:
    sum=sum+i
print(sum)    

#while循环

sum= 0
t=90
while t>0:
    sum=sum+t
    t=t-2
print(sum)    


#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }

for x,y in d.items():
    print(x+y)




#break 提前退出循环
#continue 结束这次循环