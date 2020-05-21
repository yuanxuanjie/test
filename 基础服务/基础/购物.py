g_list=[
    ('boot',120),
    ('phone',3000),
    ('mac',8000),
    ('office',30)
]
l_list=[]
ma=input('m>>:')
if ma.isdigit():
    ma = int(ma)
    while True:

        for index,i in enumerate(g_list):
            print(index,i)
        gs = input('>>:')
        if gs.isdigit():
            gs = int(gs)
            if gs>=0 and gs<=len(g_list):
                p_gs=g_list[gs]
                if ma >= p_gs[1]:
                    l_list.append(p_gs)
                    ma -= p_gs[1]
                    print('is ma [%s] yu e %s' % (p_gs[0],ma))
                else:
                    print('余额不足')
            else:
                print('spbcz')
        elif gs == 'q':
            print('----------')
            for i in l_list:
                print(i)
            exit()
        else:
            print('expct')

else:
    print('jiabi')