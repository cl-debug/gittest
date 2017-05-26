#coding=UTF-8

#把变量从内存中变成可存储或传输的过程称之为序列化
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上

#python 提供两个某块支持序列化 cPickle 和 pickle

try:
    import cPcikle as pickle
except ImportError:
    import pickle    
    
#对象序列化并写入文件    

d=dict(name='bob',age=20)

print pickle.dumps(d)

#pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件

f=open("read.txt","w")

pickle.dump(d, f)
f.close()