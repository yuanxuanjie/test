"""
name=input('name:')
job=input('job')
ap=input('axl')

info = '''
------------------info or {name}
name:{name}
job:{job}
ap:{ap}
'''.format(name=name,
           job=job,
           ap=ap)
print(info)
"""
t = '窝气'
print(t.encode('utf-8'))
print(t.encode('utf-8').decode('utf-8'))

a = [0,1,2,3]
for i,f in enumerate(a):
    print(i,f)

print(a.index(1))

ak = {
    a:'wo',b:'ta',c:'ni'
}

if ak in a:
    print(ak)