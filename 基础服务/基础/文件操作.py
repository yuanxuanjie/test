'''
f = open('文件','w')  #以写的模式打开文件
f.write('hehehehe,\n')
f.write('hahahaha')
f.close()

f = open('文件','r') #以读的模式打开
print(f.read())
f.close()

f = open('文件','a',encoding='utf-8',)  #以追加的模式打开文件
f.write('还好吧！')
f.write('还好吧！')
'''

'''
#方法
f = open('文件','r')
print(f.tell())
f.readline()
print(f.tell())
f.seek(0)
print(f.tell())
f.write('hello 1 \n')
f.flush()

import sys,time

for i in range(20):
    sys.stdout.write('#')
    time.sleep(0.5)
    '''
#修改
f = open('文件','r',encoding='utf-8')
f_new = open('file','w',encoding='utf-8')
for i in f:
    if '开户行' in i:
        i=i.replace('开户行','某行')
    f_new.write(i)
f.close()
f_new.close()

