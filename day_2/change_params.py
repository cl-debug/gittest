#可变参数 参数个数可变
def cal(*number):
    sum = 0
    for n in number:
        sum=sum+n*n
    return sum


print(cal(1,2,2,2))

#不可变参数
def cal_no(number):

    sum = 0
    for n in number:
        sum = sum +n*n
    return sum

print (cal_no([1,2,2,2]))


#如果已经有一个list 或者tuple 参数前加*
nums = [1,2,3,4,5]

print(cal(*nums))



