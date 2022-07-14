import os
import sys

if __name__ == '__main__':
    current_path = sys.path[0]
    input_path = str(input("输入目标路径 - 默认为当前目录: "))
    target_path = current_path if not input_path else input_path
    input_port = str(input("输入目标端口 - 默认为8000: "))
    target_port = "8000" if not input_port else input_port
    os.chdir(target_path)
    os.system(f"start cmd /k python -m http.server {target_port}")
