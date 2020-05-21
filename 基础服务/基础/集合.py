## 集合
data = [1,2,3,5,2,7]
data = set(data)
list1 = {1,2,4,3}


#交集
print(data.intersection(list1))
print(data & list1) #运算符


#并集 (两个集合合并，并去重)
print(data.union(list1))
print(data | list1) #运算符


#差集（保留data里有，list1里没有的数据）
print(data.difference(list1))
print(data - list1) #运算符


list1.add(98) #增加一项
list1.update([99,100,111]) #添加多项
list1.remove(111) #删除一项
list1.discard('us') #删除不存在的值时，不会报错
print(list1)

