# Bilibili Bv Av 号码相互转换工具
#
# 算法部分代码来自：
# https://www.zhihu.com/answer/1099438784

import time
import os
import sys
import platform


def av2bv():
    clear()
    print("\n[*] ============= av to bv =============\n")
    print("[*] 输入av（纯数字），例如: 170001\n    若输入 0 则返回上级\n")
    try:
        x = int(input("[+] 输入："))
        if x == 0:
            return 0
        x = (x ^ xor) + add
        r = list('BV1  4 1 7  ')
        for i in range(6):
            r[index_list[i]] = table[x // 58 ** i % 58]
        result = ''.join(r)
    except Exception as err:
        print("\n[!] 出错\n", err)
    else:
        print("[+] 结果：", result)
    input("\n[+] 按 Enter 键继续……")


def bv2av():
    clear()
    print("\n[*] ============= bv to av =============\n")
    print("[*] 输入BV，例如: BV17x411w7KC\n    若输入 0 则返回上级\n")
    x = input("[+] 输入：")
    if x == "0":
        return 0
    try:
        r = 0
        for i in range(6):
            r += tr[x[index_list[i]]] * 58 ** i
        result = (r - add) ^ xor
    except Exception as err:
        print("\n[!] 出错\n", err)
    else:
        print("[+] 结果：", result)
    input("\n[+] 按 Enter 键继续……")


def clear():
    sysinfo = platform.platform()
    if "indows" in sysinfo:
        os.system("cls")
    elif "inux" in sysinfo:
        os.system("clear")
    else:
        os.system("cls")


def quit_(_info):
    print(_info)
    sys.exit()


def choose():
    while 1:
        print("\n[*] ========== MENU ==========\n")
        print("[*] 1. Av 转 Bv\n[*] 2. Bv 转 Av\n[*] 0. 退出")
        a = input("\n[+] 选择：")
        if a == "1":
            while 1:
                sig = av2bv()
                if sig == 0:
                    break
            clear()
        elif a == "2":
            while 1:
                sig = bv2av()
                if sig == 0:
                    break
            clear()
        elif a == "0":
            clear()
            break
        else:
            print("[#] 输入有误，请重新输入")
            time.sleep(1.5)
            clear()


if __name__ == '__main__':
    # 初始化生成 tr
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    xor = 177451812
    add = 8728348608
    index_list = [11, 10, 3, 8, 4, 6]  # r列表中的索引号
    try:
        choose()
    except KeyboardInterrupt:
        quit_("\n\n[!] Raised KeyboardInterrupt!   >>>  Exiting……")
