'''
def dee(a):
    print("%s 个人" %a)
[dee(i) for i in range(10)] #列表生成式

a= (dee(i) for i in range(10)) #生成器
a.__next__()  #生成下一条数据
'''
import time
#协程
b1 = '韭菜'
def xf(name):
    print('%s 准备吃包子了'%name)
    while True:
        baozi = yield
        print('\033[31:1m [%s]包子来了[%s]开始吃包子了 \033[0m'%(baozi,name))

# a = xf('jsion')
# #a.send(b1)
# a.__next__()
# a.send(b1)

def sc(name):
    a = xf('A')
    a.__next__()
    for i in range(1,11):
        print('\033[32:1m{0}开始做包子了\033[0m'.format(name))
        time.sleep(1)
        a.send(i)
sc('jeco')



