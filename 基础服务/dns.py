
#!/usr/bin/python3
import  dns.resolver
dm = input('>:')
A = dns.resolver.query(dm,'A')
for i in A.response.answer:
    for z in i.items:
        if z.rdtype == 1:
            print(z.address)
print(A)
print(i)
print(i.items)
print(z)
print(z.rdtype)
print(z.address)
print(A.response.answer)
print(dns.resolver.query('www.baidu.com','A'))


