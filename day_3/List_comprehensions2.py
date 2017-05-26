#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块
l=[ d for d in os.listdir('.')] # os.listdir列出文件目录
print(l)

d = {'x': 'A', 'y': 'B', 'z': 'C' }

m=[k + '=' + v for k, v in d.items()]

# v.lower() 全部转换为小写
m=[k + '=' + v.lower() for k, v in d.items()]

print(m)


L=["Hello","Ni","Hao"]

print([x.lower() for x in L])