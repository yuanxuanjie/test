# help(dir)
#!/usr/bin/python3
from IPy import IP
import time
ip_cmd = input('>>:')
ip = IP(ip_cmd)
f = open('1.txt','w')
print(len(ip))
for s in ip:
    print(type(s))
    print(s)
    str(s)

    f.write(s)
    time.sleep()
f.close()
