#coding=UTF-8
import logging
#它允许你指定记录信息的级别，有debug，info，warning，error等几个级别    
logging.basicConfig(level=logging.INFO)

s='0'

n=int(s)

logging.info('n=%s'%(n))
