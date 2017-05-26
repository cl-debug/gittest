#coding=UTF-8
try:
    import cPickle as pickle
except ImportError:
    import pickle
    
    
f=open('read.txt','r')

d=pickle.load(f)

f.close()
print d
