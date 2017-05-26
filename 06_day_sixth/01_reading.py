#coding=UTF-8

f=open('read.txt','r')
#标示符'r'表示读，这样，我们就成功地打开了一个文件


#如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示

print  f.read()

#最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的

f.close()

#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用
#为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现

try:
    f=open('read.txt','r')
    print f.read()
finally:    
    if f:
        f.close()
        
#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法        

with open('read.txt','r') as f:
    print f.read()

#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
#每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉