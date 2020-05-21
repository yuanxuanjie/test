import json,pickle
import tesy_json
try:
    f_date = pickle.loads(tesy_json.date)
    t_date = pickle.loads(tesy_json.date3)
    print(t_date)
except Exception as e:
    print(e)
import hashlib
md5 = hashlib.md5
x = 'sjlkfjdslfd'

md5(x)
print(x)
