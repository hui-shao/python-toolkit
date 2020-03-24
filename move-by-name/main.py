import getopt
import os
import re
import shutil
import sys
import time


def main():
    os.chdir(sys.path[0])  # 切换到脚本所在目录（pyinstaller打包时需要注释掉）
    options()
    loop(filenames)


def options():
    """用于处理传入参数"""
    print("")
    global overwrite
    global filenames
    opts, args = getopt.getopt(sys.argv[1:], '-h-o:-f:', ['help', 'overwrite=', 'filename='])
    if len(opts) <= 1:  # 若未接收到已经预设的命令行参数，则直接采用传入的参数（用于“直接拖文件到py脚本上”时）
        filenames = sys.argv
        filenames.pop(0)
        print("[+] Files: ", filenames)
        return 0
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            print("[+] Help info")
            exit()
        if opt_name in ('-o', '--overwrite'):
            print("[+] Overwrite: ", opt_value)
            overwrite = opt_value
        if opt_name in ('-f', '--filename'):
            filenames = re.findall(pattern=r'{(.*?)}', string=opt_value)  # 传入多文件时，路径用{}包裹。此情况下使用正则提取
            print("[+] Files: ", filenames)
    print("")


def loop(inputfile_s):
    input("\n[*] 按下Enter继续...\n")
    start = time.time()
    for inputfile in inputfile_s:
        try:
            judge(inputfile)
        except Exception as err:
            print(err)
    end = time.time()
    print("\n[*] Total time: %d s" % (round(end-start, 3)))


def judge(inputfile):
    name = os.path.basename(inputfile)  # 从路径截取文件名
    if (re.search("语文|chin.*?", name, re.IGNORECASE)) is not None:
        target_dir = "1.语文"
    elif (re.search("数学|math.*?", name, re.IGNORECASE)) is not None:
        target_dir = "2.数学"
    elif (re.search("英语|eng.*?", name, re.IGNORECASE)) is not None:
        target_dir = "3.英语"
    elif (re.search("物理|phy.*?", name, re.IGNORECASE)) is not None:
        target_dir = "4.物理"
    elif (re.search("化学|chem.*?", name, re.IGNORECASE)) is not None:
        target_dir = "5.化学"
    elif (re.search("生物|bio.*?", name, re.IGNORECASE)) is not None:
        target_dir = "6.生物"
    else:
        print("[*] %s 未匹配到任何字符，跳过!" % name)
        return 0
    move(inputfile, target_dir)


def move(_inputfile, _targetdir):
    name = os.path.basename(_inputfile)  # 从路径截取文件名
    if not os.path.exists(_targetdir):
        os.mkdir(_targetdir)
    if os.path.exists(_targetdir + '/' + name):
        if overwrite is False:
            print("[+] %s 目标文件已存在，跳过..." % name)
            return 0
        elif overwrite is True:
            print("[+] %s 目标文件已存在，覆盖！" % name)
            os.remove("./%s/%s" % (_targetdir, name))
    try:
        # 测试完修改为剪贴
        shutil.move(_inputfile, _targetdir)
        # shutil.copy2(_inputfile, _targetdir)
        print("[+] Moving %s ----> ./%s/" % (name, _targetdir))
    except shutil.Error as err1:
        print("错误\n", err1)
        exit(1)


if __name__ == "__main__":
    filenames = []
    overwrite = False
    main()
    input("\n[*] 按Enter键退出...")
