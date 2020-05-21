import re,time,threading,socket
class home(object):
    def __init__(self,name,index):
        self.name = name
        self.index = index

    def ftp(self):
        try:
            pass
        except EOFError as e:
            print(e)

    def ssh(self):
        try:
            pass
        except EOFError as e:
            print(e)
name,passwd= 'jeco','123'
def zs(func):
    def tp(*args,**kwargs):

        username=input('username:')
        password = input('password:')
        if username == name and passwd ==password:
            print('\033[32:1m welcome is %s\033[0m' % username)
            res = func()
        else:
            print('\033[31:1m In username or password \033[0m')

    return tp

def index():
    print('welcome to index')
@zs
def home():
    print('welcome to home')

home()
index()





