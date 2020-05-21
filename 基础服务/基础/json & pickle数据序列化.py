

#Json
import pickle
def js(name):
     print('js:',name)

info = {
     'name':'jeco',
     'age': 23,
     'js':js
}
f = open('1.txt','wb')
date = pickle.dump(info,f)

f.close()

