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
        print("[+] Files:  ", filenames)
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
            print("[+] Files:  ", filenames)
    print("")


def loop(inputfile_s):
    input("\n[*] 按下Enter继续...\n")
    start = time.time()
    for inputfile in inputfile_s:
        try:
            move(inputfile)
        except Exception as err:
            print(err)
    end = time.time()
    print("\n[*] Total time: %d s" % (round(end-start, 3)))


def move(_inputfile):
    name = os.path.basename(_inputfile)  # 从路径截取文件名
    targetdir = time.strftime("%m-%d", time.localtime(os.path.getmtime(_inputfile)))  # 以文件修改日期命名的文件夹
    if not os.path.exists(targetdir):
        os.mkdir(targetdir)
    if os.path.exists(targetdir + '/' + name):
        if overwrite is False:
            print("[+] %s 目标文件已存在，跳过..." % name)
            return 0
        elif overwrite is True:
            print("[+] %s 目标文件已存在，覆盖！" % name)
            os.remove("./%s/%s" % (targetdir, name))
    try:
        shutil.move(_inputfile, targetdir)
        # shutil.copy2(_inputfile, targetdir)
        print("[+] Moving %s ----> ./%s/" % (name, targetdir))
    except shutil.Error as err1:
        print("错误\n", err1)
        exit(1)


if __name__ == "__main__":
    filenames = []
    overwrite = False
    main()
    input("\n[*] 按Enter键退出...")
