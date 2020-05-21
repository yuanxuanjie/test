import queue,time,threading
def shuchu():
    f = open('1.txt','r+')
    for i in f.read():
        print(i)
class de(object):
    def __init__(self,*args):
        self.name = name
        self.password = password
    def sc (self):
        count = 0
        try:
            f = open('1.txt','w+')
            while True:
                for i in range(1,15):
                    count+= 1
                    f.write(str(i))
                    if count == 10:
                       f.close()
                       return shuchu()
        except EOFError as e:
            print(e)


if __name__ == "__main__":
    name = 'jeco'
    password = '123.com'
    star = de(name,password)
    star.sc()
