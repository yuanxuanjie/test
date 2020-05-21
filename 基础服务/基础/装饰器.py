

"""
import time

def tiemr(func):  #装饰功能的函数
    def dome(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        ks = stop_time-start_time
        print('time:',ks) #print('time%s'%(stop-start))
    return dome
@tiemr
def bar():
    time.sleep(3)
    print('the run bar')
@tiemr
def test1(name):
    time.sleep(1)
    print('name:',name)

bar()
test1('jeco')
"""
username,passwd='jeco','abc123'
def pps(type_home):

#装饰函数附加认证
    print('type:',type_home)
    def ps(func):

        def h_p(*args, **kwargs):
            if type_home == 'local':
                name = input('username:')
                password = input('password:')
                if name == username and passwd == password:
                        print('\033[32:1mwelcome is %s\033[0m' % name)
                        res = func(*args, **kwargs)
                        return res
                        # func(*args,**kwargs)
                else:
                    print('\033[31:1mis username or password \033[0m')
            elif type_home == 'iadp':
                print('没有')
            else:
             print('ERRo')

        return h_p
    return ps

def index():
    print('welcome to index')
@pps(type_home='local')
def home():
    print('welcome to home')
    return 'from home '
@pps(type_home='iadp')
def bbs():
    print('welcome to bbs')

index()
home()
bbs()

