#coding=UTF-8

open(name,'r')

#'r' 读文件
#'rb' 读取二进制文件
#要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：

f = open('/Users/michael/gbk.txt', 'rb')
u = f.read().decode('gbk')

#Python还提供了一个codecs模块帮我们在读文件时自动转换编码

import codecs

with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'