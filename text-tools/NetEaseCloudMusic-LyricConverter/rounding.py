# -*- coding: UTF-8 -*-
import os
import time
import re
import platform


def addfiles():  # 生成一个文件名的list，方便批量处理
    files = []
    for file in os.listdir("./input_1/"):
        if file.endswith(".lrc"):  # 筛选文件后缀
            files.append(file)
    return files


def read(filename):
    try:  # 实现gbk与utf-8两种读入模式自动切换
        f_in = open("./input_1/%s" % filename, encoding="utf-8")
        t = f_in.read()  # 网易云歌词文件本来就是字典
    except UnicodeDecodeError:
        f_in = open("./input_1/%s" % filename, encoding="gbk")
        t = f_in.read()
    f_in.close()
    return t


def write(filename, text_in):  # 传入参数 文件名，内容
    if not os.path.exists("./output"):
        os.mkdir("./output")
    with open("./output/%s" % filename, "w", encoding="utf-8") as f_out:  # 默认以utf-8写出，兼容性好
        f_out.write(text_in)


def convert(text_in):
    text_out = ""
    lines_1 = text_in.split("\n")
    lines_2 = []
    for line_1 in lines_1:
        try:
            num_1 = re.findall(r"\.(\d{3})\]", line_1)[0]
        except IndexError:
            line_2 = line_1
        else:
            num_2 = str(round(int(num_1) / 10)).zfill(2)
            line_2 = re.sub(r"(\.)\d{3}(\].*?)", "." + num_2 + "]", line_1, 1)
        lines_2.append(line_2)
    for new_line in lines_2:
        text_out += new_line + "\n"
    return text_out


def clean():
    if sys_type == "Windows":
        os.system("cls")
    elif sys_type == "Linux":
        os.system("clear")


if __name__ == "__main__":
    sys_type = platform.system()  # 判断系统平台，为clear命令使用做准备
    inputfiles = addfiles()
    print("共读取到" + str(len(inputfiles)) + "个文件：\n" + str(inputfiles) + "\n")
    time.sleep(1)
    clean()
    print("\n开始处理")
    i = 1  # 记录“第几个”文件
    for inputfile in inputfiles:  # 遍历文件列表，读取逐个文件进行处理
        text_1 = read(inputfile)
        print(text_1 + "\n===================\n以上是第" + str(i) + "个\n\n")
        text_2 = convert(text_1)
        write(inputfile, text_2)
        print(text_2 + "\n===================\n以上是处理后的结果\n\n")
        i = i + 1
    print("\n\n转换完成！")
