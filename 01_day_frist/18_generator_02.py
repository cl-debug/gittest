#coding=UTF-8
#斐波那契数列 除第一个和第二个数外，任意一个数都可由前两个数相加得到

def lib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'    

lib(20)

def fib_1(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    

f= fib_1(50)

print(f)
   