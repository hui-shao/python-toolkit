import os


def change_suffix(_mainpath, _suffix):
    files = os.listdir(_mainpath)
    print("共读取到"+str(len(files))+"个文件：\n"+str(files))
    for filename in files:
        fullpath = _mainpath+filename
        os.rename(fullpath, fullpath+"."+_suffix)
    print("修改成功")


if __name__ == "__main__":
    mainpath = "./input/" # 文件所在目录 注意结尾时的 / 别漏了
    suffix = "lrc" # 需要添加的后缀
    change_suffix(mainpath, suffix)
