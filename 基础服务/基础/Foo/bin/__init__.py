
import os,sys
print(__file__) #获取相对路径
JD_DIR = os.path.dirname(os.path.dirname(__file__))     #动态获取绝对路径
sys.path.append(JD_DIR)  #加入环境变量
from foo import man     #导入主程序

man.ds()
