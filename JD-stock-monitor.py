import requests
import time
import os
import platform
import random

def sendMail(name,url,timestamp):
    import smtplib
    from email.mime.text import MIMEText
    # email 用于构建邮件内容
    from email.header import Header

    # 用于构建邮件头

    # 发信方的信息：发信邮箱，邮箱授权码
    from_addr = '<your email address>@xxx.com'
    password = 'your verify code'

    # 收信方邮箱
    to_addr = mail_receiver

    # 发信服务器
    smtp_server = 'smtp.xxx.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText("你关注的商品：\n\n"+name+"："+url+"\n\n现在有货啦，赶快去购买吧\n"+timestamp,"plain","utf-8")

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    #  邮件主题
    msg['Subject'] = Header("【%s】" % (name) + "到货提醒    " + timestamp)

    try:
        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server) # 不传入参数似乎会报错
        server.connect(smtp_server, 465)
        # 登录发信邮箱
        server.login(from_addr, password)
        # 发送邮件
        server.sendmail(from_addr, to_addr.split(","), msg.as_string())
        # 关闭服务器
        server.quit()
        print("\n---邮件发送成功---")
    except smtplib.SMTPRecipientsRefused:
        print('Recipient refused')
    except smtplib.SMTPAuthenticationError:
        print('Auth error')
    except smtplib.SMTPSenderRefused:
        print('Sender refused')
    except smtplib.SMTPException as e:
        print(e.message)

def clean():
    if sys_type == "Windows":
        os.system("cls")
    elif sys_type == "Linux":
        os.system("clear")


#############################
#                           #
#         Code Start        #
#                           #
#############################

# 记录第几次操作
flag = 0 
# 判断系统类型
sys_type = platform.system()
# 收件邮箱（多个用,分割）
mail_receiver = 'example1@gmail.com,example2@163.com,example3@qq.com'
# 商品的url
urls = [
    'https://c0.3.cn/stock?skuId=1336984&area=16_1370_46145_0&venderId=1000078145&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=158071785741420407990&ch=1&callback=jQuery1571998',
    'https://c0.3.cn/stock?skuId=100011293950&area=16_1370_46145_0&venderId=1000078145&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=158071785741420407990&ch=1&callback=jQuery1314477',
    'https://c0.3.cn/stock?skuId=1163651&area=16_1370_46145_0&venderId=1000078145&buyNum=1&choseSuitSkuIds=&cat=9192,12190,12602&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=158071785741420407990&ch=1&callback=jQuery5088839'
    ]
# 每个url对应名称(方便辨认)
names = ['D7002-H930','H950V-,25只1盒','耳塞']

while (1):
    try:
        session = requests.Session()
        session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Connection": "keep-alive"
        }
        time_now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print('第' + str(flag) + '次    ------    ' + time_now)
        flag += 1
        a = 0 # 用于匹配names列表的索引号
        for url in urls:
            # 商品url
            skuidUrl = 'https://item.jd.com/' + url.split('skuId=')[1].split('&')[0] + '.html'
            name = names[a]
            response = session.get(url)
            #print(response.text)
            if (response.text.find('无货') > 0):
                print('无货:' +name+'：' +skuidUrl)
            else:
                print('有货-有货- 有货啦!:'+name+'：  '+ skuidUrl)
                sendMail(name,skuidUrl,time_now)
            a = a + 1
        time.sleep(random.randint(8,30))
        clean()
    except KeyboardInterrupt:
        print("\n用户终止操作！程序退出...")
        break

