import pickle


def js(name):
    print('js:', name)
f = open('1.txt','rb')
date = pickle.load(f)
print(date)
print(date['name'])