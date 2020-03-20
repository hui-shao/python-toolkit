from getopt import getopt as get_opt
from os import path as os_path
from os import mkdir as os_mkdir
from os import remove as os_remove
from shutil import move as shutil_move
from shutil import Error as shutil_Error
from sys import argv as sys_argv
from re import findall as re_findall
import time


def main():
    # os.chdir(sys_path[0])  # 切换到脚本所在目录（pyinstaller打包时需要注释掉）
    options()
    loop(filenames)


def options():
    """用于处理传入参数"""
    print("")
    global overwrite
    global filenames
    opts, args = get_opt(sys_argv[1:], '-h-o:-f:', ['help', 'overwrite=', 'filename='])
    if len(opts) <= 1:  # 若未接收到已经预设的命令行参数，则直接采用传入的参数（用于“直接拖文件到py脚本上”时）
        filenames = sys_argv
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
            filenames = re_findall(pattern=r'{(.*?)}', string=opt_value)  # 传入多文件时，路径用{}包裹。此情况下使用正则提取
            print("[+] Files:  ", filenames)
    print("")


def loop(inputfile_s):
    input("\n[*] 按下Enter继续...\n")
    for inputfile in inputfile_s:
        try:
            move(inputfile)
        except Exception as err:
            print(err)


def move(_inputfile):
    name = os_path.basename(_inputfile)  # 从路径截取文件名
    targetdir = time.strftime("%m-%d", time.localtime(os_path.getmtime(_inputfile)))  # 以文件修改日期命名的文件夹
    if not os_path.exists(targetdir):
        os_mkdir(targetdir)
    if os_path.exists(targetdir + '/' + name):
        if overwrite is False:
            print("[+] %s 目标文件已存在，跳过..." % name)
            return 0
        elif overwrite is True:
            print("[+] %s 目标文件已存在，覆盖！" % name)
            os_remove("./%s/%s" % (targetdir, name))
    try:
        shutil_move(_inputfile, targetdir)
        # shutil.copy2(_inputfile, targetdir)
        print("[+] Moving %s ----> ./%s/" % (name, targetdir))
    except shutil_Error as err1:
        print("错误\n", err1)
        exit(1)


if __name__ == "__main__":
    filenames = []
    overwrite = False
    main()
    input("\n[*] 按Enter键退出...")
