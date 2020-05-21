print(all([1,-5,3]) )  #判断可迭代对象里是否全部为真 ，是则返回True

print(any([]))   #判断可迭代对象里只要有一个值为真 ，是则返回True

print(bin(7))   #10进制转2进制

a="print('he')"
exec(a)  #把字符串转换为可执行代码

c = lambda n:4 if n<3 else n   #匿名函数，只能用于一些简单的 如：三元运算
print(c(3))

res = filter(lambda n:n>5,range(10))    #过滤掉指定的数据，结合匿名用法,打印大于5的整数
for i in res:
    print(i)

si = frozenset([1,3,54,6,435,23])   #不可变集合，如元组

print(globals())        #返回当前程序所有的全局变量，按照字典的格式

#
# def dd(n):
#     if n > 0 :
#
#         n=n/2
#         n = int(n)
#         print(n)
#         return dd(n)
#     else:
#         print(n)
# dd(5000000)

x = hash('jeco')    #生成一个md5值 ，可用于快速对比文件，和确认文件是否被改动
print(x)

print(pow(2,5))     #返回3的5次方


d = {1:'a',3:'c',2:'b',5:'y',4:'t'}
print(d)
print(sorted(d.items()))      #对字典进行排序


a = [1,2,3,4]
b = ['a','b','c','d']
for i in zip(a,b):print(i)  #把两个列表一一对应的拼接在一起

#ord()

f = open('_TS_SN','rb')
f.read()
#print(f.read().encode('gbk').decode('utf-8'))
print(f.read())
#print(f.read().decode('utf-8'))