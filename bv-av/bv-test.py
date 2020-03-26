# Bilibili Bv Av 号码批量转换与校验工具（随机）
#
# 主要用于检验算法
# 核心代码来自：
# https://www.zhihu.com/answer/1099438784
# 本人稍作修改和完善 @ hui-shao


import requests
import json
import random


# backup
# def enc(x):
#     s = [11, 10, 3, 8, 4, 6]  # r列表中的索引号
#     xor = 177451812
#     add = 8728348608
#     x = (x ^ xor) + add
#     r = list('BV1  4 1 7  ')
#     for i in range(6):
#         r[s[i]] = table[x // 58 ** i % 58]
#     return ''.join(r)

def enc(x):
    xor = 177451812
    add = 8728348608
    index_list = [11, 10, 3, 8, 4, 6]  # r列表中的索引号
    x = (x ^ xor) + add
    bv = list('BV1  4 1 7  ')
    for i in range(6):
        bv[index_list[i]] = table[x // 58 ** i % 58]
    return ''.join(bv)


def checkv(x, y):
    if str(enc(int(x))) == str(y):
        return "Valid √"
    else:
        return "Not Valid ×"


if __name__ == "__main__":
    Back_URL = 'https://api.bilibili.com/x/web-interface/archive/stat?aid='
    headers = {
        'Cookie': "Replace Me With REAL COOKIE",
        'Pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    # 初始化生成 tr
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    for i in range(0, 50000):
        av_num = random.randint(100, 9999999)
        resp = requests.get(Back_URL + str(av_num), headers=headers)
        # print(resp.text)
        res = json.loads(resp.text)
        if int(res["code"] == 0):
            print("{} {} {}".format(res["data"]["aid"], res["data"]["bvid"],
                                    str(checkv(res["data"]["aid"], res["data"]["bvid"]))))
