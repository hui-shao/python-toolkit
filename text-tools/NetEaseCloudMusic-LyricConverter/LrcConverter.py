import json
import os
import time


def addfiles():  # 生成一个文件名的list，方便批量处理
    files = []
    for file in os.listdir("./input/"):
        if file.endswith(".lrc"):  # 筛选文件后缀
            files.append(file)
    return files


def read(filename):
    try:  # 实现gbk与utf-8两种读入模式自动切换
        f_in = open("./input/%s" % (filename), encoding="utf-8")
        dic = json.loads(f_in.read())  # 网易云歌词文件本来就是字典
    except UnicodeDecodeError:
        f_in = open("./input/%s" % (filename), encoding="gbk")
        dic = json.loads(f_in.read())
    f_in.close()
    t = dic["lyric"]  # 取字典中的“lyric”部分
    print(t)
    return t


def write(filename, text_in):  # 传入参数 文件名，内容
    if not os.path.exists("./output"):
        os.mkdir("./output")
    with open("./output/%s" % (filename), "w", encoding="utf-8") as f_out:  # 默认以utf-8写出，兼容性好
        f_out.write(text_in)


if __name__ == "__main__":
    inputfiles = addfiles()
    print("共读取到"+str(len(inputfiles))+"个文件：\n"+str(inputfiles))
    time.sleep(1)
    i = 1  # 记录“第几个”文件
    for inputfile in inputfiles:  # 遍历文件列表，读取逐个文件进行处理
        text = read(inputfile)
        print("===================\n以上是第"+str(i)+"个\n\n")
        write(inputfile, text)
        i = i + 1
    print("\n转换完成！")
