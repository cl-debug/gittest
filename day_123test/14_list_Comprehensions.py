print([x * x for x in range(1,10)])

#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

#还可以使用两层循环，可以生成全排列

print([x+y for x in "abc" for y in "def"])

import os # 导入os模块，模块的概念后面讲到

print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录
