import os
import time
import platform
import json


def addfiles():
    files = []
    for file in os.listdir("./input/"):
        if file.endswith(".txt"):
            files.append(file)
    return files


def read(filename):
    try:
        f_in = open("./input/%s" % (filename), encoding="utf-8")
        t = f_in.read()
    except UnicodeDecodeError:
        f_in = open("./input/%s" % (filename), encoding="gbk")
        t = f_in.read()
    f_in.close()
    print(t)
    return t


def write(filename, text_in, mode):  # 传入参数 文件名 内容 转换模式(逐个文件/所有文件)
    if not os.path.exists("./converted"):
        os.mkdir("./converted")
    if mode == "1":
        with open("./converted/%s" % (filename), "w", encoding="utf-8") as f_out:
            f_out.write(text_in)
    elif mode == "2":
        with open("./converted/%s" % (filename), "w", encoding="gbk") as f_out:
            f_out.write(text_in)
    elif mode == "3":  # 逐个文件选择转换模式
        while True:  # 主要是用于处理输入流异常，下同
            b = input("\n1. utf-8\n2. gbk\n输入你的选择：")
            if b == "1":
                with open("./converted/%s" % (filename), "w", encoding="utf-8") as f_out:
                    f_out.write(text_in)
                clean()
                break
            elif b == "2":
                with open("./converted/%s" % (filename), "w", encoding="gbk") as f_out:
                    f_out.write(text_in)
                clean()
                break
            else:
                print("错误，重新输入")
                time.sleep(2)
                clean()


def clean():
    if sys_type == "Windows":
        os.system("cls")
    elif sys_type == "Linux":
        os.system("clear")


if __name__ == "__main__":
    inputfiles = addfiles()
    print("共读取到"+str(len(inputfiles))+"个文件：\n"+str(inputfiles)+"\n")
    time.sleep(1)
    i = 1
    sys_type = platform.system()  # 判断系统平台，为os命令使用做准备
    while True:
        mode = input(
            "\n1. 全部转为utf-8\n2. 全部转为gbk\n3. 逐个文件选择\n输入你的选择：")  # 选择转换模式
        if mode in ["1", "2", "3"]:
            break
        else:
            print("错误，重新输入")
            time.sleep(2)
            clean()
    for inputfile in inputfiles:
        text = read(inputfile)
        print("===================\n以上是第"+str(i)+"个\n")
        write(inputfile, text, mode)
        i = i + 1
    print("\n转换完成！")
