import sys
print(sys.getdefaultencoding())
s = '你好'
s_to_gbk = s.encode('gbk')
print(s_to_gbk)

#转换为utf-8

s_to_utg8 = s_to_gbk.decode('gbk').encode('utf-8').decode('utf-8')
print(s_to_utg8)