'''
网易云音乐歌词 时间格式替换（批量）
自动去除多余的 0 ，使时间均为2位数字
若原本就是两位则不替换
修改后亦可用于文本替换
例如：
[03:29.680]穿越蓝天   ---替换为--->   [03:29.68]穿越蓝天
[03:59.90]以无限延伸的光芒   ---不替换--->   [03:59.90]以无限延伸的光芒
'''
import os
import time
import re


def addfiles():  # 生成一个文件名的list，方便批量处理
    files = []
    for file in os.listdir("./input/"):
        if file.endswith(".lrc"):  # 筛选文件后缀
            files.append(file)
    return files


def read(_filename):
    # 自动判断utf-8 或 gbk
    try:
        f_in = open("./input/%s" % (_filename), encoding="utf-8")
        lines = f_in.readlines()  # 采用逐行读取，为 "正则逐行匹配，并在匹配的文本中使用replace()" 准备
    except UnicodeDecodeError:
        f_in = open("./input/%s" % (_filename), encoding="gbk")
        lines = f_in.readlines()
    f_in.close()
    return lines


def match_replace(_text):
    list_1 = re.findall(r".*\d\d0].*\n", _text,)  # 匹配含有 "<数字><数字>0]" 的行（含换行符）
    if list_1 == []:
        # 若行不符合正则，则该行按原数据写入新文件
        f_out.write(_text)
        print(_text)
    else:
        # 若行符合正则，则该行经过进一步替换后写入新文件
        for text1 in list_1:
            text2 = text1.replace("0]", "]")
            f_out.write(text2)
            print(text2)
    f_out.flush()  # 立即将改动写入文件，避免丢失


if __name__ == "__main__":
    inputfiles = addfiles()  # 生成文件名列表
    print("共读取到"+str(len(inputfiles))+"个文件：\n"+str(inputfiles)+"\n即将开始……\n")
    time.sleep(1)
    i = 1  # 用于记次(第几个文件)
    for inputfile in inputfiles:
        # 新建文件用于输出
        if not os.path.exists("./output"):
            os.mkdir("./output")
        f_out = open("./output/%s" % (inputfile), "w+", encoding="utf-8")

        lines = read(inputfile)  # 逐行读取生成"行"列表
        for line in lines:
            match_replace(line) # 逐行匹配，替换，写出

        f_out.close
        print("\n==========以上是第"+str(i)+"个文件=========\n")
        i = i + 1
