import smtplib,string
datas = \
    {
        'host' : 'hwsmtp.qiye.163.com',
        'theme' : 'Python test to SMTP',
        's_inx' : 'yuan_xj_mail@163.com',
        'f_out' : 'yuanxuanjie@manew.com',
        'date' : 'test smtplib'

    }
zu = (

    "发件人:%s" % datas['f_out'],
    "收件人:%s" % datas['s_inx'],
    "Theme:%s" % datas['theme'],
    " %s" % datas['date'],
    "/r/t"
)

f_server = smtplib.SMTP()
f_server.connect(datas['host'],994)
f_server.starttls()
print(datas['f_out'])
f_server.login(datas['f_out'],'z2auS9gZwy9KEaCJ')
f_server.sendmail(datas['f_out'],datas['s_inx'],zu)
f_server.quit()
